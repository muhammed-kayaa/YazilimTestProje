import os
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def _basic_stats(text):
    # lightweight duplicate of training basic_stats: avg sent len, ttr, punct ratio
    import nltk
    try:
        sents = nltk.sent_tokenize(text)
    except Exception:
        sents = [s.strip() for s in text.split('.') if s.strip()]
    
    try:
        words = nltk.word_tokenize(text)
    except Exception:
        words = text.split()
    
    avg_sent_len = np.mean([len(w.split()) for w in sents]) if sents else 0
    ttr = len(set(words)) / (len(words) + 1)
    punct_ratio = sum(1 for ch in text if ch in '!?.,;:') / (len(text) + 1)
    return [avg_sent_len, ttr, punct_ratio]
def predict_text(text, model_name='lr', models_dir=None):
	if models_dir is None:
		# Compute project root relative to this file
		src_dir = os.path.dirname(__file__)
		root_dir = os.path.dirname(src_dir)
		models_dir = os.path.join(root_dir, 'models')
	model_path = os.path.join(models_dir, f'{model_name}.pkl')
	tfidf_path = os.path.join(models_dir, 'tfidf.pkl')
	if not os.path.exists(model_path):
		raise FileNotFoundError(f'Model not found: {model_path}')
	if not os.path.exists(tfidf_path):
		raise FileNotFoundError(f'TF-IDF featurizer not found: {tfidf_path}')

	model = joblib.load(model_path)
	tfidf = joblib.load(tfidf_path)

	# create feature vector
	Xtf = tfidf.transform([text])
	basic = np.array([_basic_stats(text)])
	from scipy.sparse import hstack
	X = hstack([Xtf, basic])

	if hasattr(model, 'predict_proba'):
		proba = float(model.predict_proba(X)[:, 1][0])
	else:
		try:
			score = model.decision_function(X)[0]
			proba = float(1 / (1 + np.exp(-score)))
		except Exception:
			proba = 0.0
	label = int(proba >= 0.5)
	return {'label': label, 'proba': proba}


if __name__ == '__main__':
	import sys
	if len(sys.argv) < 2:
		print('Usage: python predict.py "text to check" [model_name]')
		sys.exit(1)
	text = sys.argv[1]
	model = sys.argv[2] if len(sys.argv) > 2 else 'lr'
	print(predict_text(text, model_name=model, models_dir='models'))

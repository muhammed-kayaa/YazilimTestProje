import os
import sys

# Uncomment for debugging imports, but typically skip since packages should be installed
# def check_requirements():
#   missing = []
#   for pkg in ['joblib', 'sklearn', 'pandas', 'numpy', 'nltk', 'scipy']:
#     try:
#       __import__(pkg)
#     except Exception:
#       missing.append(pkg)
#   if missing:
#     print('Missing packages: ' + ', '.join(missing), file=sys.stderr)
#     print('\nInstall them with (recommended):', file=sys.stderr)
#     print('pip install pandas numpy scikit-learn joblib nltk scipy', file=sys.stderr)
#     sys.exit(1)
# check_requirements()

import joblib
import pandas as pd
import numpy as np
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, roc_auc_score


def basic_stats(text):
  try:
    sents = nltk.sent_tokenize(text)
  except Exception:
    # fallback: split by period if punkt fails
    sents = [s.strip() for s in text.split('.') if s.strip()]
  
  try:
    words = nltk.word_tokenize(text)
  except Exception:
    # fallback: simple split
    words = text.split()
  
  avg_sent_len = np.mean([len(w.split()) for w in sents]) if sents else 0
  ttr = len(set(words)) / (len(words) + 1)
  punct_ratio = sum(1 for ch in text if ch in '!?.,;:') / (len(text) + 1)
  return [avg_sent_len, ttr, punct_ratio]


def collect_from_raw(raw_folder='data/raw'):
  """Try to build a DataFrame from raw sources (relative to project root).

  Supports:
    - data/raw/human/*.txt and data/raw/ai/*.txt (preferred)
    - CSV files under data/raw/ with columns `text` and `label`
  Returns DataFrame with columns `text` and `label` or empty DataFrame.
  """
  rows = []
  # Compute absolute path: <root>/data/raw
  src_dir = os.path.dirname(__file__)
  root_dir = os.path.dirname(src_dir)
  folder = os.path.join(root_dir, raw_folder)
  
  # check human/ai subfolders
  human_dir = os.path.join(folder, 'human')
  ai_dir = os.path.join(folder, 'ai')
  if os.path.isdir(human_dir) or os.path.isdir(ai_dir):
    for label_dir, label in [(human_dir, 0), (ai_dir, 1)]:
      if os.path.isdir(label_dir):
        for fn in os.listdir(label_dir):
          if fn.lower().endswith('.txt'):
            p = os.path.join(label_dir, fn)
            try:
              with open(p, 'r', encoding='utf-8') as f:
                text = f.read()
              rows.append({'text': text, 'label': label})
            except Exception:
              continue
    if rows:
      return pd.DataFrame(rows)

  # fallback: read CSVs in raw folder
  if os.path.isdir(folder):
    for fn in os.listdir(folder):
      if fn.lower().endswith('.csv'):
        p = os.path.join(folder, fn)
        try:
          df = pd.read_csv(p)
          if 'text' in df.columns and 'label' in df.columns:
            rows.append(df[['text', 'label']])
        except Exception:
          continue
  if rows:
    return pd.concat([r if isinstance(r, pd.DataFrame) else pd.DataFrame([r]) for r in rows], ignore_index=True)
  return pd.DataFrame(columns=['text', 'label'])


def load_or_build_dataset(processed_path='data/processed/dataset.csv'):
  src_dir = os.path.dirname(__file__)
  root_dir = os.path.dirname(src_dir)
  processed_abs = os.path.join(root_dir, processed_path)
  
  if os.path.exists(processed_abs):
    df = pd.read_csv(processed_abs)
    if 'text' in df.columns and 'label' in df.columns:
      return df
    else:
      raise ValueError('Processed dataset must contain text and label columns')

  # try to build from raw
  df = collect_from_raw()
  if df.empty:
    raise FileNotFoundError('No processed dataset and no raw data found. Place files under data/raw/human and data/raw/ai or provide data/processed/dataset.csv')

  # basic cleaning
  df['text'] = df['text'].astype(str).map(lambda s: s.replace('\n', ' ').strip())
  df = df.drop_duplicates(subset=['text'])
  # ensure label is numeric 0/1
  df = df[df['text'].map(lambda t: len(t.split()) >= 10)]
  processed_dir = os.path.dirname(processed_abs)
  os.makedirs(processed_dir, exist_ok=True)
  df.to_csv(processed_abs, index=False)
  print('Built processed dataset at', processed_abs)
  return df


def train_models(processed_path='data/processed/dataset.csv', out_dir='models'):
  src_dir = os.path.dirname(__file__)
  root_dir = os.path.dirname(src_dir)
  out_dir_abs = os.path.join(root_dir, out_dir)
  os.makedirs(out_dir_abs, exist_ok=True)

  # ensure nltk punkt_tab tokenizer (newer versions require this)
  try:
    nltk.data.find('tokenizers/punkt_tab')
  except LookupError:
    try:
      nltk.data.find('tokenizers/punkt')
    except LookupError:
      print('Downloading NLTK punkt tokenizer...')
      nltk.download('punkt_tab', quiet=True)
      nltk.download('punkt', quiet=True)

  df = load_or_build_dataset(processed_path)
  # Guard: need at least 2 samples to perform a train/test split
  n_samples = len(df)
  if n_samples < 2:
    print(f'Not enough samples to train ({n_samples}). Need at least 2 samples. Skipping training.')
    return
  
  # Clean: remove rows with NaN or empty text
  df = df.dropna(subset=['text', 'label'])
  df = df[df['text'].astype(str).str.strip() != '']
  
  if len(df) < 2:
    print(f'After cleaning, only {len(df)} samples remain. Need at least 2 samples. Skipping training.')
    return
  
  texts = df['text'].tolist()
  y = df['label'].values

  tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
  Xtf = tfidf.fit_transform(texts)
  basic = np.array([basic_stats(t) for t in texts])
  X = hstack([Xtf, basic])

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

  models = {
    'lr': LogisticRegression(max_iter=2000),
    'rf': RandomForestClassifier(n_estimators=200),
    'svm': SVC(probability=True)
  }

  for name, model in models.items():
    print('Training', name)
    model.fit(X_train, y_train)
    model_path = os.path.join(out_dir_abs, f'{name}.pkl')
    joblib.dump(model, model_path)
    print('Saved', model_path)

    preds = model.predict(X_test)
    if hasattr(model, 'predict_proba'):
      probs = model.predict_proba(X_test)[:, 1]
    else:
      try:
        scores = model.decision_function(X_test)
        probs = (scores - scores.min()) / (scores.max() - scores.min() + 1e-9)
      except Exception:
        probs = np.zeros_like(preds, dtype=float)

    print(name)
    print(classification_report(y_test, preds))
    try:
      print('ROC-AUC', roc_auc_score(y_test, probs))
    except Exception:
      pass

  # save tfidf
  tfidf_path = os.path.join(out_dir_abs, 'tfidf.pkl')
  joblib.dump(tfidf, tfidf_path)
  print('Saved TF-IDF to', tfidf_path)


if __name__ == '__main__':
  train_models()

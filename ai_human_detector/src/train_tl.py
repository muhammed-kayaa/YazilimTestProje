from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
import numpy as np
import pandas as pd

MODEL_NAME = 'dbmdz/bert-base-turkish-cased'

def load_data(path='../data/processed/dataset.csv'):
    df = pd.read_csv(path)
    return df

def preprocess_and_train():
    df = load_data()
    ds = Dataset.from_pandas(df[['text','label']])
    tok = AutoTokenizer.from_pretrained(MODEL_NAME)

    def tok_fn(ex):
        return tok(ex['text'], truncation=True, padding='max_length', max_length=256)

    ds = ds.map(lambda x: tok_fn(x), batched=True)
    ds = ds.train_test_split(test_size=0.1)

    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)

    training_args = TrainingArguments(
        output_dir='../models/tl',
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=2,
        evaluation_strategy='epoch',
        save_strategy='epoch',
        logging_dir='../models/tl/logs'
    )

    def compute_metrics(p):
        preds = np.argmax(p.predictions, axis=1)
        from sklearn.metrics import accuracy_score, precision_recall_fscore_support
        acc = accuracy_score(p.label_ids, preds)
        prec, rec, f1, _ = precision_recall_fscore_support(p.label_ids, preds, average='weighted')
        return {'accuracy': acc, 'precision': prec, 'recall': rec, 'f1': f1}

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=ds['train'],
        eval_dataset=ds['test'],
        compute_metrics=compute_metrics
    )

    trainer.train()

if __name__=='__main__':
    preprocess_and_train()

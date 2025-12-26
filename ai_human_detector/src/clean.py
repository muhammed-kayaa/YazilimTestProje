import re
from bs4 import BeautifulSoup
from langdetect import detect
import pandas as pd
import os


def clean_text(s):
    if not isinstance(s, str):
        s = str(s)
    s = BeautifulSoup(s, "html.parser").get_text()
    s = s.replace("\n", " ").strip()
    s = re.sub(r"\s+", " ", s)
    # normalize quotes
    s = s.replace('\u201c', '"').replace('\u201d', '"')
    return s


def is_language(s, lang='tr'):
    try:
        return detect(s) == lang
    except Exception:
        return False


def pipeline(df, min_words=30, lang=None):
    """Clean and filter a DataFrame with a `text` column.

    Returns a cleaned DataFrame containing at least `text` and `label` (if present).
    """
    df = df.copy()
    df['text'] = df['text'].astype(str).map(clean_text)
    df = df.drop_duplicates(subset=['text'])
    if lang:
        df = df[df['text'].map(lambda t: is_language(t, lang))]
    df = df[df['text'].map(lambda t: len(t.split()) >= min_words)]
    return df


def process_and_save(df, dst='data/processed/dataset.csv', min_words=30, lang=None):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    df2 = pipeline(df, min_words=min_words, lang=lang)
    df2.to_csv(dst, index=False)
    return df2


if __name__ == '__main__':
    src = 'data/raw/all.csv'
    if os.path.exists(src):
        df = pd.read_csv(src)
        out = process_and_save(df, dst='data/processed/dataset.csv')
        print('Processed ->', len(out))
    else:
        print('No default source found. Use data_collect.load_local_samples or call process_and_save with a DataFrame.')

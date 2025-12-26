import os
import pandas as pd

def load_local_samples(folder='data/raw'):
    rows = []
    for fname in os.listdir(folder):
        if fname.endswith('.csv'):
            df = pd.read_csv(os.path.join(folder, fname))
            rows.append(df)
    if rows:
        return pd.concat(rows, ignore_index=True)
    return pd.DataFrame(columns=['text','label','source','license'])

if __name__=='__main__':
    df = load_local_samples()
    print('Loaded', len(df))

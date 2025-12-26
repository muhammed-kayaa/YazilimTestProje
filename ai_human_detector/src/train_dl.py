import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional, Conv1D, GlobalMaxPooling1D
from tensorflow.keras.callbacks import ModelCheckpoint

def load_texts(path='../data/processed/dataset.csv'):
    df = pd.read_csv(path)
    return df['text'].tolist(), df['label'].values

def prepare(texts, max_words=20000, maxlen=300):
    tok = Tokenizer(num_words=max_words)
    tok.fit_on_texts(texts)
    seqs = tok.texts_to_sequences(texts)
    X = pad_sequences(seqs, maxlen=maxlen)
    return X, tok

def lstm_model(max_words, maxlen):
    model = Sequential([
        Embedding(max_words, 128, input_length=maxlen),
        LSTM(64),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def bilstm_model(max_words, maxlen):
    model = Sequential([
        Embedding(max_words, 128, input_length=maxlen),
        Bidirectional(LSTM(64)),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def cnn_model(max_words, maxlen):
    model = Sequential([
        Embedding(max_words, 128, input_length=maxlen),
        Conv1D(128, 5, activation='relu'),
        GlobalMaxPooling1D(),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

if __name__=='__main__':
    texts, y = load_texts()
    X, tok = prepare(texts)
    max_words = 20000
    maxlen = X.shape[1]
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2)

    m = lstm_model(max_words, maxlen)
    m.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3, batch_size=64)
    m.save('../models/lstm.h5')

    m2 = bilstm_model(max_words, maxlen)
    m2.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3, batch_size=64)
    m2.save('../models/bilstm.h5')

    m3 = cnn_model(max_words, maxlen)
    m3.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3, batch_size=64)
    m3.save('../models/cnn.h5')

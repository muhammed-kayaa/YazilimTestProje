import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, roc_curve, auc, classification_report

def load_models():
    models = {}
    models['lr'] = joblib.load('../models/lr.pkl')
    models['rf'] = joblib.load('../models/rf.pkl')
    models['svm'] = joblib.load('../models/svm.pkl')
    return models

def evaluate_models(X_test, y_test):
    models = load_models()
    for name, model in models.items():
        print(f'Evaluating {name}...')
        y_pred = model.predict(X_test)
        print(classification_report(y_test, y_pred))
        
        y_proba = model.predict_proba(X_test)[:, 1]
        fpr, tpr, _ = roc_curve(y_test, y_proba)
        roc_auc = auc(fpr, tpr)
        print(f'ROC-AUC: {roc_auc}')
        
        cm = confusion_matrix(y_test, y_pred)
        print('Confusion Matrix:')
        print(cm)
        print()

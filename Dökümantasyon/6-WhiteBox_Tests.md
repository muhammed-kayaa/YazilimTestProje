# White Box Test Raporu

## Amaç
Kodun içindeki temel fonksiyonların doğru çalıştığını doğrulamak için unit testler uygulanmıştır.

## Kullanılan Araç
- pytest / unittest

## Test Edilen Modüller
- `src/clean.py`
- `src/predict.py`
- `src/train_ml.py`

## Örnek Testler

### Test-1: Temizleme fonksiyonu boş metin kontrolü
```python
def test_clean_empty_text():
    assert clean_text("") == ""


Test-2: Tahmin fonksiyonunun label döndürmesi:

def test_predict_returns_label():
    result = predict_text("örnek metin", "lr")
    assert result["label"] in [0, 1]


Test-3: Dataset kolon kontrolü 

def test_dataset_columns():
    df = pd.read_csv("data/processed/dataset.csv")
    assert "text" in df.columns and "label" in df.columns


---
 
 
 Sonuç

White-box testler başarıyla çalıştırılmıştır ve sistemin temel fonksiyonları doğrulanmıştır.
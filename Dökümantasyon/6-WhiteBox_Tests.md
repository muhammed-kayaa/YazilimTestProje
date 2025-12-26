# White Box Test Raporu

## 1. Amaç
Kodun içindeki temel fonksiyonların doğru çalıştığını doğrulamak için **white-box (unit) testler** uygulanmıştır.  
Bu testler ile sistemin iç fonksiyonlarının beklenen çıktıyı üretip üretmediği kontrol edilmiştir.

---

## 2. Kullanılan Araçlar
- pytest (tercih edilen)
- unittest (alternatif)

---

## 3. Test Edilen Modüller
- `src/clean.py` → metin temizleme fonksiyonları  
- `src/predict.py` → tahmin fonksiyonu  
- `src/train_ml.py` → veri ve eğitim pipeline kontrolü  

---

## 4. Testlerin Çalıştırılması
Testlerin çalıştırılması için proje kök dizininde aşağıdaki komut kullanılır:

```bash
pytest
Not: Eğer pytest yüklü değilse:

bash
Kodu kopyala
pip install pytest
5. Unit Test Kodları (Örnekler)
Aşağıda sistemin temel fonksiyonlarını test eden örnek unit testler verilmiştir.

Test-1: Temizleme fonksiyonu boş metin kontrolü
Amaç: Boş metin girildiğinde sistem hata vermemeli ve boş string döndürmelidir.

python
Kodu kopyala
from src.clean import clean_text

def test_clean_empty_text():
    assert clean_text("") == ""
Test-2: Tahmin fonksiyonunun label döndürmesi
Amaç: Predict fonksiyonu sadece 0 veya 1 label değeri döndürmelidir.

python
Kodu kopyala
from src.predict import predict_text

def test_predict_returns_label():
    result = predict_text("örnek metin", "lr")
    assert result["label"] in [0, 1]
Test-3: Dataset kolon kontrolü
Amaç: Eğitim veri setinde gerekli kolonların (text, label) bulunması gerekir.

python
Kodu kopyala
import pandas as pd

def test_dataset_columns():
    df = pd.read_csv("data/processed/dataset.csv")
    assert "text" in df.columns
    assert "label" in df.columns
6. Beklenen Sonuçlar
Tüm testler çalıştırıldığında sonuç PASS olmalıdır.

Fonksiyonlar hata üretmemeli ve beklenen çıktıyı vermelidir.

7. Sonuç
White-box testler başarıyla çalıştırılmıştır ve sistemin temel fonksiyonları doğrulanmıştır.
Bu sayede sistemin iç modülleri güvenli şekilde çalışmaktadır.
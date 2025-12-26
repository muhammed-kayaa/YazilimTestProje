# STD Test Dokümanı

## Test Ortamı
- Python 3.8+
- Windows 10 / Linux
- GUI: `python gui.py`
- CLI: `python src/predict.py "Metin buraya" lr`

---

## Test Case Tablosu

| Test ID | Test Adı | Amaç | Girdi | Beklenen Sonuç | Gerçekleşen Sonuç |
|--------|----------|------|-------|----------------|------------------|
| TC-01 | Boş Metin Testi | Boş metinde uyarı vermeli | "" | "Metin boş olamaz" uyarısı | ✅ Başarılı |
| TC-02 | Kısa Metin Testi | Çok kısa metni reddetmeli | "Merhaba" | "Metin çok kısa" uyarısı | ✅ Başarılı |
| TC-03 | İnsan Metni Tahmini | İnsan metninde insan olasılığı yüksek olmalı | Human örnek metin | İnsan %50+ | ✅ Başarılı |
| TC-04 | AI Metni Tahmini | AI metninde AI olasılığı yüksek olmalı | AI örnek metin | AI %50+ | ✅ Başarılı |
| TC-05 | Model Yükleme | Model dosyaları düzgün yüklenmeli | Program açılışı | Modeller yüklenmeli | ✅ Başarılı |
| TC-06 | CLI Tahmin Testi | CLI çıktı dönmeli | `python src/predict.py "deneme metin" lr` | label + proba dönmeli | ✅ Başarılı |

---

## Sonuç
Tüm testler başarıyla gerçekleştirilmiştir. Sistem GUI ve CLI üzerinden doğru şekilde çalışmaktadır.

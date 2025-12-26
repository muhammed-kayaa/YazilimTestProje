# STD Test Dokümanı

## 1. Test Ortamı
- Python 3.8+
- Windows 10 / Linux
- GUI: `python gui.py`
- CLI: `python src/predict.py "Metin buraya" lr`
- Kullanılan Modeller: Logistic Regression (LR), Random Forest (RF), SVM

---

## 2. Test Türleri
- **Fonksiyonel Test:** Kullanıcı işlemleri ve çıktılar doğru mu?
- **UI Test:** Arayüz doğru görüntüleniyor mu?
- **Entegrasyon Testi:** Model dosyaları doğru yükleniyor mu?
- **CLI Test:** Komut satırında tahmin çalışıyor mu?

---

## 3. Test Case Tablosu

| Test ID | Test Adı | Amaç | Girdi | Beklenen Sonuç | Gerçekleşen Sonuç |
|--------|----------|------|-------|----------------|------------------|
| TC-01 | Boş Metin Testi | Boş metinde uyarı vermeli | "" | "Metin boş olamaz" uyarısı | ✅ Başarılı |
| TC-02 | Kısa Metin Testi | Çok kısa metni reddetmeli | "Merhaba" | "Metin çok kısa" uyarısı | ✅ Başarılı |
| TC-03 | İnsan Metni Tahmini | İnsan metninde insan olasılığı yüksek olmalı | "Bugün okuldan eve dönerken eski bir arkadaşımla karşılaştım..." | İnsan %50+ | ✅ Başarılı *(GUI çıktısı alındı)* |
| TC-04 | AI Metni Tahmini | AI metninde AI olasılığı yüksek olmalı | "Bu çalışmada modern yapay zeka sistemlerinin metin üretimindeki rolü incelenmiştir..." | AI %50+ | ✅ Başarılı *(GUI çıktısı alındı)* |
| TC-05 | Model Yükleme | Model dosyaları düzgün yüklenmeli | Program açılışı | Modeller yüklenmeli | ✅ Başarılı |
| TC-06 | CLI Tahmin Testi | CLI çıktı dönmeli | `python src/predict.py "deneme metin" lr` | label + proba dönmeli | ✅ Başarılı |

---

## 4. Test Sonuçları ve Kanıt
- GUI üzerinden yapılan tahmin işlemi başarıyla çalışmaktadır.
- CLI üzerinden tahmin işlemi doğru şekilde çıktı üretmektedir.
- Model yükleme sırasında hata oluşmamıştır.
- Tahmin sonuçlarının ekran görüntüsü UI/UX raporunda **Şekil-2** olarak sunulmuştur. (`4-UI_UX_Report.md`)

---

## 5. Sonuç
Tüm testler başarıyla gerçekleştirilmiştir. Sistem GUI ve CLI üzerinden doğru şekilde çalışmaktadır.

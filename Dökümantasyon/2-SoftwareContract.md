# Yazılım Şartnamesi / Proje Sözleşmesi

## 1. Proje Adı
AI vs İnsan Metin Dedektörü

## 2. Proje Ekibi
- (İsim Soyisim 1)
- (İsim Soyisim 2)
- (İsim Soyisim 3) (varsa)

## 3. Proje Tanımı
Bu proje, verilen Türkçe metnin insan tarafından mı yazıldığı yoksa yapay zeka tarafından mı üretildiğini tespit eden bir metin sınıflandırma sistemidir. Sistem üç farklı ML modeli (LR, RF, SVM) ile sonuç üretir ve kullanıcıya yüzdelik oranlarla sunar.

## 4. Proje Kapsamı
- Veri seti toplama ve düzenleme
- Veri temizleme ve ön işleme
- 3 farklı ML modeli ile eğitim ve değerlendirme
- GUI ve CLI üzerinden kullanım
- Test ve kalite raporu hazırlama

## 5. Teslimatlar
- Veri seti dosyaları (CSV)
- Eğitilmiş modeller (`lr.pkl`, `rf.pkl`, `svm.pkl`, `tfidf.pkl`)
- GUI uygulaması (`gui.py`)
- CLI tahmin scripti (`src/predict.py`)
- Dokümantasyonlar ve test raporları

## 6. Kabul Kriterleri
- Kullanıcı metin girdikten sonra AI/Human tahmini yapılmalıdır
- En az 3 modelin sonucu gösterilmelidir
- Yüzdelik oranlar kullanıcıya sunulmalıdır
- Model dosyaları eksiksiz yüklenmelidir
- Program GUI üzerinden çalışmalıdır

## 7. Ekler
- Veri seti lisans bilgileri
- Taskboard ekran görüntüleri
- Test dokümanları ve kalite raporu

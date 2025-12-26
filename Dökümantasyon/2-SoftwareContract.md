# Yazılım Şartnamesi / Proje Sözleşmesi

## 1. Proje Adı
AI vs İnsan Metin Dedektörü

## 2. Proje Ekibi
- 232803062 — Muhammed KAYA  
- 232803022 — Enes ANILIR  
- 232804016 — Uğur PAK  
- 222803055 — Yiğit Geldi  

## 3. Proje Tanımı
Bu proje, verilen Türkçe metnin insan tarafından mı yazıldığı yoksa yapay zeka tarafından mı üretildiğini tespit eden bir metin sınıflandırma sistemidir. Sistem üç farklı ML modeli (Logistic Regression, Random Forest, SVM) ile sonuç üretir ve kullanıcıya **yüzdelik oranlarla** sunar. Uygulama hem GUI hem CLI üzerinden çalıştırılabilir.

## 4. Proje Kapsamı
- Veri seti toplama ve düzenleme  
- Veri temizleme ve ön işleme (preprocessing)  
- 3 farklı ML modeli ile eğitim ve değerlendirme  
- GUI ve CLI üzerinden kullanım  
- Test dokümanları ve kalite raporu hazırlama  

## 5. Teslimatlar
- Veri seti dosyaları (CSV formatında)  
- Eğitilmiş modeller (`lr.pkl`, `rf.pkl`, `svm.pkl`, `tfidf.pkl`)  
- GUI uygulaması (`gui.py`)  
- CLI tahmin scripti (`src/predict.py`)  
- Dokümantasyon dosyaları ve test raporları  

## 6. Kabul Kriterleri
- Kullanıcı metin girdikten sonra AI/Human tahmini yapılmalıdır.  
- En az 3 modelin sonucu ayrı ayrı gösterilmelidir.  
- Tahminler yüzdelik oranlar ile sunulmalıdır.  
- Model dosyaları eksiksiz yüklenmelidir.  
- Program GUI üzerinden çalışmalıdır.  
- CLI üzerinden de tahmin alınabilmelidir.

## 7. Ekler
- Veri seti lisans bilgileri  
- Taskboard ekran görüntüleri  
- Test dokümanları ve kalite raporu  

---

## 8. Roller ve Sorumluluklar
| Üye | Sorumluluk |
|-----|------------|
| Muhammed KAYA | Dokümantasyon hazırlığı, GUI testi, entegrasyon |
| Enes ANILIR | Veri seti oluşturma ve temizleme |
| Uğur PAK | Model eğitim pipeline ve değerlendirme |
| Yiğit Geldi | CLI testleri, kalite raporu ve test senaryoları |

> Not: Roller proje sürecinde ekip içinde ortaklaşa yürütülmüş olabilir.

---

## 9. Zaman Planı (Sprint Planı)
- **Sprint 1:** Veri seti toplama ve düzenleme  
- **Sprint 2:** Veri temizleme ve preprocessing  
- **Sprint 3:** Model eğitimleri (LR, RF, SVM) + performans analizi  
- **Sprint 4:** GUI + CLI entegrasyonu, testler ve dokümantasyon  

---

## 10. Varsayımlar ve Kısıtlar
- Veri seti Türkçe metinlerden oluşmaktadır.  
- Veri kaynağı açık erişimli içeriklerden seçilmiştir.  
- Proje, Python 3.8+ ortamında çalışacak şekilde geliştirilmiştir.  
- Performans değerleri kullanılan veri setine bağlı olarak değişebilir.

---

## 11. Teslim Doğrulama (Acceptance Testing)
Teslim öncesinde aşağıdaki kontroller uygulanmıştır:
- STD test senaryoları uygulanmıştır (`5-STD_TestDocument.md`)  
- White-box testler uygulanmıştır (`6-WhiteBox_Tests.md`)  
- Kod kalitesi analizi yapılmıştır (`7-QualityReport.md`)

---

## 12. Versiyon Bilgisi
- Doküman Versiyonu: **v1.0**
- Tarih: **26.12.2025**
- Ders / Proje: **Yazılım Mühendisliği Proje Çalışması**

---

## 13. İmzalar
Bu sözleşme ve şartname dokümanı, proje ekibi tarafından hazırlanmış ve teslim edilmiştir.

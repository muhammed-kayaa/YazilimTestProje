# Yazılım Kalite Raporu

## 1. Amaç
Bu rapor, geliştirilen yazılımın kod kalitesini ölçmek, olası hataları belirlemek ve iyileştirme alanlarını tespit etmek amacıyla hazırlanmıştır.  
Kod analizi için statik analiz aracı kullanılarak kalite değerlendirmesi yapılmıştır.

---

## 2. Kullanılan Araçlar
- **Pylint** (Python statik analiz aracı)

> Not: Rubrikte SonarQube / SourceMonitor gibi araçlar önerilmiş olsa da proje Python tabanlı olduğu için statik analiz Pylint ile yapılmıştır.

---

## 3. Analiz Ortamı
- Python 3.8+
- Windows 10 / Linux
- Analiz edilen klasör: `src/`

---

## 4. Analizin Çalıştırılması
Proje dizininde aşağıdaki komut çalıştırılmıştır:

```bash
python -m pylint src


Çıktıyı dosyaya kaydetmek için:

python -m pylint src > pylint_report.txt


5. Analiz Sonuçları (Özet)

✅ Pylint Skoru: 1.47 / 10

Not: Pylint, Python kod standartlarını oldukça katı biçimde değerlendirdiği için docstring eksikliği, satır uzunluğu ve tekrar eden kod blokları gibi stil uyarılarından dolayı skor düşük çıkmıştır.
Bu skor kodun çalışmadığını değil, kod standartlarına göre iyileştirme yapılabileceğini göstermektedir.

6. Bulgular ve Yorum

Statik analiz sonucunda:

Kod modüler yapıda tasarlanmıştır (src/ klasörü içinde ayrılmıştır).

Veri temizleme, özellik çıkarımı ve tahmin işlemleri ayrı modüllere bölünmüştür.

Çoğu uyarı, sistemin çalışmasını engelleyen hata değil, formatlama ve standartlar ile ilgilidir (satır uzunluğu, isimlendirme, docstring vb).

Kodun okunabilirliğini artırmak için küçük düzenlemeler yapılabilir.

7. İyileştirme Önerileri

Fonksiyonlara docstring eklenmesi

Değişken adlarının daha açıklayıcı hale getirilmesi

Uzun satırların bölünmesi

Tekrarlı kod bloklarının azaltılması (duplicate-code uyarıları)

Gereksiz importların kaldırılması

8. Kanıt / Çıktı

Pylint analiz çıktısı kanıt olarak aşağıdaki dosya halinde sunulmuştur:

pylint_report.txt

9. Sonuç

Kod kalite analizi sonucunda proje, çalışır ve modüler bir yapıya sahiptir.
Pylint skorunun düşük çıkması, kodun çalışmadığını değil, standartlara göre iyileştirme yapılabileceğini göstermektedir.
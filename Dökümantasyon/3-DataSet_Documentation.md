# Veri Seti Dokümantasyonu

## Amaç
AI ve İnsan tarafından yazılmış Türkçe metinlerden oluşan bir veri seti hazırlanarak AI/Human sınıflandırma modeli eğitilmiştir.

## Veri Kaynakları

### İnsan Metinleri
- arxiv.org üzerinden alınan açık erişimli makale özetleri
- human_Created.csv (3000 satır)

### AI Metinleri
- ChatGPT / Gemini gibi LLM araçları kullanılarak prompt ile üretilmiştir
- ai_generated.csv (8277 satır)

## Lisans Bilgisi
Veri seti oluşturulurken aşağıdaki lisanslara uygun kaynaklar tercih edilmiştir:
- CC-BY / CC0 (açık erişimli içerikler)
- Akademik kullanım için uygun içerikler

## Veri Formatı
`dataset.csv` dosyası formatı:
- text: metin içeriği
- label: 0 (İnsan), 1 (AI)

## Temizleme İşlemleri
- Boş satırlar kaldırıldı
- Çok kısa metinler filtrelendi
- Noktalama ve gereksiz boşluklar normalize edildi
- UTF-8 encoding ile kayıt edildi

## Not
Rubrikte veri seti “kod” olarak istenmiş olsa da bu projede “metin” sınıflandırma yapıldığı için veri seti Türkçe metinlerden oluşturulmuştur.

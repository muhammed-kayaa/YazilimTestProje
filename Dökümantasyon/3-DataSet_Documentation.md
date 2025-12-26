# Veri Seti Dokümantasyonu

## 1. Amaç
AI ve İnsan tarafından yazılmış Türkçe metinlerden oluşan bir veri seti hazırlanarak AI/Human sınıflandırma modeli eğitilmiştir. Amaç, kullanıcıdan alınan bir metnin **insan mı yoksa AI üretimi mi olduğunu** tahmin edebilmektir.

---

## 2. Veri Kaynakları

### 2.1 İnsan Metinleri (Human)
- Kaynak: **arxiv.org** üzerinden alınan açık erişimli makale özetleri  
- Kullanım: akademik içerikler (abstract)  
- Dosya: `human_Created.csv` (**3000 satır**)  

Örnek arxiv arama linki:  
https://arxiv.org/search/?query=abstract&searchtype=all&source=header

---

### 2.2 AI Metinleri (AI Generated)
- Kaynak: **ChatGPT / Gemini** gibi LLM araçları
- Yöntem: farklı konularda prompt girilerek Türkçe metin üretilmiştir.
- Dosya: `ai_generated.csv` (**8277 satır**)  

#### Kullanılan örnek promptlar
1. "Türkçe olarak 150 kelimelik bilimsel bir paragraf yaz."
2. "Türkçe olarak ekonomi hakkında kısa bir makale özeti üret."

---

## 3. Veri Seti Boyutu ve Dağılımı
Proje eğitiminde kullanılan işlenmiş veri seti:

- `dataset.csv` toplam: **3616 örnek**
- Etiket dağılımı:
  - Human (label=0): **3000**
  - AI (label=1): **616**

> Not: Veri seti arxiv insan metinleri ağırlıklı olacak şekilde oluşturulmuştur. AI verileri ise LLM ile üretilmiş metinlerden seçilmiştir.

---

## 4. Veri Formatı
İşlenmiş veri seti `dataset.csv` formatı:

| Kolon | Açıklama |
|------|----------|
| text | Metin içeriği |
| label | 0=İnsan, 1=AI |

---

## 5. Lisans Bilgisi
Veri seti oluşturulurken aşağıdaki lisanslara uygun kaynaklar tercih edilmiştir:
- **CC-BY / CC0** (açık erişimli içerikler)
- Akademik kullanım için uygun içerikler  
- Arxiv açık erişim içeriklerinden yalnızca **özet** bölümleri kullanılmıştır.

---

## 6. Temizleme ve Ön İşleme (Preprocessing)
Veriler model eğitiminden önce aşağıdaki işlemlerle temizlenmiştir:

- Boş satırlar kaldırıldı  
- Çok kısa metinler filtrelendi (minimum kelime sınırı)  
- Noktalama işaretleri normalize edildi  
- Gereksiz boşluklar temizlendi  
- UTF-8 encoding ile kayıt edildi  
- Metinler model eğitimine uygun hale getirildi (TF-IDF için)

---

## 7. Veri Örnekleri

### Human örnek (label=0)
> "Bu çalışmada, sinir ağlarının optimizasyon yöntemleri incelenmiştir..."

### AI örnek (label=1)
> "Bu araştırmada modern yapay zeka modellerinin metin üretme kapasitesi ele alınmaktadır..."

---

## 8. Rubrik Uyarlama Notu
Rubrikte veri seti “kod” olarak istenmiş olsa da bu projede **metin sınıflandırma** yapıldığı için veri seti Türkçe metinlerden oluşturulmuştur. Veri boyutu rubrikte istenen minimum örnek sayılarını karşılayacak şekilde hazırlanmıştır.

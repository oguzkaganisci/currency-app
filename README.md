# Döviz Baba Pro 💱

Gelişmiş, modern ve gerçek zamanlı bir finans/döviz takip paneli. Python (Flask) arka planı ve tamamı özel yazılmış şık bir "Glassmorphism" (Cam Efekti) önyüzü (HTML/CSS/JS) ile geliştirilmiştir.

## 🚀 Özellikler (Features)

- **Gerçek Zamanlı Veri:** Frankfurter API üzerinden anlık döviz kurları.
- **Tarihsel Grafikler:** 7 Gün, 30 Gün, 3 Ay ve 1 Yıllık detaylı çizgi grafikler (Chart.js arayüzü ile).
- **Hızlı Çevirici:** Seçilen kura özel anında TRY (₺) hesaplaması yapan Converter Widget.
- **Karanlık/Aydınlık (Dark/Light) Mod:** Ekranın üstünden tek tıkla değişen ve `localStorage` ile tarayıcıya kaydedilen premium tasarımlar.
- **Akıllı Sıralama ve Arama:** En Çok Yükselenler, Alfabetik veya canlı arama filtreleriyle yüzlerce kur arasında anında sonuç.
- **Favoriler Panosu:** İstenilen kurun yanındaki `⭐` ikonuna tıklayarak favoriye alma ve listeyi özelleştirme.

## 🛠️ Kurulum (Installation)

1. Depoyu bilgisayarınıza indirin (Clone):
   ```bash
   git clone https://github.com/KULLANICI_ADINIZ/doviz-baba-pro.git
   ```
2. Proje dizinine girin:
   ```bash
   cd doviz-baba-pro
   ```
3. Gerekli Python kütüphanelerini kurun:
   ```bash
   pip install flask requests
   ```
4. Uygulamayı çalıştırın:
   ```bash
   python currencies.py
   ```
5. Tarayıcınızda `http://127.0.0.1:5000` adresine gidin.

## 🎨 Teknolojiler (Tech Stack)
- **Backend:** Python, Flask, Requests
- **Frontend:** Vanilla JS, HTML5, CSS3 (CSS Variables, Flexbox/Grid)
- **Grafikler:** Chart.js
- **Veri Kaynağı:** Frankfurter API

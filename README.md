# 🕵️‍♂️ Steganografi Uygulaması

Bu proje, **Python kullanılarak geliştirilen GUI (arayüzlü) bir steganografi uygulamasıdır**. Uygulama sayesinde kullanıcılar bir metni bir görselin içine gizleyebilir veya gizli veriyi geri okuyabilir.

## 🧠 Ne Yapıyor?

- `veri_yazma_arayüzlü.py`: Kullanıcının girdiği metni seçilen bir görsele gizler.
- `veri_okuma_arayüzlü.py`: Önceden gizlenmiş veriyi bir görselden okur ve kullanıcıya gösterir.

Her iki uygulama da kullanıcı dostu bir arayüze sahiptir.

## 🖼️ Kullanım Arayüzleri

### 🔐 Veri Yazma Ekranı:
Kullanıcıdan gizlenecek metni alır ve seçilen görsel dosyası içine bu metni yazar.

### 🔍 Veri Okuma Ekranı:
Kullanıcıdan içinde veri olan bir görsel alır ve içindeki metni çözümler.

## 💾 Gereksinimler

- Python 3.x
- Tkinter (standart olarak gelir)
- PIL (Pillow)

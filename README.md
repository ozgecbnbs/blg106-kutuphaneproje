# Bibliyofil - Dijital Okuma Günlüğü ve Kütüphane Sistemi 📚

Bu proje, kitapseverlerin okudukları kitapları dijital bir ortamda düzenli bir şekilde arşivlemelerine, kişisel okuma günlüklerini tutmalarına ve kitaplar hakkında detaylı incelemeler yazıp puanlama yapmalarına olanak tanıyan web tabanlı bir kütüphane ve inceleme yönetim sistemidir.

## ✨ Öne Çıkan Özellikler

* **Kullanıcı Kimliklendirme (Auth):** Güvenli kullanıcı kaydı, giriş ve çıkış işlemleri. Her kullanıcının kendi izole çalışma alanına sahip olması.
* **Kişisel Kütüphane (CRUD):** Kullanıcıların kendi okudukları kitapları sisteme ekleyebilmesi, listeleyebilmesi ve silebilmesi.
* **Gelişmiş İnceleme & Puanlama:** Kitap detay sayfalarında kullanıcılara özel 1-5 arası yıldızlı (★) puanlama yapabilme ve metin tabanlı eleştiri yazabilme imkanı.
* **Ortak Yorum Havuzu (Sosyal Etkileşim):** SQLAlchemy `JOIN` mantığı ile, farklı kullanıcıların aynı kitaba (aynı başlık ve yazar) yaptıkları yorumların ortak bir detay sayfasında birleştirilmesi.
* **Dinamik Kullanıcı Profili (Dashboard):** Kullanıcıların baş harfinden otomatik olarak oluşturulan CSS tabanlı harf avatarları. Toplam okunan kitap ve yapılan yorum istatistikleri ile geçmiş etkileşimlerin kronolojik listesi.

## 🛠 Kullanılan Teknolojiler

* **Backend:** Python / Flask (Blueprint & Factory Pattern Yapısı)
* **Veritabanı & ORM:** SQLite / SQLAlchemy 2.x
* **Veritabanı Migrasyonu:** Flask-Migrate (Alembic)
* **Form & Validasyon:** Flask-WTF / WTForms
* **Şifre Güvenliği:** Werkzeug Security
* **Frontend / UI:** HTML5, CSS3, Jinja2 Şablon Motoru, Bootstrap 5
pip install -r requirements.txt
## 🚀 Kurulum Adımları

**1. Projeyi İndirin:**
```bash
git clone <https://github.com/ozgecbnbs/blg106-kutuphaneproje.git>
cd digital_library
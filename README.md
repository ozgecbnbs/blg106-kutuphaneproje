# Bibliyofil ve Okuma Günlüğü

Bu proje, kitapseverlerin okudukları kitapları dijital bir ortamda düzenli bir şekilde arşivlemelerine, kişisel okuma günlüklerini tutmalarına ve kitaplar hakkında detaylı incelemeler yazıp puanlama yapmalarına olanak tanıyan web tabanlı bir kütüphane ve inceleme yönetim sistemidir. 

## Kullanılan Teknolojiler
* **Backend:** Python / Flask (Factory Pattern Yapısı)
* **Veritabanı & ORM:** SQLite / SQLAlchemy 2.x
* **Veritabanı Migrasyonu:** Flask-Migrate (Alembic)
* **Form & Validasyon:** Flask-WTF / WTForms
* **Şifre Güvenliği:** Werkzeug Security

## Kurulum Adımları

1. **Projeyi İndirin:**
   `git clone <github-depo-linkiniz>`
   `cd digital_library`

2. **Sanal Ortamı Aktif Edin:**
   `Set-ExecutionPolicy Unrestricted -Scope Process`
   `.\venv\Scripts\activate`

3. **Gerekli Paketleri Yükleyin:**
   `pip install -r requirements.txt`

4. **Çevre Değişkenlerini (.env) Yapılandırın:**
   Proje kök dizininde bir `.env` dosyası oluşturun ve şunları ekleyin:
   `FLASK_APP=run.py`
   `FLASK_DEBUG=1`
   `SECRET_KEY=gizli-anahtariniz-buraya`

5. **Veritabanını Başlatın:**
   `flask db init`
   `flask db migrate -m "Modeller olusturuldu"`
   `flask db upgrade`

## Geliştirme Komutları
* **Uygulamayı Başlatma:** `flask run`
* **Yeni Değişiklikleri Algılama:** `flask db migrate -m "mesaj"`
* **Veritabanını Güncelleme:** `flask db upgrade`
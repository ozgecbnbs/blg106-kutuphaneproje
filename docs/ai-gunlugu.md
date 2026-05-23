## Oturum 1 - 21 Mayıs 2026
### Hedef
Bu oturumda, Dijital Kütüphane uygulaması için Flask 3.x altyapısını ve klasör iskeletini kurmayı hedefledim. Ayrıca sanal ortamı ayarlayıp versiyon kontrol (Git) altyapısını oluşturmak önceliğimdi.

### Kullandığım Mod ve Model
Editör: Antigravity
Mod: Plan 
Model: Gemini 3 Pro 
Görünüm: Manager 

### Verdiğim Promptlar
1. "Meslek Yüksek Okulu öğrencisiyim, İnternet Programcılığı dersi için Flask 3.x ile bir web uygulaması geliştireceğim. Konum: Dijital Kütüphane ve Okuma Günlüğü. Hedef: Application factory pattern kullanan, blueprint'lere ayrılmış, temiz bir proje iskeleti kur..." 
### Ajanın Önerdiği Plan
Ajan, app/main ve app/auth blueprint'lerini ve boş __init__.py dosyalarını içeren temiz bir proje klasörü planı sundu. 
(Ekran görüntüsü: docs/img/oturum-1-plan.png) 
### Plan'da Sorguladıklarım
Plan, "Küçük adımlarla ilerleyin" yaklaşımına uygundu. Gereksiz hiçbir dosya eklenmemişti, bu yüzden planı doğrudan onayladım
### Üretilen Kodda Düzelttiklerim
- Sadece iskelet kurulduğu için koda müdahale etmedim. Fakat yönerge gereği gizliliği sağlamak adına .env.example dosyasından yararlanarak kendi .env dosyamı manuel olarak oluşturdum ve şifremi korumaya aldım.

### Karşılaştığım Hatalar ve Çözümler
- Hata: Sanal ortamı aktif ederken PowerShell kaynaklı `PSSecurityException` hatası aldım. 
- Çözüm: `Set-ExecutionPolicy Unrestricted -Scope Process` komutuyla PowerShell'e yetki vererek çözdüm.
- Hata: Git commit atarken `fatal: not a git repository` ve `Author identity unknown` hataları aldım.
- Çözüm: Önce `git init` ile klasörü projeye dönüştürdüm, sonra `git config` ile kullanıcı bilgilerimi tanıtarak ilk commit'imi başarıyla attım.

### Bu Oturumdan Öğrendiğim
Ajana projeyi hemen hazırlatmak yerine sadece klasör yapısını ve temel şeyleri oluşturmasını söyledim[cite: 311]. Böylece ajana her şeyi tek seferde yaptırmak yerine önce projenin temelinin oluşmasını sağladım. Geliştirme ortamının ve terminalin (Git, sanal ortam) nasıl yapılandırılacağını uygulamalı olarak tecrübe ettim.

### Sonraki Oturum İçin Notlar
Bir sonraki adımda SQLAlchemy 2.x stili ile veritabanı modellerini oluşturacağım.

## Oturum 2 - 22 Mayıs 2026

### Hedef
Bu oturumda, uygulamanın temelini oluşturan veritabanı şemasını tasarlamayı ve SQLAlchemy 2.x standartlarına uygun `User`, `Kitap` ve `Inceleme` modellerini oluşturmayı hedefledim.

### Kullandığım Mod ve Model
Editör: Antigravity
Mod: Plan
Model: Gemini 3 Pro
Görünüm: Manager

### Verdiğim Promptlar
1. "Mevcut projemde app/__init__.py içinde db tanımlı... app/models.py içinde şu modelleri tanımla: User, Kitap, Inceleme... Kısıtlar: Yönerge gereği kesinlikle SQLAlchemy 2.x stilini kullan (Mapped, mapped_column)..."

### Ajanın Önerdiği Plan
Ajan; User, Kitap ve Inceleme modelleri için primary key, unique alanlar ve otomatik tarih atamalarını içeren eksiksiz bir şema sundu. Ayrıca modeller arasındaki bire-çok (one-to-many) ilişkileri `relationship` ve `back_populates` kullanarak kurguladı. Kodlama öncesinde kısıtlamaların (puan sınırları vb.) veritabanı seviyesinde mi yoksa form validasyonu aşamasında mı çözülmesi gerektiğini sordu.

### Plan'da Sorguladıklarım
Ajanın kısıtlamalar konusundaki sorusunu değerlendirdim. Hataları daha esnek yakalamak ve kullanıcıya daha temiz hata mesajları gösterebilmek adına kısıtlamaları veritabanı seviyesinde (CheckConstraint) tutmak yerine form doğrulaması (validasyon) aşamasında çözmenin daha kolay ve uygun olacağına karar verdim ve ajana bu yönde onay verdim.

### Üretilen Kodda Düzelttiklerim
- Kod editörünün hata denetleyicisi sanal ortamı tam olarak algılayamadığı için SQLAlchemy satırlarının altını kırmızı çizdi. Bu görsel uyarıyı susturmak ve kodun okunabilirliğini artırmak için ilgili satırların sonuna manuel olarak `# pyrefly: ignore [missing-import]` yorum satırlarını ekledim.

### Karşılaştığım Hatalar ve Çözümler
- Hata: Yeni terminal oturumu açıldığında sanal ortamın (`venv`) kapalı olduğunu ve aktifleştirmeye çalışırken tekrar `PSSecurityException` güvenlik engeline takıldığımı gördüm.
- Çözüm: `Set-ExecutionPolicy Unrestricted -Scope Process` komutuyla PowerShell'e yeniden geçici yetki vererek sanal ortamı (`.\venv\Scripts\activate`) başarıyla ayağa kaldırdım.

### Bu Oturumdan Öğrendiğim
SQLAlchemy 2.x sürümünün getirdiği modern deklaratif yapıyı (`Mapped` ve `mapped_column`) uygulamalı olarak öğrendim. Veritabanı modelleri arasında ilişkilerin mimari olarak nasıl kurulduğunu ve şifre güvenliği için `werkzeug.security` paketinin (`set_password`, `check_password`) nasıl entegre edildiğini kavradım.

### Sonraki Oturum İçin Notlar
Modellerimiz hazır. Bir sonraki oturumda Flask-Migrate kullanarak veritabanı migrasyon süreçlerini (flask db init, migrate, upgrade) başlatacağız ve tablolarımızı fiziksel olarak oluşturacağız.

## Oturum 3 - 23 Mayıs 2026

### Hedef
SQLAlchemy ile yazdığımız veritabanı modellerini Flask-Migrate eklentisi kullanarak fiziksel bir SQLite veritabanına (`app.db`) dönüştürmek ve tabloları oluşturmak.

### Kullandığım Mod ve Model
Editör: Antigravity
Mod: Plan
Model: Gemini 3 Pro
Görünüm: Manager

### Verdiğim Promptlar
1. "Mevcut bir önceki oturumda SQLAlchemy 2.x ile veritabanı modellerimizi oluşturduk... Hedef: Veritabanı tablolarını fiziksel olarak oluşturmak için Flask-Migrate kurulumunu yap... Kurallar: flask db init, flask db migrate, flask db upgrade komutlarını çalıştır..."

### Ajanın Önerdiği Plan ve Tespitler
Ajan, projenin ilk oturumunda zaten "factory pattern" mimarisine uygun olarak `migrate.init_app(app, db)` kurulumunun yapılmış olduğunu tespit etti. Bu nedenle kod yapısını bozmadan doğrudan terminal komutlarına geçmeyi önerdi.

### Plan'da Sorguladıklarım / Ajanın Müdahalesi
Süreç esnasında ajan çok kritik bir teknik detayı fark etti: Modellerimiz `app/models.py` içinde tanımlı olmasına rağmen, uygulamanın ana giriş kapısı olan `app/__init__.py` içinde import edilmemişti. Bu durum Flask-Migrate'in tabloları "görmesini" engelliyordu. Ajan bu eksikliği fark ederek dosyanın altına `from app import models` satırını akıllıca ekledi.

### Karşılaştığım Hatalar ve Çözümler
- Herhangi bir hata ile karşılaşılmadı. Ajan, eksik olan import satırını kendisi tamamlayarak olası bir "boş veritabanı şeması" hatasının önüne geçmiş oldu. Terminalde sırasıyla `flask db init`, `flask db migrate` ve `flask db upgrade` komutları sorunsuz icra edildi.

### Bu Oturumdan Öğrendiğim
Flask-Migrate mimarisinin, SQLAlchemy'nin `metadata` yapısını takip ederek çalıştığını ve bu yüzden modellerin uygulamaya import edilmesinin zorunlu olduğunu öğrendim. Ayrıca `__pycache__` klasörünün Python tarafından kodları hızlandırmak amacıyla oluşturulan ve bytecode içeren zararsız bir sistem klasörü olduğunu kavradım.

### Sonraki Oturum İçin Notlar
Veritabanımız ve tablolarımız fiziksel olarak hazır. Bir sonraki oturumda kullanıcı kayıt (Register) ve giriş (Login) işlemlerini yönetecek olan WTForms yapılarını ve form validasyonlarını kuracağız.
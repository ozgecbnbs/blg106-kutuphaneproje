## Oturum 1 - 21 Mayıs 2026
### Hedef
Bu oturumda, Dijital Kütüphane uygulaması için Flask 3.x altyapısını ve klasör iskeletini kurmayı hedefledim. Ayrıca sanal ortamı ayarlayıp versiyon kontrol (Git) altyapısını oluşturmak önceliğimdi.

### Kullandığım Mod ve Model
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
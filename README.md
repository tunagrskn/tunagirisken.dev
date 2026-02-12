# tunagirisken.com - Site Yonetim Rehberi

## Gereksinimler

- Hugo (v0.152+)
- zip komutu (Linux/Mac'te varsayilan)

---

## Yerel Gelistirme

### Siteyi lokalde calistirma (canli onizleme)

```bash
cd /space/neptun/tgirisken.github/tunagirisken.dev
hugo server -D
```

Tarayicida `http://localhost:1313` adresine git. Dosya degisikliklerinde otomatik yenilenir.

### Siteyi production icin build etme

```bash
hugo --minify
```

Build ciktisi `public/` klasorune olusturulur.

---

## cPanel'e Deploy (Yayina Alma)

### 1. Build + ZIP olusturma

```bash
cd /space/neptun/tgirisken.github/tunagirisken.dev
hugo --minify
cd public && rm -f ../site.zip && zip -r ../site.zip . && cd ..
```

`site.zip` dosyasi proje ana dizininde olusur (~12 MB).

### 2. cPanel'e yukleme

1. cPanel'e giris yap: `https://tunagirisken.com:2083`
2. **Dosya Yoneticisi** (File Manager) ac
3. `public_html` klasorune git
4. **Yukle** (Upload) tikla → `site.zip` dosyasini sec ve yukle
5. Yuklenen `site.zip`'e sag tikla → **Extract** (Cikar)
6. Cikartma yolunun `/public_html` oldugunu dogrula → **Extract Files**
7. `site.zip` dosyasini sil (sag tikla → Sil)

### 3. Tek satirda build + zip

```bash
cd /space/neptun/tgirisken.github/tunagirisken.dev && hugo --minify && cd public && rm -f ../site.zip && zip -r ../site.zip . && echo "ZIP HAZIR" && ls -lh ../site.zip
```

---

## Bakim Modu

cPanel → Dosya Yoneticisi → `public_html/.htaccess` dosyasini duzenle.

### Bakima almak

Asagidaki 3 satirin basindaki `#` isaretlerini kaldir:

```apache
RewriteCond %{REMOTE_ADDR} !^78\.189\.95\.168$
RewriteCond %{REQUEST_URI} !^/maintenance\.html$
RewriteRule ^(.*)$ /maintenance.html [R=503,L]
```

### Bakimdan cikarmak

Ayni 3 satirin basina `#` ekle:

```apache
#RewriteCond %{REMOTE_ADDR} !^78\.189\.95\.168$
#RewriteCond %{REQUEST_URI} !^/maintenance\.html$
#RewriteRule ^(.*)$ /maintenance.html [R=503,L]
```

**Not:** `78.189.95.168` senin IP adresin. Bakim modunda sen siteyi normal gorursun, baskalari bakim sayfasini gorur. IP degisirse `.htaccess`'teki IP'yi guncelle.

---

## SSL Sertifikasi

cPanel → **SSL/TLS Status** → **Run AutoSSL**

Sertifika otomatik yenilenir, bir sey yapman gerekmez.

---

## Google Search Console

- Adres: https://search.google.com/search-console
- Sitemap: `https://tunagirisken.com/sitemap.xml` (zaten gonderildi)
- DNS dogrulama TXT kaydi cPanel Zone Editor'da ekli

Yeni yazi eklediginde Search Console'da **URL Denetimi** (URL Inspection) ile dizine ekleme isteyebilirsin.

---

## Onemli Dosya Konumlari

| Dosya/Klasor | Aciklama |
|---|---|
| `config/_default/config.toml` | Site ayarlari (baseURL, dil, tema) |
| `config/_default/params.toml` | Tema parametreleri (layout, footer) |
| `config/_default/languages.tr.toml` | Turkce dil ayarlari, yazar bilgisi |
| `content/posts/` | Blog yazilari |
| `content/about/index.md` | Hakkimda sayfasi |
| `static/` | Statik dosyalar (favicon, .htaccess, maintenance.html) |
| `static/.htaccess` | Apache yonlendirme kurallari |
| `static/maintenance.html` | Bakim sayfasi |
| `assets/css/custom.css` | Ozel CSS animasyonlari |
| `layouts/partials/extend-head.html` | Head'e eklenen ozel HTML/CSS |
| `layouts/partials/extend-footer.html` | Footer'a eklenen ozel JS |
| `layouts/partials/favicons.html` | Favicon tanimlari |
| `public/` | Build ciktisi (bunu deploy ediyoruz) |

---

## Yeni Yazi Ekleme

```bash
hugo new posts/yazi-adi/index.md
```

Olusturulan dosyayi duzenle, gorselleri ayni klasore koy.

---

## Favicon Degistirme

1. Yeni SVG ikonu `static/favicon.svg` olarak kaydet
2. PNG'leri olustur:

```bash
cd static
convert -background none -density 300 favicon.svg -resize 16x16 favicon-16x16.png
convert -background none -density 300 favicon.svg -resize 32x32 favicon-32x32.png
convert -background none -density 300 favicon.svg -resize 180x180 apple-touch-icon.png
convert -background none -density 300 favicon.svg -resize 192x192 android-chrome-192x192.png
convert -background none -density 300 favicon.svg -resize 512x512 android-chrome-512x512.png
convert favicon-16x16.png favicon-32x32.png favicon.ico
```

3. Build + ZIP + cPanel'e yukle

---

## Hizli Referans

```bash
# Lokalde calistir
hugo server -D

# Build et
hugo --minify

# Build + ZIP
hugo --minify && cd public && rm -f ../site.zip && zip -r ../site.zip . && cd ..

# DNS kontrol
dig TXT tunagirisken.com +short
```
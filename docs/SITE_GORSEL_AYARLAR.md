# 🎨 Site Görünüm Ayarları

## CSS Bilmeden Site Görünümünü Değiştirme

Bu dosyayı düzenleyerek sitenizin görünümünü kolayca özelleştirebilirsiniz.

---

## 🎨 Renk Teması Değiştirme

**Konum:** `config/_default/params.toml`

```toml
colorScheme = "slate"    # Değiştirebilirsiniz
```

### Mevcut Temalar:

- `slate` - Gri-mavi tonlar (profesyonel, minimal)
- `fire` - Sıcak renkler (turuncu, kırmızı)
- `ocean` - Okyanus mavisi (sakin, modern)
- `forest` - Yeşil tonlar (doğal, rahatlatıcı)
- `avocado` - Açık yeşil (canlı, fresh)
- `congo` - Tropikal renkler (renkli, dinamik)

**Örnek:**
```toml
colorScheme = "slate"  # ← Buraya "ocean" veya "forest" yazabilirsiniz
```

---

## 🌓 Karanlık/Aydınlık Mod

**Konum:** `config/_default/params.toml`

```toml
defaultAppearance = "dark"      # "light" veya "dark"
autoSwitchAppearance = true     # Otomatik geçiş (true/false)
```

**Seçenekler:**
- `dark` - Karanlık tema (varsayılan)
- `light` - Aydınlık tema
- `autoSwitchAppearance = true` - Kullanıcı sistem tercihine göre

---

## 🏠 Ana Sayfa Layout

**Konum:** `config/_default/params.toml`

```toml
[homepage]
  layout = "profile"    # Değiştirebilirsiniz
```

### Layout Türleri:

1. **profile** - Profil odaklı (önerilen)
   - Ortalanmış profil fotoğrafı
   - Bio ve sosyal linkler
   - Minimal ve temiz

2. **page** - Sayfa odaklı
   - Tam genişlik içerik
   - Daha fazla text alanı

3. **background** - Arka plan odaklı
   - Büyük hero image
   - Dramatik görünüm

4. **card** - Kart layout
   - Grid sistemli kartlar
   - Modern ve dinamik

**Öneri:** `profile` en minimal ve profesyonel görünümü verir.

---

## 🎯 Animasyon Seviyesi

CSS'de animasyon yoğunluğu ayarlanmış durumda:

### Şu Anki Ayarlar (Minimal):
- ✅ Çok hafif arka plan animasyonu (30 saniye)
- ✅ Yumuşak hover efektleri (3px kalkma)
- ✅ Minimal kart gölgeleri
- ❌ Particle efektler kapalı
- ❌ Typing animasyonu kapalı
- ❌ 3D hover efektler kapalı

### Daha da Minimal İçin:

Animasyonları tamamen kapatmak isterseniz:

**Konum:** `assets/css/custom.css`

Dosyanın en üstüne ekleyin:

```css
/* Tüm animasyonları kapat */
* {
  animation: none !important;
  transition: none !important;
}
```

---

## 🖼️ Ana Sayfa Görselleri

**Konum:** `static/img/`

### Gerekli Görseller:

1. **avatar.jpg** - Profil fotoğrafı
   - Boyut: 400x400px (kare)
   - Format: JPG veya PNG

2. **home.jpg** - Arka plan görseli (opsiyonel)
   - Boyut: 1920x1080px
   - Format: JPG

**Görselleri Değiştirme:**

```bash
# Profil fotoğrafını kopyala
cp yeni-fotograf.jpg static/img/avatar.jpg

# Arka plan görselini kopyala  
cp yeni-arkaplan.jpg static/img/home.jpg
```

---

## 📝 Font ve Metin Boyutu

**Konum:** `config/_default/params.toml`

Blowfish teması otomatik font yönetimi yapar, ama kendi CSS'inizi eklemek isterseniz:

**Yeni dosya:** `assets/css/custom-fonts.css`

```css
/* Daha büyük metin */
body {
  font-size: 18px;
}

/* Daha küçük metin */
body {
  font-size: 14px;
}

/* Farklı font ailesi */
body {
  font-family: 'Georgia', serif;
}
```

---

## 🎨 Kendi Renklerinizi Kullanma

**Konum:** `assets/css/custom.css`

Dosyanın başındaki `:root` bölümünü değiştirin:

```css
:root {
  --gradient-1: #667eea;  /* ← Buraya kendi renginiz */
  --gradient-2: #764ba2;  /* ← Buraya kendi renginiz */
  --gradient-3: #f093fb;  /* ← Buraya kendi renginiz */
  --gradient-4: #4facfe;  /* ← Buraya kendi renginiz */
}
```

### Renk Önerileri:

**Profesyonel Mavi:**
```css
--gradient-1: #2563eb;
--gradient-2: #1e40af;
```

**Sakin Yeşil:**
```css
--gradient-1: #059669;
--gradient-2: #047857;
```

**Sıcak Turuncu:**
```css
--gradient-1: #f59e0b;
--gradient-2: #d97706;
```

---

## 📊 Kart Stil Değiştirme

**Konum:** `config/_default/params.toml`

```toml
[list]
  cardView = true          # Kart görünümü (true/false)
  groupByYear = true       # Yıla göre grupla (true/false)
  showSummary = true       # Özet göster (true/false)
```

**Seçenekler:**
- `cardView = true` - Modern kart layout (önerilen)
- `cardView = false` - Liste görünümü (klasik)

---

## 🎯 Hızlı Görünüm Değişiklikleri

### 1. Çok Minimal İstiryorum

```toml
# config/_default/params.toml
colorScheme = "slate"
defaultAppearance = "light"

[homepage]
  layout = "profile"
  cardView = false
```

### 2. Modern ve Renkli İstiyorum

```toml
colorScheme = "fire"
defaultAppearance = "dark"

[homepage]
  layout = "card"
  cardView = true
```

### 3. Klasik Blog Görünümü

```toml
colorScheme = "slate"
defaultAppearance = "light"

[homepage]
  layout = "page"
  cardView = false
  groupByYear = true
```

---

## 🔧 Değişiklikleri Test Etme

Değişiklik yaptıktan sonra:

```bash
# Sunucuyu yeniden başlat
hugo server -D

# Tarayıcıda aç
http://localhost:1313
```

Değişiklikleri göremiyorsanız:
1. Tarayıcı cache'ini temizleyin (Ctrl+Shift+R)
2. Hugo sunucusunu durdurup yeniden başlatın

---

## 💡 İpuçları

### ✅ Yapılması Gerekenler:
- Tek seferde bir şey değiştirin
- Her değişikliği test edin
- Yedek alın (git commit)

### ❌ Yapılmaması Gerekenler:
- CSS dosyalarını karıştırmayın (gerekmedikçe)
- Aynı anda çok fazla değişiklik yapmayın
- Theme dosyalarını direkt düzenlemeyin

---

## 🆘 Sorun mu Yaşıyorsunuz?

### Site Bozuk Görünüyorsa:

1. **Son değişikliği geri alın:**
   ```bash
   git checkout -- config/_default/params.toml
   ```

2. **CSS'i varsayılana döndürün:**
   ```bash
   git checkout -- assets/css/custom.css
   ```

3. **Cache temizleyin:**
   - Tarayıcıda: Ctrl+Shift+Delete
   - Hugo: `hugo --gc`

---

## 📞 Daha Fazla Yardım

- **Blowfish Docs:** https://blowfish.page/docs/
- **Hugo Docs:** https://gohugo.io/documentation/
- **Renk Paletleri:** https://coolors.co/

---

**Kolay gelsin! 🚀**

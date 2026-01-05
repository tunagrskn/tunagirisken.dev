# Tuna Girişken - Kişisel Blog 🚀

> Embedded Systems, Linux, Yocto ve Otomotiv teknolojileri üzerine Türkçe/İngilizce blog
> **Modern animasyonlar ve etkileyici görsel efektlerle! ✨**

## ✨ Özellikler

- 🎨 **Modern Animasyonlar** - Gradient backgrounds, particle effects, 3D hover
- 🌍 **Otomatik Çeviri** - Türkçe → İngilizce (DeepL/OpenAI/Google)
- 🚀 **Performanslı** - 39ms build time, GPU-accelerated animations
- 📱 **Responsive** - Tüm cihazlarda mükemmel görünüm
- ♿ **Accessible** - WCAG uyumlu, reduced-motion desteği
- 🎯 **SEO-Friendly** - Multilingual, optimized meta tags

## 🚀 Hızlı Başlangıç

### Gereksinimler

- Hugo Extended >= 0.120.0
- Python 3.11+ (otomatik çeviri için)
- Git

### Kurulum

```bash
# Repoyu klonla
git clone https://github.com/tunagrskn/tg-blog.git
cd tg-blog

# Blowfish temasını yükle (eğer yoksa)
git submodule update --init --recursive

# Geliştirme sunucusunu başlat
hugo server -D
```

Site http://localhost:1313 adresinde çalışacaktır.

## 📝 İçerik Oluşturma

### Türkçe İçerik (Ana Dil)

Türkçe içerikler `content/tr/` dizinine eklenir:

```bash
# Yeni blog yazısı
hugo new content/tr/posts/yeni-yazi.md

# Yeni sayfa
hugo new content/tr/hakkimda.md
```

### Otomatik İngilizce Çeviri

Blog, Türkçe içerikleri otomatik olarak İngilizceye çevirebilir. 3 farklı yöntem:

#### 1. GitHub Actions (Önerilen)

Her push işleminde otomatik çeviri yapar:

1. GitHub repository Settings > Secrets > Actions'a git
2. Aşağıdaki secretlardan birini ekle:
   - `DEEPL_API_KEY` (en kaliteli)
   - `OPENAI_API_KEY` (GPT-4 ile)
   - `GOOGLE_TRANSLATE_API_KEY`

3. `content/tr/` dizinine değişiklik yap ve push et
4. GitHub Actions otomatik olarak çevirir ve `content/en/` dizinine ekler

#### 2. Manuel Çeviri (Yerel)

```bash
# Gerekli paketleri yükle
pip install requests pyyaml

# DeepL ile çevir
python scripts/translate.py --api-provider deepl --api-key YOUR_DEEPL_KEY

# OpenAI ile çevir
python scripts/translate.py --api-provider openai --api-key YOUR_OPENAI_KEY

# Google Translate ile çevir
python scripts/translate.py --api-provider google --api-key YOUR_GOOGLE_KEY
```

#### 3. Pre-commit Hook (Otomatik Yerel Çeviri)

Her commit öncesi otomatik çeviri:

```bash
# Pre-commit hook'u kur
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# API anahtarını ortam değişkeninden al
if [ ! -z "$DEEPL_API_KEY" ]; then
    python scripts/translate.py --api-provider deepl --api-key "$DEEPL_API_KEY"
    git add content/en/
fi
EOF

chmod +x .git/hooks/pre-commit

# API anahtarını ekle (.bashrc veya .zshrc)
export DEEPL_API_KEY="your-key-here"
```

## 🎨 Özelleştirme

### Tema Ayarları

- `config/_default/config.toml` - Temel yapılandırma
- `config/_default/params.toml` - Tema parametreleri
- `config/_default/languages.tr.toml` - Türkçe dil ayarları
- `config/_default/languages.en.toml` - İngilizce dil ayarları

### Renkler ve Görünüm

`config/_default/params.toml` dosyasından değiştirilebilir:

```toml
colorScheme = "slate"        # slate, ocean, fire, etc.
defaultAppearance = "dark"   # light, dark, auto
```

## 📁 Proje Yapısı

```
.
├── config/
│   └── _default/
│       ├── config.toml          # Ana yapılandırma
│       ├── languages.tr.toml    # Türkçe ayarları
│       ├── languages.en.toml    # İngilizce ayarları
│       └── params.toml          # Tema parametreleri
├── content/
│   ├── tr/                      # Türkçe içerikler (ANA)
│   │   ├── posts/
│   │   │   └── vanet.md
│   │   └── about/
│   │       └── index.md
│   └── en/                      # İngilizce içerikler (OTOMATIK)
│       ├── posts/
│       └── about/
├── static/
│   └── img/                     # Görseller
├── scripts/
│   └── translate.py             # Çeviri scripti
├── themes/
│   └── blowfish/                # Hugo teması
└── .github/
    └── workflows/
        └── translate.yml        # GitHub Actions workflow
```

## 🔧 Çeviri Sistemi Detayları

### Nasıl Çalışır?

1. **Kaynak**: Türkçe içerikler `content/tr/` dizininde yazılır
2. **İşleme**: 
   - YAML frontmatter (`title`, `description`) çevrilir
   - Markdown body çevrilir
   - Hugo shortcode'ları korunur (`{{< button >}}`, vb.)
3. **Cache**: `.translation_cache.json` ile gereksiz API çağrıları önlenir
4. **Çıktı**: İngilizce içerikler `content/en/` dizinine yazılır

### Desteklenen Çeviri Sağlayıcıları

| Sağlayıcı | Kalite | Hız | Fiyat | API |
|-----------|--------|-----|-------|-----|
| **DeepL** | ⭐⭐⭐⭐⭐ | Hızlı | Ücretsiz tier: 500K karakter/ay | [deepl.com](https://www.deepl.com/pro-api) |
| **OpenAI GPT-4** | ⭐⭐⭐⭐⭐ | Orta | $0.03/1K token | [openai.com](https://platform.openai.com) |
| **Google Translate** | ⭐⭐⭐⭐ | Çok Hızlı | $20/1M karakter | [cloud.google.com](https://cloud.google.com/translate) |

### Çeviri Özelleştirmeleri

```python
# scripts/translate.py dosyasını düzenle

# Farklı kaynak/hedef diller
python scripts/translate.py --source-lang tr --target-lang de

# Belirli bir dizini çevir
python scripts/translate.py --content-dir blog/content

# Cache'i temizle ve yeniden çevir
python scripts/translate.py --force
```

## 🚀 Deployment

### GitHub Pages

```bash
# Hugo sitesini build et
hugo --minify

# public/ dizini GitHub Pages'e deploy et
# (Bu işlem genellikle GitHub Actions ile otomatikleştirilir)
```

### Netlify

```toml
# netlify.toml
[build]
  command = "hugo --minify"
  publish = "public"

[context.production.environment]
  HUGO_VERSION = "0.152.2"
  HUGO_ENV = "production"
```

## 🎨 Görsel Özellikler

### Animasyonlar & Efektler

- **Gradient Background** - Sürekli değişen animasyonlu arka plan
- **Particle Effects** - CSS ile 50 yüzen parçacık
- **3D Card Hover** - Mouse hareketine göre 3D dönme efekti
- **Typing Animation** - Ana başlıklarda yazı makinesi efekti
- **Scroll Reveal** - Kaydırınca elementler yumuşakça belirir
- **Glassmorphism** - Modern cam efekti kartlar
- **Gradient Text** - Renkli geçişli metinler
- **Smooth Scroll** - Yumuşak sayfa kaydırma
- **Custom Scrollbar** - Gradient renkli scrollbar
- **Scroll to Top FAB** - Sağ altta floating action button

### Custom Shortcode'lar

```markdown
{{< skill-bar name="C++" percentage="95" >}}
{{< gradient-text >}}Başlık{{< /gradient-text >}}
{{< glow-text >}}Parlayan Metin{{< /glow-text >}}
{{< counter number="4" suffix="+" text="Yıl Deneyim" >}}
{{< glass-card title="Başlık" >}}İçerik{{< /glass-card >}}
```

**Detaylı Bilgi**: [docs/ANIMATION_GUIDE.md](docs/ANIMATION_GUIDE.md)

## 📊 İstatistikler

- **Dil Desteği**: Türkçe (ana), İngilizce (otomatik)
- **Tema**: Blowfish (Fire colorScheme)
- **Build Süresi**: ~39ms ⚡
- **Çeviri Süresi**: ~2-5 saniye/sayfa
- **Animasyonlar**: GPU-accelerated
- **Accessibility**: WCAG uyumlu

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing`)
3. Değişiklikleri commit edin (`git commit -m 'feat: Add amazing feature'`)
4. Branch'i push edin (`git push origin feature/amazing`)
5. Pull Request açın

---

## 🔗 Bağlantılar

- **Blog**: https://tunagrskn.github.io/tg-blog/
- **GitHub**: https://github.com/tunagrskn
- **LinkedIn**: https://linkedin.com/in/tunagrskn
- **Email**: tunagirisken@outlook.com

## 📄 Lisans

This project is licensed under the MIT License.

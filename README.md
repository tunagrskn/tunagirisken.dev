# tunagirisken.dev

Kisisel web sitesi ve teknik blog. [Hugo](https://gohugo.io/) + [Blowfish](https://blowfish.page/) temasi uzerine ozellesirilmis layoutlar ile insa edilmistir.

## Teknolojiler

- **Hugo** v0.152+ — Statik site ureteci
- **Blowfish** — Hugo temasi (git submodule)
- **Tailwind CSS** — Stil
- **Material Symbols** — Ikon seti

## Proje Yapisi

```
config/_default/        # Site, tema ve dil ayarlari
content/
  about/                # Hakkimda sayfasi
  contact/              # Iletisim sayfasi
  posts/                # Blog yazilari
layouts/
  index.html            # Ana sayfa
  about/single.html     # Hakkimda layoutu
  contact/single.html   # Iletisim layoutu
  posts/                # Yazi liste ve detay layoutlari
  partials/             # Nav, footer, head eklentileri
  shortcodes/           # Ozel shortcode'lar
assets/
  css/custom.css        # Ozel stiller ve animasyonlar
  img/                  # Gorseller
```

## Yerel Gelistirme

```bash
hugo server -D          # Canli onizleme (draft dahil)
hugo --gc --minify      # Production build
```

### run.sh

```bash
./run.sh serve          # Gelistirme sunucusu
./run.sh build          # Production build
./run.sh zip            # Build + ZIP paketi
./run.sh clean          # public/ temizligi
```

## Yeni Yazi Ekleme

```bash
hugo new posts/yazi-adi/index.md
```

Gorselleri ayni klasore koy. Front matter'da `draft: true` kaldirarak yayinla.

## Lisans

Icerik [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) ile lisanslanmistir.
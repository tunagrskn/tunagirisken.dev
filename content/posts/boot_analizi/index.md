---
title: "Gömülü Linux Boot Optimizasyonu"
date: 2025-01-05
draft: false
description: "systemd-analyze ve bootchart araçlarıyla Linux boot süresini ölçme, analiz etme ve optimize etme rehberi"
tags: ["Linux", "Boot", "Embedded Systems", "Performans", "Yocto"]
categories: ["Embedded Systems"]
showHero: true
---

# Boot Performansı Analizi: Boot Süresini Ölçme ve Optimize Etme Araçları

Boot süresi, gömülü Linux sistemleri için kritik bir performans metriğidir. Özellikle sistemin hızla ayağa kalkması gereken uygulamalarda bu metrik hayati önem taşır. Otomotiv sistemleri, endüstriyel kontrolörler ya da IoT cihazları geliştiriyor olun fark etmez; boot performansını anlamak ve optimize etmek, kullanıcı deneyimini ve sistem tepki süresini ciddi ölçüde iyileştirir.

Bu rehber, Linux boot performansını ölçmek, analiz etmek ve optimize etmek için kullanılan temel araçları ve yöntemleri ele almaktadır.

## Boot Aşamalarını Anlamak

Analiz araçlarına geçmeden önce boot sürecini kavramak gerekir:

1. **Firmware/Bootloader** - Donanım initialization ve bootloader çalıştırma
2. **Kernel Boot** - Linux kernel'in yüklenmesi ve başlatılması
3. **Userspace Init** - Sistem servislerinin ve uygulamaların ayağa kalkması

Modern systemd tabanlı sistemler, boot süresinin büyük kısmını oluşturan 2. ve 3. aşamalar için mükemmel görünürlük sağlar.

## Temel Analiz Araçları

### systemd-analyze: Ana Boot Analiz Aracınız

`systemd-analyze` komutu systemd ile birlikte gelir ve ek kurulum gerektirmeden kapsamlı boot süresi analizi sunar.

#### Temel Boot Süresi Ölçümü

```bash
# Toplam boot süresinin dökümünü göster
systemd-analyze

# Örnek çıktı:
# Startup finished in 2.847s (kernel) + 12.534s (userspace) = 15.381s
```

Bu tek komut size büyük resmi verir: kernel'in initialize olmasının ne kadar sürdüğünü ve userspace servislerin ayağa kalkmasının ne kadar zaman aldığını.

#### Servis Bazlı Analiz

```bash
# Tüm servisleri initialization süresine göre sıralı listele
systemd-analyze blame

# Sadece en yavaş 20 servisi göster
systemd-analyze blame | head -20

# 1 saniyeden uzun süren servisleri bul
systemd-analyze blame | awk '$1 > "1s" {print}'
```

`blame` alt komutu, hangi servislerin boot süresini tükettiğini belirlemek için son derece değerlidir. Ancak şunu unutmayın: servisler paralel başlayabildiğinden, toplam servis süresi her zaman boot süresine olan gerçek etkiyi yansıtmaz.

#### Critical Path Analizi

```bash
# Critical boot path'i göster (diğerlerini bloke eden servisler)
systemd-analyze critical-chain

# Belirli bir servisin dependency'lerini analiz et
systemd-analyze critical-chain servis-adiniz.service

# Örnek çıktı:
# graphical.target @8.234s
# └─multi-user.target @8.233s
#   └─network.target @8.210s
#     └─NetworkManager.service @3.156s +5.051s
```

Critical chain, boot'un tamamlanmasını fiilen hangi servislerin engellediğini gösterir. Bu zincirde yer almayan servisler, boot süresini etkilemeden ertelenebilir veya optimize edilebilir.

### Görsel Analiz Araçları

#### Boot Timeline Görselleştirme

```bash
# Boot sürecinin SVG timeline'ını oluştur
systemd-analyze plot > boot-timeline.svg

# Dependency graph'ı görüntüle
systemd-analyze dot | dot -Tsvg > boot-dependencies.svg
```

Bu görsel çıktılar şunları belirlemenize yardımcı olur:

- Paralel ve sıralı servis başlatma durumu
- Dependency darboğazları
- Paralelleştirme fırsatları
- Gereksiz yere erken başlayan servisler

#### Bootchart2: Detaylı Sistem Aktivitesi

Bootchart, boot sırasında CPU, disk I/O ve process aktivitesi dahil olmak üzere daha detaylı sistem seviyesi bilgi sağlar.

```bash
# Bootchart2 kurulumu (Debian/Ubuntu)
apt-get install bootchart2

# Yocto/gömülü sistemler için image recipe'ye ekleyin:
IMAGE_INSTALL += "bootchart2"
```

Kurulumdan sonra bootchart her boot'ta otomatik olarak chart üretir ve bunları `/var/log/bootchart/` altında saklar.

### Ek Diagnostik Komutlar

```bash
# Servis durumlarını doğrula
systemctl list-units --state=failed

# Ordering cycle'ları olan servisleri kontrol et
systemctl list-dependencies --all

# Belirli bir servisin timing'ini incele
systemctl status <servis-adi>

# Yavaş başlayan servislerin loglarını incele
journalctl -u <servis-adi> -b
```

## Sonuçları Yorumlama ve Hedef Belirleme

### Gerçekçi Boot Süresi Hedefleri

Boot süresi hedefleri sistem gereksinimlerine göre önemli ölçüde değişir:

**Tüketici Gömülü Cihazları:**
- Kernel: < 2s
- Userspace: < 5s
- Toplam: < 8s

**Endüstriyel/Otomotiv Sistemleri:**
- Kernel: < 3s
- Userspace: < 10s
- Toplam: < 15s

**Sunucu/Kompleks Sistemler:**
- Kernel: < 5s
- Userspace: < 30s
- Toplam: < 40s

### Yaygın Boot Süresi Suçluları

`systemd-analyze blame` çıktısını analiz ederken şu tipik yavaş servislere dikkat edin:

1. **Network Servisleri** - NetworkManager, systemd-networkd (genellikle 2-5s)
2. **Disk Servisleri** - fsck, filesystem mount, RAID initialization
3. **Güvenlik Servisleri** - SSH key generation, random number generator initialization
4. **Veritabanı Servisleri** - PostgreSQL, MySQL (boot'ta etkinse)
5. **Hardware Enumeration** - ModemManager, bluetooth, USB device discovery
6. **Custom Script'ler** - Legacy init script'leri, kötü optimize edilmiş startup kodu

## Optimizasyon Stratejileri

### 1. Gereksiz Servisleri Eleyin

```bash
# Tüm etkin servisleri listele
systemctl list-unit-files --state=enabled

# Boot'ta gerekmeyen servisleri devre dışı bırak
systemctl disable <servis-adi>

# Bir servisin başlamasını tamamen engelle
systemctl mask <servis-adi>

# Devre dışı bırakmak için yaygın adaylar:
systemctl disable bluetooth.service
systemctl disable avahi-daemon.service
systemctl disable ModemManager.service
```

### 2. Servis Dependency'lerini Optimize Edin

Gereksiz ordering dependency'lerini kaldırmak için servis unit dosyalarını düzenleyin:

```ini
[Unit]
Description=Benim Uygulamam
# Sadece gerçekten gerekli dependency'leri dahil edin
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/bin/benim-uygulamam

[Install]
WantedBy=multi-user.target
```

**Temel prensipler:**

- Mümkün olduğunda `Requires=` yerine `Wants=` kullanın (daha yumuşak dependency)
- Paralel başlatmaya izin vermek için `After=` direktiflerini minimize edin
- `Before=` direktifini dikkatli kullanın, sadece sıralama kritik olduğunda

### 3. Socket Activation Uygulayın

Socket activation, servislerin boot'ta değil talep üzerine başlamasını sağlar:

```bash
# Socket'i etkinleştir, servisi devre dışı bırak
systemctl enable <servis>.socket
systemctl disable <servis>.service
```

Bir socket unit dosyası oluşturun:

```ini
# /etc/systemd/system/benim-servisim.socket
[Unit]
Description=Benim Servisim Socket

[Socket]
ListenStream=8080

[Install]
WantedBy=sockets.target
```

### 4. Kritik Olmayan Servisleri Erteleyin

Boot tamamlandıktan sonra servisleri başlatmak için timer unit'leri kullanın:

```ini
# /etc/systemd/system/ertelenmis-servis.timer
[Unit]
Description=Boot Sonrası Kritik Olmayan Servisi Başlat

[Timer]
OnBootSec=30s
Unit=ertelenmis-servis.service

[Install]
WantedBy=timers.target
```

### 5. Kernel ve Bootloader Optimizasyonu

```bash
# Kernel komut satırı optimizasyonları (bootloader config'e ekleyin):
# - Konsol ayrıntı düzeyini azalt: quiet loglevel=3
# - Kernel modül yükleme gecikmelerini atla: rootwait
# - Gereksiz özellikleri devre dışı bırak: noresume (hibernation yoksa)

# Örnek GRUB konfigürasyonu:
GRUB_CMDLINE_LINUX="quiet loglevel=3 rootwait"
```

### 6. Filesystem Optimizasyonu

```bash
# /etc/fstab'da daha hızlı filesystem seçenekleri kullanın:
# - noatime: erişim zamanlarını güncelleme
# - data=writeback: daha hızlı ama daha az güvenli (dikkatli kullanın)

/dev/mmcblk0p2  /  ext4  defaults,noatime  0  1
```

### 7. Custom Script'leri Paralelize Edin

Custom initialization script'leriniz varsa, gereksiz yere bloke etmediklerinden emin olun:

```ini
[Service]
Type=forking  # Daha hızlı startup için mümkünse 'simple' kullanın
ExecStart=/usr/bin/benim-scriptim
# Diğerleriyle paralel başlamasına izin ver
DefaultDependencies=no
```

## Performans Baseline Oluşturma

### Başlangıç Noktanızı Belgeleyin

```bash
# Kapsamlı bir boot raporu oluşturun
mkdir -p ~/boot-analysis
cd ~/boot-analysis

# Baseline metrikleri kaydedin
systemd-analyze > baseline-summary.txt
systemd-analyze blame > baseline-blame.txt
systemd-analyze critical-chain > baseline-critical.txt
systemd-analyze plot > baseline-timeline.svg

# Sistem bilgisi ekleyin
uname -a >> baseline-summary.txt
date >> baseline-summary.txt
```

### Sürekli İzleme

Bir boot süresi loglama script'i oluşturun:

```bash
#!/bin/bash
# /usr/local/bin/log-boot-time.sh

LOG_FILE="/var/log/boot-times.log"

{
    echo "=== Boot Analizi $(date) ==="
    systemd-analyze
    echo "En yavaş 10 servis:"
    systemd-analyze blame | head -10
    echo "---"
} >> "$LOG_FILE"
```

Bunu bir servis olarak etkinleştirin:

```ini
# /etc/systemd/system/log-boot-time.service
[Unit]
Description=Boot Süresi Analizini Logla
After=multi-user.target

[Service]
Type=oneshot
ExecStart=/usr/local/bin/log-boot-time.sh

[Install]
WantedBy=multi-user.target
```

### Öncesi/Sonrası Karşılaştırma

```bash
# Optimizasyon öncesi
systemd-analyze > /tmp/boot-once.txt
systemd-analyze blame | head -20 >> /tmp/boot-once.txt

# Değişikliklerinizi yapın, reboot edin

# Optimizasyon sonrası
systemd-analyze > /tmp/boot-sonra.txt
systemd-analyze blame | head -20 >> /tmp/boot-sonra.txt

# Karşılaştırın
diff -u /tmp/boot-once.txt /tmp/boot-sonra.txt
```

## İleri Düzey Analiz Teknikleri

### Kernel Boot Süresi Analizi

Derinlemesine kernel boot analizi için kernel'in dahili timing'ini kullanın:

```bash
# Bootloader'da kernel timing'i etkinleştirin (kernel komut satırına ekleyin):
initcall_debug printk.time=y

# Boot sonrası kernel logunu analiz edin:
dmesg | grep "initcall" | head -50

# En yavaş kernel initialization'ları bulun:
dmesg | grep "initcall" | sort -k 4 -n | tail -20
```

### Userspace Tracing

Detaylı uygulama seviyesi analiz için:

```bash
# Yavaş bir servisin ne yaptığını anlamak için strace kullanın
strace -tt -T -f -o /tmp/service-trace.log /usr/bin/servisiniz

# Filesystem erişim pattern'lerini analiz edin
strace -e trace=open,openat,read,write -o /tmp/fs-trace.log /usr/bin/servisiniz
```

### I/O Darboğaz Analizi

```bash
# Boot sırasında I/O'yu izleyin (iotop gerektirir)
# Reboot öncesi ayrı bir konsolda veya SSH ile çalıştırın:
iotop -b -o -d 1 > /tmp/boot-io.log &

# Boot sonrası analiz edin:
grep -E "systemd|servisiniz" /tmp/boot-io.log
```

## Pratik İş Akışı

### Adım Adım Optimizasyon Süreci

1. **Baseline Ölçün**
   ```bash
   systemd-analyze
   systemd-analyze blame | head -20
   systemd-analyze critical-chain
   ```

2. **Hedefleri Belirleyin**
   - 2 saniyeden uzun süren servisler
   - Critical chain üzerindeki servisler
   - Gereksiz dependency'leri olan servisler

3. **Optimizasyonları Uygulayın**
   - Gereksiz servisleri devre dışı bırakın
   - Dependency şişkinliğini temizleyin
   - Socket activation uygulayın
   - Kritik olmayan servisleri erteleyin

4. **Test Edin ve Doğrulayın**
   ```bash
   reboot
   # Boot sonrası:
   systemd-analyze
   systemctl --failed  # Bozuk servisleri kontrol edin
   ```

5. **İyileşmeyi Ölçün**
   ```bash
   # Öncesi/sonrası karşılaştır
   diff baseline-summary.txt current-summary.txt
   ```

6. **Değişiklikleri Belgeleyin**
   - Neyin değiştirildiğine dair notlar tutun
   - Servis hatalarını kaydedin
   - Nihai boot süresi iyileşmesini kaydedin

### Hızlı Sağlık Kontrolü Script'i

Kullanışlı bir analiz script'i oluşturun:

```bash
#!/bin/bash
# boot-health-check.sh

echo "=== Boot Süresi Özeti ==="
systemd-analyze

echo -e "\n=== En Yavaş 10 Servis ==="
systemd-analyze blame | head -10

echo -e "\n=== Critical Chain ==="
systemd-analyze critical-chain | head -15

echo -e "\n=== Başarısız Servisler ==="
systemctl --failed

echo -e "\n=== Degraded State'teki Servisler ==="
systemctl list-units --state=degraded
```

## Best Practice'ler ve Tuzaklar

### Yapılması Gerekenler

✔ **Her zaman önce baseline alın** - Başlangıç noktanızı bilin

✔ **Artımlı değişiklikler yapın** - Bir seferde tek bir şeyi değiştirin

✔ **Kapsamlı test edin** - Optimizasyon sonrası servislerin hâlâ çalıştığından emin olun

✔ **Her şeyi belgeleyin** - Neyi neden değiştirdiğinize dair notlar tutun

✔ **Critical path'e odaklanın** - Boot tamamlanmasını bloke eden servislere yoğunlaşın

✔ **Önce dahili araçları kullanın** - systemd-analyze ihtiyaçların %90'ını karşılar

### Yapılmaması Gerekenler

✗ **Servisleri körü körüne devre dışı bırakmayın** - Önce ne yaptıklarını anlayın

✗ **Erken optimizasyon yapmayın** - Önce ölçün, sonra optimize edin

✗ **Güvenilirlikten ödün vermeyin** - Hızlı boot, kararsız sistem demek olmamalı

✗ **Dependency'leri görmezden gelmeyin** - Dependency kaldırmak işlevselliği bozabilir

✗ **Edge case'leri unutmayın** - Cold boot, warm boot ve recovery senaryolarını test edin

✗ **Aşırı paralelleştirme yapmayın** - Çok fazla concurrency işleri yavaşlatabilir

## Sonuç

Boot süresi optimizasyonu; ölçüm, analiz ve sistematik iyileştirmeyi birleştiren iteratif bir süreçtir. systemd'nin sağladığı araçlar bu süreci basit ve veri odaklı hale getirir.

Temel çıkarımlar:

- `systemd-analyze` ile **ölçümle başlayın**
- Toplam servis süresi yerine **critical path'e odaklanın**
- Gereksiz servisleri **eleyin, erteleyin veya paralelize edin**
- Sistem stabilitesini sağlamak için **değişiklikleri doğrulayın**
- İyileştirmeleri korumak için **belgeleyin ve izleyin**

Bu araçlar ve yöntemlerle, sistem güvenilirliğini ve işlevselliğini korurken önemli boot süresi iyileştirmeleri elde edebilirsiniz. Unutmayın ki amaç sadece hızlı bir boot değil, stabil ve tam işlevsel bir sistem sunan hızlı bir boot'tur.

## Ek Kaynaklar

- [systemd Boot Optimization](https://www.freedesktop.org/wiki/Software/systemd/Optimizations/)
- [systemd.unit Man Page](https://www.freedesktop.org/software/systemd/man/systemd.unit.html)
- [systemd-analyze Documentation](https://www.freedesktop.org/software/systemd/man/systemd-analyze.html)
- [Boot Time Optimization Techniques](https://elinux.org/Boot_Time)

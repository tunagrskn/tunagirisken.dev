---
title: "Hakkımda"
date: 2025-01-05
layout: "simple"
---

<div style="text-align: center; margin: 2rem 0;">
  <img class="nozoom protected-img" src="profile.jpg" alt="Tuna Girişken" draggable="false" oncontextmenu="return false;" style="width: 200px; height: 200px; border-radius: 50%; object-fit: cover; box-shadow: 0 10px 30px rgba(0,0,0,0.2); -webkit-user-select: none; user-select: none; pointer-events: auto;">
</div>

{{< lead >}}
Karluna Mühendislik'te **Kıdemli Gömülü Linux Geliştirme Mühendisi** olarak çalışıyorum. Savunma ve otomotiv sektörlerinde emniyet kritik gömülü sistemlerin tasarım ve geliştirilmesinde 5 yılı aşkın deneyime sahibim.
{{< /lead >}}

{{< button href="Tuna_Girisken_En_Cv.pdf" target="_blank" >}}
📄 CV
{{< /button >}}

---

## Özet

Kıdemli Gömülü Yazılım Mühendisi olarak savunma ve otomotiv sektörlerinde emniyet kritik gömülü sistemlerin tasarım ve geliştirilmesinde 5 yılı aşkın deneyime sahibim. **Baykar Teknoloji** ve **TÜBİTAK SAGE**'de, üretim seviyesindeki havacılık ve savunma sistemleri için aviyonik ve gömülü yazılım mimarisi tasarlama ve geliştirme çalışmalarında aktif roller üstlendim.

Gerçek zamanlı işletim sistemleri (RTLinux, Zephyr) üzerinde, zamanlama hassasiyeti yüksek ve deterministik sistemlerin geliştirilmesi konusunda uzmanlığa sahibim. Çok çekirdekli (ARM Cortex-A53/A55, PowerPC, x86) MPU platformları için Yocto ve Buildroot tabanlı gömülü Linux sistemlerinin geliştirilmesi ile MCU tabanlı (ARM Cortex-R5/M4/M33) sistemlerde bare-metal firmware geliştirme alanlarında deneyimim bulunuyor.

Şu anda elektrikli ticari araçlar için uçtan uca bir **Telematics Control Unit (TCU)** yazılım yığınını mimariden uygulamaya kadar geliştiriyorum; CAN/J1939 araç ağları, GNSS konumlandırma, LTE bağlantısı, MQTT tabanlı bulut telemetrisi ve arka uç veri entegrasyonu gibi konularında teknik liderlik yapıyorum.

---

## Teknik Beceriler

| Kategori | Teknolojiler |
|----------|-------------|
| **Gömülü Sistemler** | Bare-metal programlama, RTOS (PREEMPT_RT, RTLinux, Zephyr), Gömülü Linux (Yocto, Buildroot), U-Boot, Devicetree, Linux Kernel Modülü ve Sürücü Geliştirme |
| **Programlama Dilleri** | C, C++ (98/11/14/17/20/23), Assembly, Python, Bash/Batch Scripting, QML, SQL |
| **Mimariler** | ARM Cortex (R5, M4, M33, A53, A55), PowerPC (P4080DS), x86 (Xeon D-1700) |
| **İletişim Protokolleri** | CAN/J1939, TCP/UDP, MQTT, I2C, SPI, UART, USB, RS-232/485, MIL-STD-1553 |
| **Gerçek Zamanlı Ağ** | Time-Sensitive Networking (TSN), Precision Time Protocol (IEEE 1588v2) |
| **Araçlar** | GCC, GDB, LLVM, Clang, CMake, Meson, Git/GitLab CI, QEMU, OpenSSL, Qt |
| **Standartlar** | JSF AV C++, MISRA-C/C++ |

---

## Deneyim

{{< timeline >}}
{{< timelineItem icon="star" header="Kıdemli Gömülü Linux Geliştirme Mühendisi" badge="Ara. 2024 - Günümüz" subheader="Karluna Mühendislik, İzmir" >}}
<ul>
<li>Hafif ticari elektrikli araçlar için uçtan uca <strong>Telematics Control Unit (TCU)</strong> yazılım yığınını mimariden uygulamaya kadar tasarladım</li>
<li>NXP i.MX93 SoC için otomotiv standartlarına uygun <strong>Yocto Linux dağıtımı</strong> geliştirdim</li>
<li>Modern C++ standartlarında kapsamlı bir telemetri yazılım çerçevesi geliştirdim; thread-safe CAN iletişim katmanı ve SAE J1939 protokol yığını implementasyonu</li>
<li><strong>OTA (Over-The-Air)</strong> güncelleme altyapısı tasarladım; delta paket yönetimi ve atomik güncelleme mekanizması</li>
<li>MQTT tabanlı bulut telemetrisi ile filo yönetimi ve uzaktan araç kontrolü sağladım</li>
<li>Quectel LTE modemlerini (EC2x/EGxx serisi) PPP ve QMI protokolleri ile entegre ettim</li>
</ul>
{{< /timelineItem >}}

{{< timelineItem icon="shield" header="Gömülü Linux Geliştirme Mühendisi" badge="Ara. 2022 - Kas. 2024" subheader="Baykar Teknoloji, İstanbul" >}}
<ul>
<li>Yeni nesil İHA görev bilgisayarları için <strong>gerçek zamanlı işletim sistemleri</strong> geliştirdim</li>
<li>Güvenlik kritik yazılım çerçevesini mimari düzeyinde tasarladım; <strong>JSF ve MISRA C/C++</strong> standartlarına tam uyum</li>
<li><strong>Time-Sensitive Networking (TSN)</strong> altyapısını geliştirdim; mikrosaniye altı zaman senkronizasyonu ve deterministik iletişim</li>
<li>Bare-metal MCU firmware'den Linux tabanlı MPU uygulamalarına kadar çeşitli gömülü mimarilerde çözümler tasarladım</li>
<li>Simetrik (AES) ve asimetrik (RSA/ECC) kriptografik algoritmaları kullanan gömülü güvenlik altyapısı uyguladım</li>
</ul>
{{< /timelineItem >}}

{{< timelineItem icon="shield" header="Gömülü Yazılım Mühendisi Stajyeri" badge="Şub. 2022 - May. 2022" subheader="TÜBİTAK SAGE, Ankara" >}}
<ul>
<li>ELDK ve Yocto kullanarak gömülü işletim sistemlerinin derleme ve entegrasyon süreçlerine katkı sağladım</li>
<li>VxWorks RTOS için bootloader seviyesinde <strong>NVMe sürücüsü</strong> geliştirdim</li>
<li>Füze sistemlerinde NVMe cihazları için önyükleme zamanı depolama başlatma işlemlerini entegre ettim</li>
</ul>
{{< /timelineItem >}}

{{< timelineItem icon="graduation-cap" header="Yazılım Eğitmeni" badge="Mar. 2022 - May. 2022" subheader="Deneyap Türkiye, Gaziantep" >}}
<ul>
<li>Gaziantep Büyükşehir Belediyesi ve T3 Vakfı desteğiyle <strong>C++ programlama kursu</strong> verdim</li>
<li>Bellek yönetimi, RAII, STL ve nesne yönelimli tasarım gibi ileri düzey C++ konularını işledim</li>
</ul>
{{< /timelineItem >}}
{{< /timeline >}}

---

## Projeler

{{< timeline >}}
{{< timelineItem icon="lightbulb" header="NXP P4080DS Özel Linux Dağıtımı" badge="PowerPC" subheader="2.8 GB/s NVMe Sürücü Geliştirme" >}}
<ul>
<li>PowerPC P4080DS platformu için U-Boot ve SPL optimizasyonları ile üretime hazır Yocto BSP</li>
<li>DMA desteğiyle bootloader seviyesinde NVMe PCIe sürücüsü; veri aktarım gecikmesini <strong>%40 azalttım</strong></li>
</ul>
{{< /timelineItem >}}

{{< timelineItem icon="lock" header="TI Sitara AM65x SBL Geliştirme" badge="ARM Cortex" subheader="Güvenli Önyükleme Sistemi" >}}
<ul>
<li>Bellek eşlemeli XIP ile OSPI Flash tabanlı Secondary Boot Loader (SBL); <strong>&lt;2 saniye önyükleme süresi</strong></li>
<li>Şifrelenmiş görüntü doğrulaması ile güvenli önyükleme zinciri uyguladım</li>
</ul>
{{< /timelineItem >}}
{{< /timeline >}}

---

## Eğitim

{{< timeline >}}
{{< timelineItem icon="graduation-cap" header="Yüksek Lisans - Bilgisayar Mühendisliği" badge="2025 - Devam Ediyor" subheader="Ege Üniversitesi, İzmir" >}}
{{< /timelineItem >}}

{{< timelineItem icon="graduation-cap" header="Lisans - Elektrik-Elektronik Mühendisliği" badge="2017 - 2022" subheader="Hasan Kalyoncu Üniversitesi, Gaziantep" >}}
%100 İngilizce Burs | Bitirme Projesi: PID kontrolü ile RF tabanlı step motor kontrol sistemi
{{< /timelineItem >}}
{{< /timeline >}}

---

## İletişim

{{< button href="https://github.com/tunagrskn" target="_blank" >}}
{{< icon "github" >}} GitHub
{{< /button >}}

{{< button href="https://linkedin.com/in/tunagrskn" target="_blank" >}}
{{< icon "linkedin" >}} LinkedIn  
{{< /button >}}

{{< button href="mailto:tunagirisken@outlook.com" >}}
{{< icon "email" >}} Email
{{< /button >}}

---

{{< skill-banner >}}

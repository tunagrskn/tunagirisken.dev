---
title: "VPN ve APN: Erişim Noktaları Arasındaki Farklar"
date: 2025-01-05
draft: false
description: "VPN ve APN teknolojilerinin detaylı karşılaştırması, çalışma prensipleri ve gömülü sistemlerdeki kullanım alanları"
tags: ["VPN", "APN", "Network", "Security"]
categories: ["Networking"]
showHero: true
---

Gömülü sistemler ve IoT cihazları geliştirirken en sık karşılaşılan sorulardan biri şudur: "Cihazım internete nasıl çıkacak ve bu bağlantı ne kadar güvenli olacak?" Bu noktada iki temel kavram devreye girer — **APN** ve **VPN**. Her ikisi de ağ erişimiyle ilgili olsa da, birbirinden tamamen farklı katmanlarda çalışan teknolojilerdir. Bu yazıda her iki teknolojiyi detaylıca inceleyecek, aralarındaki farkları netleştirecek ve özellikle gömülü sistemler bağlamında nasıl kullanıldıklarına bakacağız.

## APN Nedir?

**APN (Access Point Name — Erişim Noktası Adı)**, bir mobil cihazın hücresel ağ üzerinden dış dünyaya (internet veya özel bir kurumsal ağ) bağlanırken kullandığı ağ geçidini tanımlayan yapılandırma parametresidir. Daha teknik bir ifadeyle APN, mobil cihaz ile operatörün **Packet Data Network Gateway (PGW/P-GW)** arasındaki bağlantıyı kuran mantıksal bir isimdir.

Bir telefon ya da IoT modülü hücresel ağa bağlandığında, veri oturumu başlatmak için operatöre bir APN bilgisi gönderir. Operatör bu bilgiye göre cihazı doğru ağ geçidine yönlendirir: genel internete mi çıkacak, kurumsal bir VPN'e mi bağlanacak, yoksa özel bir MMS sunucusuna mı erişecek — tüm bunlar APN üzerinden belirlenir.

### APN'in Yapısı

Bir APN iki ana bileşenden oluşur:

- **Network Identifier (Ağ Tanımlayıcı):** Bağlanılacak dış ağı belirtir. Örneğin `internet`, `kurumsal` veya `m2m` gibi isimler olabilir.
- **Operator Identifier (Operatör Tanımlayıcı):** Hangi operatör ağına ait olduğunu belirten, MCC (Mobile Country Code) ve MNC (Mobile Network Code) bilgilerini içeren opsiyonel kısımdır. Örneğin Türkiye'deki Turkcell için `mnc001.mcc286.gprs` gibi bir yapı kullanılır.

Tam bir APN şu şekilde görünür:

```
internet.mnc001.mcc286.gprs
```

Ancak pratikte çoğu zaman sadece ağ tanımlayıcı kısmı (`internet`, `web`, `m2m.provider.com` gibi) kullanılır.

### APN Türleri

| APN Türü | Açıklama | Örnek Kullanım |
|----------|----------|----------------|
| **Genel APN** | Cihazı doğrudan internete çıkarır | Telefon internet erişimi |
| **Özel/Kurumsal APN** | Cihazı operatörün özel bir ağ segmentine yönlendirir | Filo yönetimi, kurumsal IoT |
| **M2M APN** | Makineler arası iletişim için optimize edilmiş | Telematik cihazlar, sensörler |
| **MMS APN** | Multimedya mesajlaşma hizmeti için | MMS gönderimi |
| **Sabit IP APN** | Cihaza her bağlantıda aynı IP adresini atar | Uzaktan erişim gereken cihazlar |

### APN ve Gömülü Sistemler

Gömülü Linux sistemlerinde hücresel bağlantı genellikle **ModemManager** ve **NetworkManager** üzerinden ya da doğrudan **AT komutları** ile yönetilir. Bir LTE modülünü (örneğin Quectel EC25, Sierra Wireless HL7812) yapılandırırken APN ayarı şu şekilde yapılır:

```bash
# AT komutuyla APN tanımlama
AT+CGDCONT=1,"IP","m2m.provider.com"

# ModemManager ile bağlantı kurma
mmcli -m 0 --simple-connect="apn=m2m.provider.com"

# NetworkManager ile profil oluşturma
nmcli connection add type gsm con-name "lte-baglanti" \
  ifname "*" apn "m2m.provider.com"
```

Özellikle TCU (Telematics Control Unit) veya endüstriyel gateway gibi cihazlarda özel M2M APN'ler tercih edilir. Bunun birkaç önemli sebebi vardır:

1. **Sabit veya öngörülebilir IP adresi** atanabilir, bu sayede uzaktan erişim kolaylaşır.
2. **Özel ağ segmenti** sayesinde cihaz trafiği genel internet trafiğinden izole edilir.
3. **QoS (Quality of Service)** parametreleri M2M trafiğine göre optimize edilebilir.
4. **Güvenlik politikaları** daha sıkı şekilde uygulanabilir.

## VPN Nedir?

**VPN (Virtual Private Network — Sanal Özel Ağ)**, mevcut bir ağ altyapısı (genellikle internet) üzerinden şifreli ve güvenli bir tünel oluşturarak iki nokta arasında özel bir bağlantı kurma teknolojisidir.

VPN'in özünde yaptığı iş oldukça basittir: veriyi göndermeden önce şifreler, bir "tünel" içine koyar ve karşı tarafa ulaştığında tekrar çözer. Bu süreçte aradaki hiçbir düğüm — ne ISP, ne de üzerinden geçilen yönlendiriciler — verinin içeriğini göremez.

### VPN Nasıl Çalışır?

VPN bağlantısı kurulurken şu adımlar gerçekleşir:

1. **Kimlik doğrulama (Authentication):** İstemci ve sunucu birbirini doğrular. Sertifika tabanlı (X.509), kullanıcı adı/parola veya pre-shared key (PSK) yöntemleri kullanılabilir.
2. **Anahtar değişimi (Key Exchange):** Şifreleme için kullanılacak oturum anahtarları güvenli bir şekilde paylaşılır. Genellikle Diffie-Hellman veya ECDH algoritmaları kullanılır.
3. **Tünel oluşturma (Tunnel Establishment):** Şifreli iletişim kanalı kurulur. Orijinal IP paketleri yeni bir başlıkla sarmalanır (enkapsülasyon).
4. **Veri iletimi:** Tüm trafik şifreli tünelden geçer. Dışarıdan bakıldığında sadece VPN sunucusuyla iletişim kurulduğu görülür.

### VPN Protokolleri

Farklı senaryolar için farklı VPN protokolleri geliştirilmiştir:

| Protokol | Katman | Şifreleme | Kullanım Alanı |
|----------|--------|-----------|----------------|
| **IPsec** | L3 (Ağ) | AES, 3DES | Site-to-site bağlantılar, kurumsal ağlar |
| **OpenVPN** | L3/L4 | OpenSSL (AES-256-GCM) | Genel amaçlı, esnek yapılandırma |
| **WireGuard** | L3 | ChaCha20, Curve25519 | Yüksek performans, düşük gecikme |
| **L2TP/IPsec** | L2 | IPsec ile birlikte | Eski sistemlerle uyumluluk |
| **PPTP** | L2 | MPPE (zayıf) | ❌ Güvenli değil, kullanılmamalı |

### VPN Topolojileri

VPN bağlantıları farklı topolojilerde kurulabilir:

**Site-to-Site VPN:** İki farklı lokasyondaki ağları birbirine bağlar. Örneğin bir fabrikanın yerel ağı ile merkez ofis ağı arasında kalıcı bir tünel kurulur. Her iki tarafta da bir VPN gateway bulunur ve arkasındaki tüm cihazlar karşı ağa erişebilir.

**Remote Access VPN:** Tek bir cihazın uzak bir ağa güvenli şekilde bağlanmasını sağlar. Sahadan çalışan mühendislerin şirket ağına erişimi bu modelle yapılır.

**Hub-and-Spoke VPN:** Birden fazla uç noktanın merkezi bir sunucu üzerinden birbirine bağlandığı yapıdır. IoT cihaz filolarında sıklıkla tercih edilir — tüm cihazlar merkezi bir VPN sunucusuna bağlanır ve gerektiğinde birbirleriyle bu merkez üzerinden iletişim kurar.

### VPN ve Gömülü Sistemler

Gömülü Linux cihazlarda VPN yapılandırması genellikle **WireGuard** veya **OpenVPN** üzerinden yapılır. WireGuard, çekirdek seviyesinde çalışması ve minimalist tasarımı sayesinde kaynak kısıtlı gömülü sistemlerde öne çıkmaktadır.

```bash
# WireGuard arayüzü oluşturma
ip link add dev wg0 type wireguard

# Yapılandırma dosyası uygulama
wg setconf wg0 /etc/wireguard/wg0.conf

# Arayüzü aktifleştirme
ip addr add 10.0.0.2/24 dev wg0
ip link set wg0 up

# Yönlendirme ekleme
ip route add 192.168.1.0/24 dev wg0
```

Yocto ile geliştirilen bir gömülü Linux imajında WireGuard desteği eklemek için:

```bash
# local.conf veya image recipe'ye eklenir
IMAGE_INSTALL:append = " wireguard-tools wireguard-module"

# Kernel konfigürasyonuna eklenir (5.6 öncesi çekirdekler için)
CONFIG_WIREGUARD=m
```

Bir TCU veya endüstriyel gateway senaryosunda VPN şu amaçlarla kullanılır:

- **Uzaktan firmware güncelleme (OTA):** Güncelleme sunucusuna güvenli erişim
- **Telemetri verisi iletimi:** MQTT/AMQP trafiğinin şifrelenmesi
- **Uzaktan tanılama:** SSH üzerinden cihaza güvenli erişim
- **Cihaz filosu yönetimi:** Tüm cihazların merkezi bir VPN ağında toplanması

## APN ile VPN Arasındaki Temel Farklar

Bu iki teknoloji farklı soruları yanıtlar:

- **APN** → "Cihazım hücresel ağdan *nereye* bağlanacak?"
- **VPN** → "Bağlantım *nasıl* korunacak?"

| Özellik | APN | VPN |
|---------|-----|-----|
| **Katman** | Hücresel ağ erişim katmanı | Uygulama/Ağ katmanı |
| **Temel işlev** | Ağ geçidi tanımlama | Şifreli tünel oluşturma |
| **Şifreleme** | Kendisi şifreleme yapmaz | Uçtan uca şifreleme sağlar |
| **Bağımsızlık** | Operatöre bağımlı | Operatörden bağımsız |
| **IP ataması** | Operatör tarafından | VPN sunucusu tarafından |
| **Kapsam** | Hücresel bağlantıya özel | Her türlü ağ üzerinde çalışır |
| **Yapılandırma** | Operatörle koordineli | Tamamen kullanıcı kontrolünde |
| **Maliyet** | Operatör tarifesine dahil | Ek altyapı/lisans maliyeti |

## Birlikte Kullanım: APN + VPN

Pratikte APN ve VPN birbirinin alternatifi değil, tamamlayıcısıdır. Özellikle gömülü sistemlerde en sağlam mimari ikisinin birlikte kullanıldığı yapıdır.

Tipik bir senaryo şu şekilde işler:

```
[TCU Cihazı] → LTE Modül (APN: m2m.operator.com) → Operatör PGW → İnternet
                                                                      ↓
                                                              WireGuard Tünel
                                                                      ↓
                                                            [Bulut VPN Sunucusu]
                                                                      ↓
                                                            [MQTT Broker / OTA Sunucu]
```

Bu mimaride:

1. **APN** cihazı operatörün M2M ağ segmentine yönlendirir — böylece cihaz genel internet trafiğinden izole olur.
2. **VPN** tüneli ise internet üzerinden geçen trafiği şifreler — operatör dahil hiç kimse veri içeriğini göremez.

### Katmanlı Güvenlik Yaklaşımı

Üretim ortamında güvenlik tek bir katmana bırakılmamalıdır. APN ve VPN'in birlikte kullanımı **defense in depth (derinlemesine savunma)** prensibine uygundur:

| Katman | Teknoloji | Sağladığı Koruma |
|--------|-----------|------------------|
| Fiziksel | SIM kilidi, cihaz sertleştirme | Fiziksel erişim koruması |
| Ağ erişimi | Özel APN | Ağ segmentasyonu |
| İletişim | VPN (WireGuard/IPsec) | Uçtan uca şifreleme |
| Uygulama | TLS/mTLS | Uygulama seviyesi doğrulama |
| Veri | Payload şifreleme | Veri bütünlüğü |

## Sonuç

APN ve VPN, ağ iletişiminin farklı katmanlarında farklı sorunları çözen teknolojilerdir. APN, hücresel ağda cihazın hangi kapıdan çıkacağını belirlerken; VPN, o kapıdan çıktıktan sonra verinin güvenli bir şekilde hedefe ulaşmasını sağlar.

Gömülü sistemler geliştirirken bu iki teknolojiyi birbirinin alternatifi olarak değil, birlikte çalışan güvenlik katmanları olarak düşünmek gerekir. Özel bir M2M APN üzerinden çıkış yapıp, ardından WireGuard tüneli ile bulut altyapısına bağlanan bir cihaz — hem operatör tarafında izole edilmiş hem de internet üzerinde şifrelenmiş bir bağlantıya sahip olur.

Sonuç olarak güvenli bir bağlantı tek bir teknolojiye değil, doğru katmanda doğru aracı kullanmaya dayanır.


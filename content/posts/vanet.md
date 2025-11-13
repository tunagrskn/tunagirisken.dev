# Vehicular Ad-Hoc Networks (VANET): Akıllı Ulaşımın Geleceği

Modern ulaşım sistemleri hızla dijitalleşiyor ve araçlar artık sadece birer taşıt değil, aynı zamanda birbirleriyle ve çevreleriyle sürekli iletişim halinde olan akıllı cihazlar haline geliyor. Bu dönüşümün merkezinde **Vehicular Ad-Hoc Networks (VANET)** teknolojisi yer alıyor. Peki VANET nedir ve neden bu kadar önemli? Bu yazıda, VANET'in temellerinden uygulamalarına kadar her şeyi detaylıca inceleyeceğiz.

## Ad-Hoc Networks: Temel Kavramlar

VANET'i anlamadan önce, Ad-Hoc ağların ne olduğunu kavramak gerekiyor. **Ad-hoc network**, kelime anlamı olarak "anlık, belirli bir amaç için oluşturulan" ağ demektir. Bilgisayar ağları bağlamında ise önceden var olan bir altyapıya ihtiyaç duymadan, birbirine doğrudan bağlanan düğümlerden oluşan kendi kendini organize eden kablosuz ağlar anlamına gelir.

Bu ağların en önemli özelliği, merkezi bir yönlendirici (router), erişim noktası (access point) veya baz istasyonu olmamasıdır. Her düğüm hem istemci hem de yönlendirici görevi görebilir. Düğümler arası iletişim çok atlamalı (multi-hop) olabilir; yani A → B → C şeklinde veri aktarımı yapılabilir.

## Ad-Hoc Networks'ün Temel Özellikleri

### 1. Merkezi Olmayan (Decentralized) Mimari

Klasik ağlarda iletişim genellikle bir erişim noktası üzerinden yürürken, Ad-hoc ağlarda merkezi bir yönetici yoktur. Her bir düğüm (node) hem istemci hem yönlendirici görevi görür. Bu sayede ağ, herhangi bir merkez noktasının çökmesi durumunda bile iletişimi sürdürebilir ve tek hata noktasını (single point of failure) ortadan kaldırır.

Ancak bu durum yönlendirme ve kaynak yönetimi süreçlerini karmaşıklaştırır, çünkü ağdaki tüm düğümler bu yükü paylaşmak zorundadır.

### 2. Kendi Kendini Organize Edebilme (Self-Organizing)

Ad-hoc ağlar önceden yapılandırmaya ihtiyaç duymadan çalışabilir. Düğümler birbirini otomatik olarak keşfeder (neighbor discovery), bağlantı kurar ve gerektiğinde ağ topolojisini yeniden oluşturur. Bu özellik özellikle afet bölgeleri, askeri operasyonlar veya geçici etkinlik alanları gibi dinamik ortamlarda kritik avantaj sağlar.

Ağ topolojisi değiştikçe, düğümler yönlendirme tablolarını günceller. Bu süreç genellikle protokol tabanlıdır (örneğin AODV, DSR, OLSR).

### 3. Dinamik Topoloji (Dynamic Topology)

Ad-hoc ağların en belirgin özelliklerinden biri topolojinin sürekli değişebilmesidir. Düğümler (araçlar, telefonlar, dronlar) hareket ettikçe bağlantılar kopabilir veya yeni bağlantılar oluşabilir. Bu durum ağın sürekli olarak yeni yollar hesaplamasını gerektirir.

Bu sebeple dinamik yönlendirme algoritmaları kullanılır. Bu yapı yüksek esneklik sağlar ama aynı zamanda latency ve paket kaybı gibi zorlukları da beraberinde getirir.

### 4. Çok Atlama (Multi-Hop) İletişimi

Ad-hoc ağlarda iki düğüm arasındaki doğrudan iletişim her zaman mümkün değildir. Bu durumda veri, arada bulunan diğer düğümler üzerinden çok atlamalı bir şekilde iletilir. Her düğüm, kendisine gelen paketleri hedefe ulaşana kadar yönlendirir.

Bu mekanizma sayesinde ağ kapsama alanı genişler; örneğin 100 m menzilli düğümler 3 atlamayla 300 m uzaklıktaki hedefe ulaşabilir. Ancak çok atlamalı iletişim enerji tüketimini, gecikmeyi ve paket kaybı riskini artırır.

### 5. Enerji Kısıtlılık (Energy Constraints)

Özellikle taşınabilir cihazlar (sensörler, araç modülleri, mobil terminaller) pil gücüyle çalıştığı için enerji verimliliği kritik önemdedir. Bu nedenle Ad-hoc ağlarda yönlendirme protokolleri yalnızca en kısa yolu değil, aynı zamanda enerji açısından en uygun yolu da hesaba katabilir. Bu yaklaşım "Energy-Aware Routing" olarak bilinir.

### 6. Kısıtlı Bant Genişliği (Limited Bandwidth)

Kablosuz iletişim kanalları, kablolu ağlara göre daha dar bant genişliğine sahiptir. Ayrıca kanalın paylaşılması (CSMA/CA veya TDMA gibi erişim yöntemleriyle) çatışmalara ve paket gecikmelerine neden olabilir.

Ancak son yıllarda 5G D2D (Device-to-Device) ve 802.11p (VANET standardı) gibi teknolojilerle bu kısıtlar büyük oranda azaltılmıştır.

## Ad-Hoc Networks Ağ Mimarisi

Ad-hoc ağlar, önceden kurulmuş bir altyapıya ihtiyaç duymadan, mobil veya sabit cihazların doğrudan birbirleriyle haberleştiği dağıtık yapılı ağlardır. Bu mimaride her cihaz bir terminal (end node) olarak veri üretip tüketir ve aynı zamanda bir yönlendirici (router node) gibi davranarak diğer düğümlerin trafiğini iletir. Yani ağda "her düğüm hem kullanıcı hem yönlendiricidir."

### Ağ Mimarisi Türleri

**Saf (Pure) Ad-Hoc Mimari:**
- Hiçbir altyapı yoktur
- Tüm düğümler eşit konumdadır
- Veri yalnızca multi-hop (çok atlamalı) olarak taşınır
- Avantajı: Esneklik, hızlı kurulum, altyapıya bağımlılık yok
- Dezavantajı: Yönlendirme karmaşık, ölçeklenebilirlik sınırlı

**Hibrit (Hybrid) Ad-Hoc Mimari:**
- Kısmen altyapı bulunur (erişim noktaları veya sabit istasyonlar)
- Mobil düğümler birbirleriyle doğrudan iletişim kurabilir, ancak gerektiğinde altyapı üzerinden de haberleşir
- VANET, MANET, Mesh Network gibi sistemlerde sıkça görülür
- Avantajı: Daha iyi kapsama alanı ve yönlendirme verimliliği

## Ad-Hoc Networks Türleri

### MANET (Mobile Ad-hoc Network)

MANET, mobil cihazların statik altyapıdan bağımsız olarak, dinamik topolojiye sahip, kendiliğinden organize olan ağlardır. Bu ağlar, sürekli hareket eden düğümlerle birlikte, yönlendirme protokollerinin yüksek mobiliteyi ve sık topoloji değişikliklerini yönetmesini gerektirir.

### VANET (Vehicular Ad-hoc Network)

VANET, araçlar arasındaki doğrudan iletişimi sağlayan, yüksek hızda hareket eden ve sık sık bağlantı kopmalarına neden olan ağlardır. Bu ağlar, düşük gecikme süreleri ve güvenilir veri iletimi için, özellikle yönlendirme ve güvenlik protokollerinde optimizasyon gerektirir.

### SANET (Sensor Ad-hoc Network)

SANET, dağıtık sensör düğümlerinin birbirleriyle iletişim kurarak çevresel verileri topladığı ve ilettiği ağlardır. Düşük enerji tüketimi ve veri iletimi için verimli protokoller gerektiren bu ağlar, genellikle düşük bant genişliğine sahip, yüksek gecikmeli ve düşük maliyetli ağlardır.

### FANET (Flying Ad-hoc Network)

FANET, insansız hava araçları (İHA) arasındaki ağları ifade eder ve bu ağlar, uçuş esnasında düşük gecikmeli veri iletimi ve yüksek hızda yönlendirme gereksinimlerini karşılamalıdır. FANET, uçuş dinamiklerine bağlı olarak sık sık topoloji değişiklikleri yaşar ve bu da ağın güvenilirliğini artıran özel yönlendirme ve hata toleranslı protokoller gerektirir.

## VANET: Araç Ağlarının Derinlemesine İncelenmesi

**Vehicular Ad-Hoc Network (VANET)**, araçların kendi aralarında ve yol kenarı altyapılarla kablosuz iletişim kurarak kendiliğinden ağlar oluşturduğu, Akıllı Ulaşım Sistemleri'nin temel bileşenidir. Her araç hem veri gönderen hem de veri ileten bir düğüm görevi üstlenir.

VANET'in temel özellikleri:
- Merkezi bir yönlendirici, erişim noktası veya baz istasyonu yoktur
- Her düğüm (araç) hem istemci hem yönlendirici görevi görebilir
- Düğümler arası iletişim çok atlamalı olabilir (A → B → C şeklinde)

## VANET Ağ Mimarisi

VANET ekosistemi, farklı iletişim türlerini kapsayan kapsamlı bir mimari üzerine kurulmuştur:

### V2V (Vehicle-to-Vehicle): Araçlar Arası İletişim

Araçlar arası doğrudan iletişim, VANET'in en temel bileşenidir. Araçlar birbirleriyle kablosuz iletişim kurarak hız, konum ve fren durumu gibi bilgileri paylaşır. Çarpışma uyarıları ve acil fren bildirimleri anlık olarak komşu araçlara iletilerek kazalar önlenir.

IEEE 802.11p/WAVE gibi özel protokoller ve mekanizmalar, bu iletişimin temelini oluşturur.

### V2I (Vehicle-to-Infrastructure): Araçtan Altyapıya İletişim

V2I, araçlar ile yol kenarı altyapısı arasında bağlantı kurar. Bu iletişim türü, veri alışverişini kolaylaştırmak için yol kenarı üniteleri (RSU) ve trafik yönetim sistemleri ağından yararlanır.

Trafik ışığı optimizasyonu ve sürücülere gerçek zamanlı bilgi dağıtımı gibi uygulamaları destekleyerek etkin trafik yönetimine önemli katkı sağlar.

### V2P (Vehicle-to-Pedestrian): Araçtan Yayaya İletişim

Akıllı telefon veya giyilebilir cihazlar aracılığıyla yayaların GPS konum bilgisi ve hareket yönü araçlara kablosuz olarak iletilir. Bluetooth gibi teknolojiler ile yayalar ve araçlar arasında 50-150 metre menzilde iki yönlü iletişim sağlanır.

Bu sistem özellikle kör noktalardaki, kavşaklardaki veya araç arkasından yola çıkmaya çalışan yayaları tespit ederek sürücüye görsel ve sesli uyarı vererek trafik kazalarını azaltır.

### V2X (Vehicle-to-Everything): Her Şeye Bağlı Araç

V2X, tüm iletişim türlerini kapsayan genel terimdir. V2V, V2I, V2P ve diğer tüm iletişim türlerini kapsayan bütünleşik bir sistemdir. Araçların çevrelerindeki her varlıkla iletişim kurmasını sağlayarak tam bir bağlantılı ulaşım ekosistemi oluşturur.

## VANET Birimleri

Araç Ad-Hoc Ağlarının kapsamlı incelenmesi kapsamında, araç iletişim sistemlerinin karmaşık yapısını oluşturan temel bileşenleri analiz etmek büyük önem taşır. Bu ekosistemin merkezinde iki kritik unsur yer alır:

### Onboard Unit (OBU): Araç Üstü Birim

**On-Board Unit (OBU)**, araç içi iletişim ve veri işleme görevlerini üstlenen gömülü bir elektronik birimdir. VANET mimarisinin temel bileşenlerinden biri olan OBU, aracın sensörlerinden gelen verileri toplayarak işler ve diğer araçlar (V2V) veya yol kenarı üniteleri (RSU) ile kablosuz iletişim kurar.

**Kullanılan Teknolojiler:**
- IEEE 802.11p
- DSRC (Dedicated Short-Range Communications)
- LTE-V
- 5G

**Temel Bileşenler:**
- İşlemci (SoC veya MCU)
- Bellek
- Kablosuz iletişim modülü
- Güç yönetimi birimi

**OBU'nun Temel İşlevleri:**

1. **Veri Toplama:** CAN, LIN veya Ethernet üzerinden araç sensörlerinden gelen verileri okur
2. **İletişim:** Hücresel ağ (4G/5G), Wi-Fi veya DSRC aracılığıyla bulut sistemleriyle veya diğer araçlarla veri alışverişi yapar
3. **Konum Takibi:** GPS veya GNSS modülü ile aracın konum bilgisini sürekli olarak sağlar
4. **Veri İşleme:** Toplanan verileri yerel olarak işler, filtreler veya sıkıştırır
5. **Güvenlik:** Şifreleme, kimlik doğrulama ve güvenli güncelleme (OTA) mekanizmalarını destekler

### Roadside Unit (RSU): Yol Kenarı Birimi

**Roadside Unit (RSU)**, genellikle yol kenarlarına, kavşaklara veya otopark gibi stratejik noktalara yerleştirilen sabit iletişim birimleridir. RSU'lar, araçlar arası ağ ile (V2V) geniş ağ altyapısı arasında köprü görevi görür ve internet bağlantısı, güvenlik bilgileri ve trafik uyarıları sağlar.

**RSU'ların Üç Temel İşlevi:**

1. **Kapsama Alanını Genişletmek:** Uzak araçların da ağa dahil olmasını sağlar
2. **İnternet Erişimi Sağlamak:** Özellikle doğrudan V2V iletişimin mümkün olmadığı durumlarda
3. **Güvenlik Uygulamaları:** Düşük köprüler, kazalar veya yol bakım bölgeleri hakkında gerçek zamanlı uyarılar

**RSU Yapısının Avantajları:**
- Veri akışı çift yönlüdür; araçlardan gelen bilgiler merkeze iletilir, merkezden gönderilen uyarılar araçlara geri iletilir
- İletişim kapsama alanı genişler; uzak konumdaki araçlar RSU'lar üzerinden ağa bağlanabilir
- Gerçek zamanlı trafik yönetimi ve güvenlik uyarıları sağlanabilir

RSU'lar hem gateway hem de relay node olarak çalışarak VANET ekosisteminin omurgasını oluşturur.

## VANET Yönlendirme Protokolleri

VANET yapılarında yönlendirme protokolleri, araçlar ile RSU arasındaki veri iletiminin verimli, güvenilir ve düşük gecikmeli şekilde gerçekleşmesi açısından kritik bir rol oynar. Bu protokoller, ağ topolojisinin yüksek oranda dinamik olması, sınırlı bağlantı süresi, yüksek hız farklılıkları ve değişken ağ yoğunluğu gibi zorluklarla başa çıkacak şekilde tasarlanmıştır.

### VANET'e Özgü Zorluklar

VANET'ler yüksek mobiliteye, sık topoloji değişimlerine ve yoğun trafik ortamlarına sahip olduğu için klasik MANET (Mobile Ad-Hoc Network) protokolleri genellikle yeterli olmaz. Bu nedenle, VANET'e özel yönlendirme protokolleri geliştirilmiştir.

VANET yönlendirme protokolleri genel olarak işleyiş prensiplerine göre altı ana kategoriye ayrılır. Her kategori, belirli bir iletişim senaryosuna veya gereksinime uygun olarak optimize edilmiştir:

1. **Topoloji Tabanlı Protokoller:** Proaktif ve reaktif yönlendirme stratejileri
2. **Pozisyon Tabanlı Protokoller:** GPS konum bilgilerini kullanan protokoller
3. **Broadcast Tabanlı Protokoller:** Belirli bölgelere mesaj yayını
4. **Küme Tabanlı Protokoller:** Araçları gruplar halinde organize eden yaklaşımlar
5. **Geocast Protokoller:** Coğrafi bölgelere özel mesajlaşma
6. **Hibrit Protokoller:** Birden fazla yaklaşımı birleştiren protokoller

## Sonuç: VANET'in Geleceği

Vehicular Ad-Hoc Networks (VANET), akıllı ulaşım sistemlerinin temel taşı olarak ortaya çıkmıştır. Araçlar arası iletişimden altyapı entegrasyonuna, yayalarla etkileşimden her şeye bağlı araç konseptine kadar uzanan geniş bir yelpazede VANET teknolojisi, trafik güvenliğini artırma, trafik akışını optimize etme ve sürücü deneyimini iyileştirme potansiyeline sahiptir.

5G teknolojisinin yaygınlaşması, edge computing altyapısının gelişmesi ve yapay zeka algoritmalarının olgunlaşmasıyla birlikte VANET'in yetenekleri daha da artacaktır. Yakın gelecekte tamamen otonom araçların birbirleriyle kusursuz iletişim kurduğu, trafik kazalarının neredeyse sıfıra indiği ve şehir içi ulaşımın tamamen optimize edildiği bir dünya görebiliriz.

Bu teknolojinin başarısı, sadece teknik altyapının geliştirilmesine değil, aynı zamanda güvenlik standartlarının belirlenmesine, gizlilik endişelerinin giderilmesine ve küresel bir standardizasyonun sağlanmasına da bağlıdır. VANET, ulaşım sektöründeki dijital dönüşümün merkezinde yer almaya devam edecek ve akıllı şehirlerin vazgeçilmez bir parçası olacaktır.

---

*Bu yazı, modern ulaşım sistemlerinin geleceğini şekillendiren VANET teknolojisinin kapsamlı bir incelemesini sunmaktadır. Araç ağları, IoT (Nesnelerin İnterneti) ve akıllı şehir konseptleriyle birleşerek daha güvenli, verimli ve sürdürülebilir bir ulaşım ekosistemi oluşturmayı hedeflemektedir.*
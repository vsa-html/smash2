# 🔥 SMASH XSO — 9 Layer DDoS Ultimate

**SMASH** adalah alat uji penetrasi (penetration testing) yang dirancang untuk mensimulasikan serangan **DDoS** (Distributed Denial of Service) dengan 9 metode serangan berbeda, mencakup Layer 3 hingga Layer 7. Script ini dibuat hanya untuk tujuan edukasi dan pengujian keamanan pada sistem yang kamu miliki sendiri atau dengan izin tertulis dari pemilik sistem.

> ⚠️ PERINGATAN HUKUM:
Penggunaan tanpa izin adalah tindakan ilegal dan dapat dikenai sanksi pidana sesuai UU ITE dan peraturan perundang-undangan lainnya.
Penulis tidak bertanggung jawab atas segala bentuk penyalahgunaan alat ini.

---

## 🚀 Fitur Utama ##

• *9 Metode Serangan* — UDP Flood Ultimate, DNS Amplification, ICMP Flood, TCP SYN Flood, SSL Renegotiation, HTTP GET Flood, HTTP POST Flood, Slowloris.

• *Multi-threading* — Atur jumlah thread hingga ribuan.

• *Durasi Fleksibel* — Tentukan durasi serangan atau jalankan tanpa batas (unlimited).

• *Pilihan Metode Bebas* — Pilih satu metode, beberapa, atau jalankan semua secara acak.

• *ICMP Flood (Root)* — Mendukung serangan ICMP jika dijalankan sebagai root.

• *CTRL + C* — Menghentikan serangan cukup dengan menekan CTRL + C.

---

## 🆕 Update Terbaru ##

Menggantikan method **UDP FLOOD** yang lama dengan yang baru, bernama **UDP FLOOD ULTIMATE**

Kelebihan **UDP FLOOD ULTIMATE** sebagai berikut:

##

1. Payload Maksimal (65.500 bytes)
2. Burst 200 Paket per Loop
3. Socket Buffer 16MB
4. Pre-Generated Payload
5. Low Thread, High Impact
6. Bypass Rate Limiting
7. Amplifikasi Bandwidth
8. Bisa Dijalankan Tanpa Root
9. Efek Instan
10. Fokus ke Bandwidth

##

***KESIMPULAN***

UDP Flood Ultimate = Senjata pamungkas SMASH XSO.

• **Brutal** — Bandwidth target abis dalam detik

• **Efisien** — Thread sedikit, efek besar

• **Ringan** — HP gak lag

• **Cepat** — Efek instan

• **Simple** — Gak butuh root

• **Universal** — Bisa ke port UDP apa aja

##

Sebelum melakukan serangan, kini tersedia menu **CEK WEB** untuk menganalisis target terlebih dahulu. Fitur ini membantu pengguna memahami karakteristik target dan memilih metode yang paling efektif.

Fitur CEK WEB meliputi:

• **🔍 Deteksi Proteksi** — Mengidentifikasi apakah target dilindungi oleh Cloudflare, Vercel, Nginx, Apache, atau tanpa proteksi.

• **🌐 Analisis HTTP** — Menampilkan status code, server header, dan content-type target.

• **📡 Scan Port UDP** — Memeriksa port-port UDP penting seperti DNS (53), NTP (123), Memcached (11211), SNMP (161), LDAP (389), dan SSDP (1900).

• **💡 Rekomendasi Method** — Memberikan saran metode serangan yang paling cocok berdasarkan hasil analisis.

Dengan fitur ini, pengguna dapat melakukan rekognisi awal sebelum menentukan strategi pengujian — menjadikan SMASH XSO bukan sekadar alat serang, tapi juga alat analisis keamanan.

---

## 🛠️ Instalasi Keperluan ##

```bash
pkg update && pkg upgrade
pkg install python
pkg install git
pkg install openssl-tool
pip install requests
```

---

## 📁 Instalasi Git ##

```bash
git clone https://github.com/vsa-html/smash2.git
```

---

## 📱 Jalankan ##

```bash
cd smash2
python main.py
```

---

## 📦 Persyaratan ##

• Modul `requests`

• (Opsional) Hak akses root untuk ICMP Flood.

• Aplikasi `Termux`

----

## 📊 Peringkat Method ##

1. ***UDP Flood Ultimate*** `⭐⭐⭐⭐⭐`

Paling brutal buat server yang gak pake proteksi. Cukup 800–1200 thread, server langsung lumpuh dalam hitungan detik.

##

2. ***DNS Amplification*** `⭐⭐⭐⭐½`

Efek besar kalo target pake DNS. Bisa amplify traffic 30–60x lipat.

##

3. ***ICMP Flood*** `⭐⭐⭐⭐`

Bikin server kewalahan nanganin ping terus-menerus. Butuh root.

##

4. ***TCP SYN Flood*** `⭐⭐⭐⭐`

Bikin server kehabisan koneksi (half-open connections).

##

5. ***SSL Renegotiation*** `⭐⭐⭐½`

Lumayan buat server HTTPS, tapi butuh resource lebih.

##

6. ***HTTP Flood*** `⭐⭐⭐`

Sangat ganas buat web server. Memakan resource CPU & RAM target.

##

7. ***HTTP POST Flood*** `⭐⭐⭐`

Mirip HTTP Flood, tapi lebih berat di sisi server.

##

8. ***Slowloris*** `⭐⭐½`

Halus tapi mematikan. Bikin server kehabisan thread.

---

# 🎯 Rekomendasi Penggunaan #

Method yang gw saranin:

Web biasa `UDP Flood Ultimate` (nomor 1)

Kalo web pake Cloudflare `HTTP Flood` (nomor 6)

Servernya pake HTTPS `SSL` `Renegotiation` (nomor 5)

Servernya lemah `Slowloris` (nomor 8)

Server VPS biasa `DNS Amplification` (nomor 2)


---

> ⚠️Disclaimer

Script ini dibuat semata-mata untuk keperluan edukasi keamanan siber dan pengujian penetrasi dengan izin.
Penggunaan untuk menyerang, merusak, atau mengganggu layanan orang lain tanpa izin adalah melanggar hukum di banyak negara, termasuk Indonesia.
Penulis dan kontributor tidak bertanggung jawab atas segala konsekuensi yang timbul dari penyalahgunaan alat ini.

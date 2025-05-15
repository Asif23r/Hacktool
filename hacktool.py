import os
import socket
import requests
import random
import re
import hashlib
import smtplib
import platform
import subprocess
import zipfile
import time
import itertools
import string
from bs4 import BeautifulSoup
from datetime import datetime
from colorama import Fore, init

init(autoreset=True)

print(f"""{Fore.GREEN}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘
⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀
⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸
⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃
⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

print(f"""{Fore.YELLOW}
+--------------------------------------+
|  Instagram : @code_with_raaz._       |
|  Telegram  : @RaazXdev               |
|  GitHub    : @Asif23r                |
+--------------------------------------+
""")

# === TOOL 1: IP Location Tracker ===
def ip_location_tracker():
    ip = input("Enter target IP address (from logger): ")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        print("\n[✓] Location Details:")
        print(f"IP Address : {data.get('query')}")
        print(f"Country    : {data.get('country')}")
        print(f"Region     : {data.get('regionName')}")
        print(f"City       : {data.get('city')}")
        print(f"ISP        : {data.get('isp')}")
        print(f"Lat/Lon    : {data.get('lat')}, {data.get('lon')}")
        print(f"Timezone   : {data.get('timezone')}")
    except Exception as e:
        print(f"[-] Error: {e}")

# === TOOL 2: OSINT User Lookup ===
def osint_user_lookup():
    username = input("Enter username to search: ")
    platforms = {
        "Instagram": f"https://instagram.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://x.com/{username}"
    }
    for name, url in platforms.items():
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print(f"[+] Found on {name}: {url}")
            else:
                print(f"[-] Not found on {name}")
        except:
            print(f"[-] Error connecting to {name}")

# === TOOL 3: Wordlist Generator ===
def wordlist_generator():
    name = input("Enter name: ")
    dob = input("Enter birth year (YYYY): ")
    words = [
        name + dob,
        name + "@" + dob[-2:],
        name + "123",
        name.capitalize() + "!",
        name[::-1] + dob[-2:]
    ]
    with open("wordlist.txt", "w") as f:
        for w in words:
            f.write(w + "\n")
    print("[✓] Wordlist saved as 'wordlist.txt'")

# === TOOL 4: Port Scanner ===
def port_scanner():
    host = input("Enter target IP or domain: ")
    ports = [21,22,23,25,53,80,443,3306]
    print(f"\n[✓] Scanning {host}...")
    for port in ports:
        with socket.socket() as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            else:
                print(f"[-] Port {port} is closed")

# === TOOL 5: Fake IP Generator ===
def fake_ip_generator():
    ip = ".".join(str(random.randint(1,255)) for _ in range(4))
    print(f"[+] Generated fake IP: {ip}")

# === TOOL 6: Website Tester ===
def website_tester():
    url = input("Enter website URL (with http/https): ")
    try:
        r = requests.get(url, timeout=5)
        print(f"\n[✓] Status Code: {r.status_code}")
        print(f"[✓] Server: {r.headers.get('Server','Unknown')}")
        print(f"[✓] Content-Type: {r.headers.get('Content-Type','Unknown')}")
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.title.string if soup.title else 'N/A'
        print(f"[✓] Page Title: {title}")
    except Exception as e:
        print(f"[-] Error accessing site: {e}")

# === TOOL 7: Website Details Scraper ===
def website_details_scraper():
    url = input("Enter website URL (with http/https): ")
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.title.string if soup.title else 'N/A'
        print(f"\n[✓] Title: {title}")
        desc_tag = soup.find('meta', attrs={'name':'description'})
        description = desc_tag['content'] if desc_tag else 'N/A'
        print(f"[✓] Meta Description: {description}")
        h1s = soup.find_all('h1')
        h2s = soup.find_all('h2')
        print(f"\n[✓] H1 Headings ({len(h1s)}):")
        for i, h in enumerate(h1s,1):
            print(f"  {i}. {h.text.strip()}")
        print(f"\n[✓] H2 Headings ({len(h2s)}):")
        for i, h in enumerate(h2s,1):
            print(f"  {i}. {h.text.strip()}")
        links = soup.find_all('a', href=True)
        print(f"\n[✓] Total Links Found: {len(links)}")
        for i, l in enumerate(links[:20],1):
            print(f"  {i}. {l['href']}")
        if len(links) > 20:
            print(f"  ... and {len(links)-20} more links")
    except Exception as e:
        print(f"[-] Error accessing website: {e}")

# === TOOL 8: Port Banner Grabber ===
def port_banner_grabber():
    host = input("Enter target IP or domain: ")
    port = int(input("Enter port number: "))
    try:
        with socket.socket() as s:
            s.settimeout(3)
            s.connect((host, port))
            s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = s.recv(1024).decode(errors='ignore')
            print(f"\n[✓] Banner for {host}:{port}:\n{banner}")
    except Exception as e:
        print(f"[-] Could not grab banner: {e}")

# === TOOL 9: Hash Generator & Cracker ===
def hash_generator_and_cracker():
    choice = input("Choose (1) Generate Hash or (2) Crack Hash: ")
    if choice == '1':
        text = input("Enter text to hash: ")
        print(f"MD5    : {hashlib.md5(text.encode()).hexdigest()}")
        print(f"SHA1   : {hashlib.sha1(text.encode()).hexdigest()}")
        print(f"SHA256 : {hashlib.sha256(text.encode()).hexdigest()}")
    elif choice == '2':
        htype = input("Enter hash type (md5/sha1/sha256): ").lower()
        hvalue = input("Enter hash to crack: ").lower()
        if not os.path.exists("wordlist.txt"):
            print("[-] wordlist.txt not found. Generate it first.")
            return
        with open("wordlist.txt","r") as f:
            words = f.read().splitlines()
        for w in words:
            if htype == 'md5' and hashlib.md5(w.encode()).hexdigest() == hvalue:
                print(f"[✓] Cracked! Password: {w}")
                return
            if htype == 'sha1' and hashlib.sha1(w.encode()).hexdigest() == hvalue:
                print(f"[✓] Cracked! Password: {w}")
                return
            if htype == 'sha256' and hashlib.sha256(w.encode()).hexdigest() == hvalue:
                print(f"[✓] Cracked! Password: {w}")
                return
        print("[-] Password not found in wordlist.")
    else:
        print("[-] Invalid choice.")

# === TOOL 10: SMS BOMBER (DEMO ONLY) ===
def sms_bomber():
    print("Warning: This is a demo SMS bomber. Use responsibly and with permission!")
    phone = input("Enter target phone number (with country code): ")
    count = int(input("Enter number of messages to send: "))
    for i in range(count):
        print(f"[✓] Sending SMS {i+1} to {phone} (simulated)")
    print("[✓] Demo SMS bombing complete.")

# === TOOL 11: System Info Collector ===
def system_info_collector():
    print("\n[✓] Collecting system info...\n")
    print(f"Platform     : {platform.system()} {platform.release()}")
    print(f"Processor    : {platform.processor()}")
    try:
        uname = subprocess.check_output("uname -a", shell=True).decode().strip()
        print(f"Uname        : {uname}")
    except:
        pass
    print(f"Machine      : {platform.machine()}")
    print(f"Hostname     : {socket.gethostname()}")
    try:
        ip = socket.gethostbyname(socket.gethostname())
        print(f"Local IP     : {ip}")
    except:
        pass

# === TOOL 12: ZIP PASSWORD CRACKER ===
def raaz_zip_cracker():
    zip_path = input("Enter path to ZIP file: ")
    wordlist_file = "wordlist.txt"

    if not zipfile.is_zipfile(zip_path):
        print("[-] Not a valid ZIP file.")
        return

    if os.path.exists(wordlist_file):
        with open(wordlist_file, "r") as f:
            wordlist = [line.strip() for line in f.readlines()]
    else:
        wordlist = []

    with zipfile.ZipFile(zip_path) as zf:
        for pwd in wordlist:
            try:
                zf.extractall(pwd=pwd.encode())
                print(f"[✓] Password found from wordlist: {pwd}")
                return
            except:
                print(f"Trying wordlist password: {pwd}")

        print("[*] Password not found in wordlist, starting brute force (10 minutes max)...")

        chars = string.ascii_letters + string.digits + string.punctuation
        start_time = time.time()
        max_duration = 600

        for length in range(4, 8):
            for pwd_tuple in itertools.product(chars, repeat=length):
                if time.time() - start_time > max_duration:
                    print("[-] Time limit reached. Password not found.")
                    return
                pwd = ''.join(pwd_tuple)
                try:
                    zf.extractall(pwd=pwd.encode())
                    print(f"[✓] Password cracked by brute force: {pwd}")
                    with open(wordlist_file, "a") as f:
                        f.write(pwd + "\n")
                    return
                except:
                    print(f"Trying brute force password: {pwd}")

        print("[-] Password not found.")

# === MENU ===
def menu():
    while True:
        print(f"""{Fore.CYAN}
=========================
     RAAZX TOOLKIT      
  by @the_bot_developer
=========================
1) IP Location Tracker
2) OSINT User Scanner
3) Wordlist Generator
4) Port Scanner
5) Fake IP Generator
6) Website Tester
7) Website Details Scraper
8) Port Banner Grabber
9) Hash Generator & Cracker
10) SMS Bomber (Demo)
11) System Info Collector
12) ZIP Password Cracker
0) Exit
=========================
""")

        choice = input("Enter your choice: ")

        if choice == '1':
            ip_location_tracker()
        elif choice == '2':
            osint_user_lookup()
        elif choice == '3':
            wordlist_generator()
        elif choice == '4':
            port_scanner()
        elif choice == '5':
            fake_ip_generator()
        elif choice == '6':
            website_tester()
        elif choice == '7':
            website_details_scraper()
        elif choice == '8':
            port_banner_grabber()
        elif choice == '9':
            hash_generator_and_cracker()
        elif choice == '10':
            sms_bomber()
        elif choice == '11':
            system_info_collector()
        elif choice == '12':
            raaz_zip_cracker()
        elif choice == '0':
            print("[✓] Exiting. Stay ethical, hacker Raaz!")
            break
        else:
            print("[-] Invalid choice. Try again.")

if __name__ == "__main__":
    menu()

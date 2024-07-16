import json
import time
import sys
import atexit
import time
import os
import requests
import urllib.parse
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
import requests,os,sys, time
from time import strftime
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
import os,sys
import os
import requests
import urllib.parse
from time import strftime
import json
import atexit
import os
import json
import sys 
def vLongzZ():
	print('')
def vLongzZz():
	print('')
def vanlongzZ():
	print('')
def vanlongzZz():
	print('')
def api_fb():
	print('')
def api_cookie():
	print('')
def api_tds():
	print('')
def api_like():
	print('')
def api_camxuc():
	print('')
import requests

try:
    __check__ = requests.get(
        'https://raw.githubusercontent.com/VQAKDZ/ktoolvqak20/main/sever.txt').text
except:
    print('\033[1;39m Vui Lòng Kết Nối Mạng !')
    exit("")
if "off" in __check__:
    print(' \033[1;37m   ██╗░░██╗░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░')
    print(' \033[1;37m   ██║░██╔╝░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░')
    print(' \033[1;37m   █████═╝░█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░')
    print(' \033[1;37m   ██╔═██╗░╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░')
    print(' \033[1;37m   ██║░╚██╗░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗')
    print(' \033[1;37m   ╚═╝░░╚═╝░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝')
    print('  \033[1;37m           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('  \033[1;37m           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(' \033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = =')
    print(' \033[1;39m┌──────────────────────── ANH KHOA ─────────────────┐')
    print(' \033[1;32m║   \033[1;39m~[⟨⟩] ➩\033[0;31m ADMIN: \033[1;34mANH KHOA  ') 
    print(' \033[1;32m║   \033[1;39m~[⟨⟩] ➩ FACEBOOK: \033[1;34mVƯƠNG QUỐC ANH KHOA      ')  
    print(' \033[1;32m║   \033[1;39m~[⟨⟩] ➩ ZALO: \033[1;36m0363161335       ')             
    print(' \033[1;32m║   \033[1;39m~[⟨⟩] ➩ YOUTUBE: https://www.youtube.com/@anhkhoatool')
    print(' \033[1;39m└───────────────────────────────────────────────────┘')
    print('Sever Đang Bảo Trì Đợi Tí')
    exit("")
import json
import requests
import os
import urllib.parse
import atexit
from time import strftime, time
import hashlib
import random

KEYS_FILE = 'VQAK-keys.json'
EXPIRATION_SECONDS = 86400  # 24 hours in seconds

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def save_key_to_file(key, ip, creation_time, expiration_seconds, filename=KEYS_FILE):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
    else:
        data = {}

    data[ip] = {'key': key, 'creation_time': creation_time, 'expiration_seconds': expiration_seconds}

    with open(filename, 'w') as file:
        json.dump(data, file)

def load_key_from_file(ip, filename=KEYS_FILE):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return data.get(ip)
    return None

def is_key_expired(key_info):
    current_time = time()
    creation_time = key_info.get('creation_time', 0)
    expiration_seconds = key_info.get('expiration_seconds', EXPIRATION_SECONDS)
    return current_time - creation_time > expiration_seconds

def fetch_shortened_url(url, token):
    try:
        encoded_url = urllib.parse.quote(url)
        api_url = f'https://yeumoney.com/QL_api.php?token={token}&url={encoded_url}&format=json'
        response = requests.get(api_url)
        response.raise_for_status()
        result = response.json()
        if result["status"] == "success":
            return result["shortenedUrl"]
        else:
            return result["status"]
    except requests.exceptions.RequestException as e:
        return f"Error fetching shortened URL: {e}"

def fetch_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        ip = response.json()['ip']
        return ip
    except requests.exceptions.RequestException as e:
        return None

def generate_key(ip):
    if ip:
        key_base = ip + strftime('%d') + str(random.randint(1000, 9999))
        key = "VQAK-" + hashlib.sha256(key_base.encode()).hexdigest()[:16]  # Truncate to 16 characters
        return key
    return None

def display_banner(link_key, ip):
    banner = f'''
\033[1;39m        ██╗░░██╗░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░
\033[1;39m        ██║░██╔╝░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
\033[1;39m        █████═╝░█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░
  \033[1;39m      ██╔═██╗░╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;39m        ██║░╚██╗░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
\033[1;39m        ╚═╝░░╚═╝░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
  \033[1;39m             ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  \033[1;39m             ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
╔══════════════════════════════════════════════════════════╗
║ ~[⟨⟩] ➩ ADMIN:       ANH KHOA                            ║
║ ~[⟨⟩] ➩ FACEBOOK:    VƯƠNG QUỐC ANH KHOA                 ║
║ ~[⟨⟩] ➩ YOUTUBE:     https://www.youtube.com/@anhkhoatool║
║ ~[⟨⟩] ➩ ZALO:        0363161335                          ║
╚══════════════════════════════════════════════════════════╝
\033[1;34m= = = = = = = = = = = = = = = = = = = = = = = = = = = = =
\033[1;31mTHÔNG BÁO: TOOL HƠI LỎ NHƯNG MÀ NGON NÊN VƯỢT KEY XÀI ĐI!!!!
    \033[1;39m~[⟨⟩] ➩ ĐÂY LÀ TOOL FREE NÊN KEY SẼ THAY ĐỔI SAU 24H !!
    \033[1;39m~[⟨⟩] ➩ \u001b[32;1mLink lấy key: \033[1;33m{link_key}
    \033[1;39m~[⟨⟩] ➩ Địa chỉ IP của bạn: \033[1;31m{ip}
\u001b[31;1m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   \033[1;39mNhập Key để Vào Tool : '''
    print(banner)

def display_thank(VQAK):
    print(f"\n CẢM ƠN BẠN ĐÃ DÙNG TOOL CỦA {VQAK}! CHÚC BẠN MỘT NGÀY TỐT LÀNH!!")

def main():
    atexit.register(display_thank, "VQAK")
    clear_screen()

    ip = fetch_public_ip()
    if ip is None:
        print("Không thể lấy địa chỉ IP công cộng. Vui lòng kiểm tra kết nối internet của bạn.")
        return

    saved_key_info = load_key_from_file(ip)

    # Key được định nghĩa sẵn trong mã
    user_key = "khoai38373929274740208268"
    expiration_seconds = 3600  # Đặt thời gian hết hạn cho key (ví dụ: 1 giờ = 3600 giây)

    if saved_key_info and not is_key_expired(saved_key_info):
        print('\033[1;32m Key chính xác Đúng Chúc Bạn Ngày Tốt Lành')
    else:
        if saved_key_info and is_key_expired(saved_key_info):
            print('\033[1;31m Key đã hết hạn, vui lòng tạo key mới.')
        
        creation_time = time()
        url = f'https://vuongquocanhkhoakey.000webhostapp.com/key.html?key={user_key}'
        token_link1s = "baa2a5a08ef25aa3ff1e7708b69244c0378dc6a6ff412e4de7d3d7f705db62a6"
        link_key = fetch_shortened_url(url, token_link1s)

        if link_key.startswith("Error"):
            print(link_key)
            return

        display_banner(link_key, ip)
       
        while True:
            nhap_key = input().strip()

            if nhap_key == user_key:
                print('\033[1;32m Key chính xác Đúng Chúc Bạn Ngày Tốt Lành')
                save_key_to_file(nhap_key, ip, creation_time, expiration_seconds)
                break
            else:
                print('\033[1;31m Key Không Chính Xác, Bạn Chắc Chắn Đã Nhập Đúng Key?')
                print(f'\u001b[32;1m Link Lấy Key: \033[1;33m{link_key}')
                print('\033[1;39m------------------------------------------')
                print('   \033[1;32mNhập Key để Vào Tool : ', end='')

if __name__ == "__main__":
    main()  
#màu
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
#key tool
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
#MÀU
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#ĐÁNH DẤU BẢN QUYỀN
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"
thanh_xau=red+'['+vang+'⟨⟩'+red+'] '+trang+'➩ '+luc
thanh_dep=trang+'~'+red+'['+luc+'✓'+red+'] '+trang+'➩ '+luc
os.system("cls" if os.name == "nt" else "clear")
banner="""
\033[1;39m        ██╗░░██╗░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░
\033[1;39m        ██║░██╔╝░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
\033[1;39m        █████═╝░█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░
  \033[1;39m      ██╔═██╗░╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;39m        ██║░╚██╗░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
\033[1;39m        ╚═╝░░╚═╝░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
  \033[1;39m             ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  \033[1;39m             ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
╔══════════════════════════════════════════════════════════╗
║ ~[⟨⟩] ➩ ADMIN:       ANH KHOA                            ║
║ ~[⟨⟩] ➩ FACEBOOK:    VƯƠNG QUỐC ANH KHOA                 ║
║ ~[⟨⟩] ➩ YOUTUBE:     https://www.youtube.com/@anhkhoatool║
║ ~[⟨⟩] ➩ ZALO:        0363161335                          ║
╚══════════════════════════════════════════════════════════╝
\033[1;34m= = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00)
print("\033[1;31m THÔNG BÁO: \033[1;39mKEY THAY ĐỔI THEO IP ĐÃ VÀO ĐƯỢC TOOL THÌ ĐỪNG ĐỔI IP NHA!!")
print("\033[1;31m THÔNG BÁO: XÀI TOOL NẾU CÓ LỖI GÌ HÃY IB BÁO ADMIN")
print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══\x1b[1;91m══\033[1;32m══")
print(f"\x1b[38;5;226m[ NGÀY HÔM NAY LÀ ] : \x1b[38;5;46m{ngay_hom_nay}/{thang_nay}/{nam_}")
print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══\x1b[1;91m══\033[1;32m══")
def banner():
    print('\033[1;39m        ██╗░░██╗░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░')
    print('\033[1;39m        ██║░██╔╝░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░')
    print('\033[1;39m        █████═╝░█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░')
    print('  \033[1;39m      ██╔═██╗░╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░')
    print('\033[1;39m        ██║░╚██╗░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗')
    print('\033[1;39m        ╚═╝░░╚═╝░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝')
    print('\033[1;39m               ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('\033[1;39m               ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('╔══════════════════════════════════════════════════════════╗')
    print('║ ~[⟨⟩] ➩ ADMIN:       ANH KHOA                            ║')
    print('║ ~[⟨⟩] ➩ FACEBOOK:    VƯƠNG QUỐC ANH KHOA                 ║')
    print('║ ~[⟨⟩] ➩ YOUTUBE:     https://www.youtube.com/@anhkhoatool║')
    print('║ ~[⟨⟩] ➩ ZALO:        0363161335                          ║')
    print('╚══════════════════════════════════════════════════════════╝')
    print('\033[1;34m= = = = = = = = = = = = = = = = = = = = = = = = = = = = =')
# =======================[ NHẬP KEY ]=======================

# Tool names and URLs mapping
tool_urls = {
    '1': 'https://raw.githubusercontent.com/VQAKDZ/vqakktoolv20/main/srctdsfulljob.py',
    '2': 'https://raw.githubusercontent.com/VQAKDZ/vqakktoolv20/main/srctdsfblike.py',
    '3': 'https://raw.githubusercontent.com/VQAKDZ/vqakktoolv20/main/srctdstiktok.py',
    '4': 'https://raw.githubusercontent.com/VQAKDZ/vqakktoolv20/main/srcgetid.py',
    '5': 'https://raw.githubusercontent.com/VQAKDZ/vqakktoolv20/main/srcchecklive.py',
    '6': 'https://raw.githubusercontent.com/VQAKDZ/vqakktoolv20/main/srctoolnuoifb.py',
    '7': 'https://raw.githubusercontent.com/VQAKDZ/vqakktoolv20/main/srcgetcookie.py',
    '8': 'https://raw.githubusercontent.com/VQAKDZ/vqakktoolv20/main/srcspamsms.py',
    '9': 'https://raw.githubusercontent.com/VQAKDZ/vqakktoolv20/main/srcbuffviewtt.py'
}

tool_names = {
    '1': 'TDS CHẠY FULL JOB [VIP]',
    '2': 'TDS CHỈ CHẠY LIKE [VIP]',
    '3': 'TDS CHẠY TIKTOK [VIP]',
    '4': 'TOOL GET ID[VIP]',
    '5': 'TOOL CHECK LIVE UID [VIP]',
    '6': 'NUÔI ACC FACEBOOK [VIP]',
    '7': 'GET COOKIE TỪ TK MK [VIP]',
    '8': 'SPAM SMS [VIP]',
    '9': 'BUFF VIEW TIKTOK [VIP]'
}

def print_and_flush(msg):
    print(msg)
    sys.stdout.flush()

def thank_you_message(tool_name):
    print(f"\n\033[1;31m BẠN ĐÃ DỪNG TOOL {tool_name}!\033[0m")

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_external_ip():
    try:
        response = requests.get('http://httpbin.org/ip')
        if response.status_code == 200:
            ip_data = response.json()
            return ip_data['origin']
        else:
            print("\033[1;31mFailed to fetch external IP address")
    except requests.RequestException as e:
        print(f"\033[1;31mRequest error: {e}")
    return "Unknown"

def run_tool(chon):
    if chon not in tool_urls:
        print("\033[1;31mSAI LỰA CHỌN")
        print("\033[1;31mCOI CÓ SAI CHỖ NÀO KHÔNG")
        return
    
    tool_name = tool_names[chon]
    atexit.register(thank_you_message, tool_name)

    print_and_flush("\033[1;31mVui lòng chờ...")
    time.sleep(1)
    clear_console()
    print_and_flush(f"\033[1;31mĐANG VÀO TOOL {tool_name}... CHÚC BẠN MỘT NGÀY TỐT LÀNH!! ")

    url = tool_urls[chon]
    try:
        response = requests.get(url)
        if response.status_code == 200:
            exec(response.text)
        else:
            print(f"\033[1;31mFailed to fetch tool script from {url}")
    except requests.RequestException as e:
        print(f"\033[1;31mRequest error: {e}")

    input("\n\033[1;34mNhấn Enter để quay lại chọn công cụ...")
    clear_console()
    main_menu()

def main_menu():
    external_ip = get_external_ip()
    print(f"\n\033[1;39mIP HIỆN TẠI CỦA BẠN LÀ: \033[1;31m{external_ip}")
    print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══\x1b[1;91m══\033[1;32m══")

    while True:
        print('[\033[1;39mKhoa]➩ \033[1;39mNhập \033[1;39mSố [1] \033[1;32mTDS CHẠY FULL JOB [VIP]')
        print('[\033[1;39mKhoa]➩ \033[1;39mNhập \033[1;39mSố [2] \033[1;31mTDS CHỈ CHẠY LIKE [VIP]')
        print('[\033[1;39mKhoa]➩ \033[1;39mNhập \033[1;39mSố [3] \033[0;93mTDS CHẠY TIKTOK [VIP]')
        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══\x1b[1;91m══\033[1;32m══")
        print('[\033[1;39mKhoa]➩ \033[1;39mNhập \033[1;39mSố [4] \033[1;34mTOOL GET ID[VIP]')
        print('[\033[1;39mKhoa]➩ \033[1;39mNhập \033[1;39mSố [5] \033[1;35mTOOL CHECK LIVE UID [VIP]')
        print('[\033[1;39mKhoa]➩ \033[1;39mNhập \033[1;39mSố [6] \033[1;36mNUÔI ACC FACEBOOK [VIP]')
        print('[\033[1;39mKhoa]➩ \033[1;39mNhập \033[1;39mSố [7] \x1b[38;5;226mGET COOKIE TỪ TK MK [VIP]')
        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══\x1b[1;91m══\033[1;32m══")
        print('[\033[1;39mKhoa]➩ \033[1;39mNhập \033[1;39mSố [8] \033[0mSPAM SMS [VIP]')
        print('[Khoa]➩ Nhập \033[1;39mSố [9] BUFF VIEW TIKTOK [VIP]')


        chon = input('\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;37m: \033[1;33m')

        while chon not in tool_urls:
            print("\033[1;31mSai lựa chọn, vui lòng thử lại.")
            chon = input('\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;37m: \033[1;33m')

        run_tool(chon)

if __name__ == "__main__":
    main_menu()


import os

def clear_screen():
    # Check if the operating system is Windows
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# Call the function to clear the screen
api_fb()
vLongzZ()
vLongzZz()
vanlongzZ()
vanlongzZz()
api_fb()
api_cookie()
api_tds()
api_like()
api_camxuc()
clear_screen()
banner()
import requests, random, os, time
from bs4 import BeautifulSoup
list=[]
cookies=[]
def AddFriend(cookie, delay, add):
    count=0
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi',
        'cookie': cookie,
        'dpr': '1',
        'priority': 'u=0, i',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.172", "Google Chrome";v="124.0.6367.172", "Not-A.Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'viewport-width': '767',
    }
    access = requests.get('https://mbasic.facebook.com/friends/center/suggestions/', headers=headers).text
    find = BeautifulSoup(access, 'html.parser').find_all('a', href=lambda href: href and '/a/friends/add/?encrypted_id=' in href)
    print('Tìm Thấy ' + str(len(find)) + ' Bạn Bè Gợi Ý')
    if len(find) == 0:
        print('Tiến Hành Lấy Danh Sách ID')
        gioitinh = random.choice(['female', 'male'])
        ten = requests.get('https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/' + gioitinh).json()['data']['name']
        params = {
            'q': ten,
        }
        access = requests.get('https://mbasic.facebook.com/search/top/', params=params, headers=headers).text
        find = BeautifulSoup(access, 'html.parser').find_all('a', href=lambda href: href and '/profile.php?id=' in href)
        for i in find:
            id = i['href'].split('/profile.php?id=')[1].split('&')[0]
            list.append(id)
        for item in list[:]:
            if list.count(item) > 1:
                list.remove(item)
        print('Tìm Thấy ' + str(len(list)) + ' ID')
        for add in list:
            count += 1
            access = requests.get('https://mbasic.facebook.com/profile.php?id=' + add, headers=headers).text
            ten = access.split('<title>')[1].split('<')[0]
            nodeadd = access.split('/a/friends/profile/add/?subject_id=')[1].split('"')[0].replace('amp;', '')
            requests.get('https://mbasic.facebook.com/a/friends/profile/add/?subject_id=' + nodeadd, headers=headers)
            print(f'[{count}] | ADD FRIEND | {ten} | {add}')
            for i in range(delay,0,-1):
                print("Vui Lòng Đợi", i, "Giây                                         ", end=" \r")
                time.sleep(1)
            if count == add:
                break

def JoinGroup(cookie, delay, group):
    count=0
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi',
        'cookie': cookie,
        'dpr': '1',
        'priority': 'u=0, i',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.172", "Google Chrome";v="124.0.6367.172", "Not-A.Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'viewport-width': '767',
    }
    access = requests.get('https://mbasic.facebook.com/groups/?category=membership/', headers=headers).text
    find = BeautifulSoup(access, 'html.parser').find_all('a', href=lambda href: href and '/a/group/join/?button_id=' in href)
    print('Tìm Thấy ' + str(len(find)) + ' Nhóm Gợi Ý')
    for join in find:
        count += 1
        join = join['href'].replace("amp;", '').replace('"', '')
        id = join.split('group_id=')[1].split('&')[0]
        ten = requests.get('https://mbasic.facebook.com/groups/' + id, headers=headers).text.split('<title>')[1].split('<')[0]
        requests.get('https://mbasic.facebook.com' + join, headers=headers)
        print(f'[{count}] | JOIN GROUP | {ten} | {id} |')
        for i in range(delay,0,-1):
            print("Vui Lòng Đợi", i, "Giây                                         ", end=" \r")
            time.sleep(1)
        if count == group:
            break

def InteractionPost(cookie, delay, post):
    count=0
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi',
        'cookie': cookie,
        'dpr': '1',
        'priority': 'u=0, i',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.172", "Google Chrome";v="124.0.6367.172", "Not-A.Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'viewport-width': '767',
    }
    access = requests.get('https://mbasic.facebook.com/', headers=headers).text
    find_post = BeautifulSoup(access, 'html.parser').find_all('a', string='Toàn bộ tin')
    print('Tìm Thấy ' + str(len(find_post)) + ' Bài Viết')
    for link in find_post:
        count += 1
        nxt = link.find_previous_sibling('a')
        if nxt:
            id = nxt['href'].split('sid=')[1].split('&')[0]
            access = requests.get('https://mbasic.facebook.com/reactions/picker/?ft_id=' + id, headers=headers).text
            find = BeautifulSoup(access, 'html.parser').find_all('a', href=lambda href: href and '/ufi/reaction/?ft_ent_identifier=' in href)
            chon = random.choice(['LIKE', 'LOVE', 'TT', 'HAHA', 'WOW', 'SAD', 'ANGRY'])
            like = str(find[0]).split('<a href="')[1].split('"')[0].replace("amp;", '').replace('"', '')
            love = str(find[1]).split('<a href="')[1].split('"')[0].replace("amp;", '').replace('"', '')
            tt = str(find[2]).split('<a href="')[1].split('"')[0].replace("amp;", '').replace('"', '')
            haha = str(find[3]).split('<a href="')[1].split('"')[0].replace("amp;", '').replace('"', '')
            wow = str(find[4]).split('<a href="')[1].split('"')[0].replace("amp;", '').replace('"', '')
            sad = str(find[5]).split('<a href="')[1].split('"')[0].replace("amp;", '').replace('"', '')
            angry = str(find[6]).split('<a href="')[1].split('"')[0].replace("amp;", '').replace('"', '')
            if chon == 'LIKE':
                requests.get('https://mbasic.facebook.com/' + like, headers=headers)
                print(f'[{count}] Đã Thả Like Cho Bài Viết ' + id)
            if chon == 'LOVE':
                requests.get('https://mbasic.facebook.com/' + love, headers=headers)
                print(f'[{count}] Đã Thả Yêu Thích Cho Bài Viết ' + id)
            if chon == 'TT':
                requests.get('https://mbasic.facebook.com/' + tt, headers=headers)
                print(f'[{count}] Đã Thả Thương Thương Cho Bài Viết ' + id)
            if chon == 'HAHA':
                requests.get('https://mbasic.facebook.com/' + haha, headers=headers)
                print(f'[{count}] Đã Thả Haha Cho Bài Viết ' + id)
            if chon == 'WOW':
                requests.get('https://mbasic.facebook.com/' + wow, headers=headers)
                print(f'[{count}] Đã Thả Wow Cho Bài Viết ' + id)
            if chon == 'SAD':
                requests.get('https://mbasic.facebook.com/' + sad, headers=headers)
                print(f'[{count}] Đã Thả Sad Cho Bài Viết ' + id)
            if chon == 'ANGRY':
                requests.get('https://mbasic.facebook.com/' + angry, headers=headers)
                print(f'[{count}] Đã Thả Phẫn Nộ Cho Bài Viết ' + id)
            for i in range(delay,0,-1):
                print("Vui Lòng Đợi", i, "Giây                                         ", end=" \r")
                time.sleep(1)
        if count == post:
            break
print('Nhập [01] Để Nhập Cookie\nNhập [02] Để Lấy Cookie Từ File')
chon = input('Chọn ==> ')
if chon == '1':
    for i in range(99999):
        cookie = str(input(f'Nhập Cookie Thứ {i+1}: '))
        if cookie == "":
            break
        else:
            cookies.append(cookie)
elif chon == '2':
    file = input('Nhập File Chứa Cookie (Không Cần .txt): ').strip()
    with open(f"{file}.txt") as f:
        cookies = [line.strip() for line in f if line.strip()]
add = int(input('Nhập Số Lần Kết Bạn Gợi Ý: '))
group = int(input('Nhập Số Lần Tham Gia Nhóm Gợi Ý: '))
post = int(input('Nhập Số Lần Tương Tác Bài Viết: '))
delay = int(input('Nhập Delay: '))
if __name__ == "__main__":
    while True:
        for cookie in cookies:
            if cookie.strip() == "":
                continue
            id = cookie.strip().split('c_user=')[1].split(";")[0]
            print(f'Đang Chạy Uid: {id}')
            AddFriend(cookie.strip(), delay, add)
            JoinGroup(cookie.strip(), delay, group)
            InteractionPost(cookie.strip(), delay, post)
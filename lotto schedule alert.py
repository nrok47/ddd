import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime

import pandas as pd
import json
import csv
from google.oauth2 import service_account
import requests
import schedule
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

cookies = {
    'language': '1lKSZI3TjFZkJmBSB5kx7Auewvyu46hhbwMHEuhRbRX6%2FiQEGxgTZQMH1azoIPW6',
    'core-session': 'zz3K9Aw6rHD8S7hR2k0wDbbpgSW00Ho2J%2F%2BUKl%2F5DFVcJshB3IOIl2GosSG8jT4qvkZkwPJ9df3pVVAq8d4pYVLDnmFkwpqzjvzzNtYO5J1e2NJX8VUZ1E2t0i%2F8rfmU',
    'core-session-value': '32Fq6nwbgLs2piPwdnCZNVOHND8R4aeds4XYbj8q9g8%2Bv94MfG%2F11GPAE2CqxoqH1%2BgVzEClc7dmeqi3rH8vsqTwRpd3BMe%2BM4m0WnXRiCQpbRilry6r0dVIqgEF1sOV1sEN9E%2F2v2MJcXxiYm9jB7nGjJklZj1hjc5jbtCq1kgchj2BkzxedrONxCXC2Hw%2BlilqWzQcIB11PwNDbD59H6a7OyamUD9Gtz1521HcpL8vsozl%2FZyLG8wfjWwRRooajWp2uVNI6i8xRColGneoHkQ9F5QDb7ZsuWW1waAs13N%2BP256ndBdRG0h2s9H2GnhQHu6PPHqXmB3XOEx9ihoIA%3D%3D',
    'XSRF-TOKEN': 'ZPjZEyoN-iGzITJmCUmM8V2ZyUGG99PoGGCQ',
}

headers = {
    'authority': 'thailotto.io',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,th;q=0.8,ja;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'language=1lKSZI3TjFZkJmBSB5kx7Auewvyu46hhbwMHEuhRbRX6%2FiQEGxgTZQMH1azoIPW6; core-session=zz3K9Aw6rHD8S7hR2k0wDbbpgSW00Ho2J%2F%2BUKl%2F5DFVcJshB3IOIl2GosSG8jT4qvkZkwPJ9df3pVVAq8d4pYVLDnmFkwpqzjvzzNtYO5J1e2NJX8VUZ1E2t0i%2F8rfmU; core-session-value=32Fq6nwbgLs2piPwdnCZNVOHND8R4aeds4XYbj8q9g8%2Bv94MfG%2F11GPAE2CqxoqH1%2BgVzEClc7dmeqi3rH8vsqTwRpd3BMe%2BM4m0WnXRiCQpbRilry6r0dVIqgEF1sOV1sEN9E%2F2v2MJcXxiYm9jB7nGjJklZj1hjc5jbtCq1kgchj2BkzxedrONxCXC2Hw%2BlilqWzQcIB11PwNDbD59H6a7OyamUD9Gtz1521HcpL8vsozl%2FZyLG8wfjWwRRooajWp2uVNI6i8xRColGneoHkQ9F5QDb7ZsuWW1waAs13N%2BP256ndBdRG0h2s9H2GnhQHu6PPHqXmB3XOEx9ihoIA%3D%3D; XSRF-TOKEN=ZPjZEyoN-iGzITJmCUmM8V2ZyUGG99PoGGCQ',
    'referer': 'https://thailotto.io/member/lottery/yeekee',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

def yeekee_time_loop():
    current_time = datetime.now()
    print("this time is " + str(current_time))

def loop_get_name():
    first_round = 171
    this_round = int(get_round_yeekee())
    first_round = first_round + this_round +1
    if first_round >= 203 :
        first_round = first_round + 5

    url_lotto = 'https://thailotto.io/member/lottery/yeekee/{}'
    url_now = url_lotto.format(first_round)

    print(url_now)
    print("test GIThub")
    print("--------------  end loop ---------------")   

    #response = requests.get('https://thailotto.io/member/lottery/yeekee/172', cookies=cookies, headers=headers)
    response = requests.get(str(url_now), cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')

    for i in soup.find_all("div",{"nav-text"}):
        yee_round = i.get_text()
    print(yee_round)

    #find_16 = soup.find_all("a",{"text-danger btn-scroll"})
    for i in soup.find_all("a",{"text-primary btn-scroll"}):
        find_1 = i.get_text()
    for i in soup.find_all("a",{"text-danger btn-scroll"}):
        find_16 = i.get_text()
    for i in soup.find(href="?page=2&scrollToRow=50"):
        find_100 = i.get_text()    
        
    #print(find_100.strip())

    time.sleep(0.5)
    #all_s = [find_1.strip(),find_16.strip(),find_100.strip()]
    #print(all_s)
    
    find_1 = find_1.strip()
    find_16 = find_16.strip()
    find_100 = find_100.strip()
    print(" ลำดับ 1: " + find_1 + " / ลำดับ 16: " + find_16 +" / ลำดับ 100: "+ find_100)
    
    #lst_gen12 = "sam***_j7, gra***99, jas***rice1, haw***ur, Not***nk, two***phong67, sol***on, fer***ja, Mos***PaTiPan9, Fri***hip, bas***ab"
    lst_gen12 = "alu***d,way***d,sav***k50,hac***,pon***ba07,nat***it1199,Mov***aven,bac***s,sil***n,gra***99,boo***my,sso***ss,jat***9,Hok***do,Mon***za,Nav***4X,eld***orld,win***09,xik***4,not***0,noo***789,mom***199"


    token = "GVkgMapvmyx4de0mblxgx6f3NxTSC4MFQ7vTYwH57nR"
    uri = "https://notify-api.line.me/api/notify"
    header = {"Authorization": "Bearer "+token}
    #msg = {"message": "  "}
    #resp = requests.post(uri,headers=header,data=msg)
        
    if find_1 in lst_gen12 :
        yee_msg = yee_round + " => " + find_1 + " :ยิงเข้า 1"
        msg = {"message": yee_msg }
        resp = requests.post(uri,headers=header,data=msg)
        print("=> " + find_1 + " :ยิงเข้า 1")
    if find_16 in lst_gen12 :
        yee_msg = yee_round + " => " + find_16 + " :ยิงเข้า 16"
        msg = {"message": yee_msg }
        resp = requests.post(uri,headers=header,data=msg)
        print("=> " + find_16 + " :ยิงเข้า 16")
    if find_100 in lst_gen12 :
        yee_msg = yee_round + " => " + find_100 + " :ยิงเข้า 100"
        msg = {"message": yee_msg }
        resp = requests.post(uri,headers=header,data=msg)
        print("=> " + find_100 + " :ยิงเข้า 100")
    else : print(" หมดละ")

#### get round yeekeee ############
def get_round_yeekee():
    this_date = datetime.now()
    this_date_str = this_date.strftime("%Y-%m-%d")
    first_round_str = this_date_str +" 06:03:33"
    first_time_obj = datetime.strptime(first_round_str,"%Y-%m-%d %H:%M:%S")
    now_time = datetime.today()
    c = now_time - first_time_obj
    round_yeekee = c.total_seconds()
    num_round_yeekee = round(round_yeekee/900)
    #if num_round_yeekee > 203:
    #    num_round_yeekee_plus = num_round_yeekee + 6
    return(num_round_yeekee)
    
#start of methods


def job():
    loop_get_name()

schedule.every().day.at("06:03").do(job)
schedule.every().day.at("06:18").do(job)
schedule.every().day.at("06:33").do(job)
schedule.every().day.at("06:48").do(job)
schedule.every().day.at("07:03").do(job)
schedule.every().day.at("07:18").do(job)
schedule.every().day.at("07:33").do(job)
schedule.every().day.at("07:48").do(job)
schedule.every().day.at("08:03").do(job)
schedule.every().day.at("08:18").do(job)
schedule.every().day.at("08:33").do(job)
schedule.every().day.at("08:48").do(job)
schedule.every().day.at("09:03").do(job)
schedule.every().day.at("09:18").do(job)
schedule.every().day.at("09:33").do(job)
schedule.every().day.at("09:48").do(job)
schedule.every().day.at("10:03").do(job)
schedule.every().day.at("10:18").do(job)
schedule.every().day.at("10:33").do(job)
schedule.every().day.at("10:48").do(job)
schedule.every().day.at("11:03").do(job)
schedule.every().day.at("11:18").do(job)
schedule.every().day.at("11:33").do(job)
schedule.every().day.at("11:48").do(job)
schedule.every().day.at("12:03").do(job)
schedule.every().day.at("12:18").do(job)
schedule.every().day.at("12:33").do(job)
schedule.every().day.at("12:48").do(job)
schedule.every().day.at("13:03").do(job)
schedule.every().day.at("13:18").do(job)
schedule.every().day.at("13:33").do(job)
schedule.every().day.at("13:48").do(job)
schedule.every().day.at("14:03").do(job)
schedule.every().day.at("14:18").do(job)
schedule.every().day.at("14:33").do(job)
schedule.every().day.at("14:48").do(job)
schedule.every().day.at("15:03").do(job)
schedule.every().day.at("15:18").do(job)
schedule.every().day.at("15:33").do(job)
schedule.every().day.at("15:48").do(job)
schedule.every().day.at("16:03").do(job)
schedule.every().day.at("16:18").do(job)
schedule.every().day.at("16:33").do(job)
schedule.every().day.at("16:48").do(job)
schedule.every().day.at("17:03").do(job)
schedule.every().day.at("17:18").do(job)
schedule.every().day.at("17:33").do(job)
schedule.every().day.at("17:48").do(job)
schedule.every().day.at("18:03").do(job)
schedule.every().day.at("18:18").do(job)
schedule.every().day.at("18:33").do(job)
schedule.every().day.at("18:48").do(job)
schedule.every().day.at("19:03").do(job)
schedule.every().day.at("19:18").do(job)
schedule.every().day.at("19:33").do(job)
schedule.every().day.at("19:48").do(job)
schedule.every().day.at("20:03").do(job)
schedule.every().day.at("20:18").do(job)
schedule.every().day.at("20:33").do(job)
schedule.every().day.at("20:48").do(job)
schedule.every().day.at("21:03").do(job)
schedule.every().day.at("21:18").do(job)
schedule.every().day.at("21:33").do(job)
schedule.every().day.at("21:48").do(job)
schedule.every().day.at("22:03").do(job)
schedule.every().day.at("22:18").do(job)
schedule.every().day.at("22:33").do(job)
schedule.every().day.at("22:48").do(job)
schedule.every().day.at("23:03").do(job)
schedule.every().day.at("23:18").do(job)
schedule.every().day.at("23:33").do(job)
schedule.every().day.at("23:48").do(job)
schedule.every().day.at("00:03").do(job)
schedule.every().day.at("00:18").do(job)
schedule.every().day.at("00:33").do(job)
schedule.every().day.at("00:48").do(job)
schedule.every().day.at("01:03").do(job)
schedule.every().day.at("01:18").do(job)
schedule.every().day.at("01:33").do(job)
schedule.every().day.at("01:48").do(job)
schedule.every().day.at("02:03").do(job)
schedule.every().day.at("02:18").do(job)
schedule.every().day.at("02:33").do(job)
schedule.every().day.at("02:48").do(job)

    
while True:
    schedule.run_pending() # รันตารางเวลา
    time.sleep(1)

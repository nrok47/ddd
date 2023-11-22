# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime , timedelta
import io

import pandas as pd
import json
import csv
from google.oauth2 import service_account
import requests
import sys
from inputimeout import inputimeout, TimeoutOccurred
import array

cookies = {
    'language': '1lKSZI3TjFZkJmBSB5kx7Auewvyu46hhbwMHEuhRbRX6%2FiQEGxgTZQMH1azoIPW6',
    'core-session': 'zz3K9Aw6rHD8S7hR2k0wDbbpgSW00Ho2J%2F%2BUKl%2F5DFVcJshB3IOIl2GosSG8jT4qvkZkwPJ9df3pVVAq8d4pYVLDnmFkwpqzjvzzNtYO5J1e2NJX8VUZ1E2t0i%2F8rfmU',
    'core-session-value': '32Fq6nwbgLs2piPwdnCZNVOHND8R4aeds4XYbj8q9g8%2Bv94MfG%2F11GPAE2CqxoqH1%2BgVzEClc7dmeqi3rH8vsqTwRpd3BMe%2BM4m0WnXRiCQpbRilry6r0dVIqgEF1sOV1sEN9E%2F2v2MJcXxiYm9jB7nGjJklZj1hjc5jbtCq1kgchj2BkzxedrONxCXC2Hw%2BlilqWzQcIB11PwNDbD59H6a7OyamUD9Gtz1521HcpL8vsozl%2FZyLG8wfjWwRRooajWp2uVNI6i8xRColGneoHkQ9F5QDb7ZsuWW1waAs13N%2BP256ndBdRG0h2s9H2GnhQHu6PPHqXmB3XOEx9ihoIA%3D%3D',
    'XSRF-TOKEN': 'ZPjZEyoN-iGzITJmCUmM8V2ZyUGG99PoGGCQ',
    'charset': 'utf-8',
}
#encoode : utf-8
headers = {
    'authority': 'thailotto.io',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,th;q=0.8,ja;q=0.7',
    'cache-control': 'max-age=0',
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
    'charset': 'utf-8',
}


def substring_after(s, delim):
    return s.partition(delim)[2]

def yeekee_time_loop():
    current_time = datetime.now()
    print("this time is " + str(current_time))

def line_noti():
    print("test")

def loop_get_name():
    yee_round = str("a")
    #response = requests.get('https://thailotto.io/member/lottery/yeekee/172', cookies=cookies, headers=headers)
    response = requests.get(str(url_now), cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')#from_encoding="utf-8"
    #soup.prettify("utf-8")

#    for i in soup.find_all("div",{"nav-text"}):
#        yee_round = i.get_text()
#    print(yee_round)
    yee_r = soup.find("div",{"nav-text"})
    if yee_r is not None:
        yee_round = yee_r.get_text()

    find_1 = str("a")
    find_16 = str("a")
    find_100 = str("a")
    no_100 = str("a")
    i = str("1")
    #find_16 = soup.find_all("a",{"text-danger btn-scroll"})
    for i in soup.find_all("a",{"text-primary btn-scroll"}):
        find_1 = i.get_text()
    #find_1 = soup.find_all("a",{"text-primary btn-scroll"})
    for i in soup.find_all("a",{"text-danger btn-scroll"}):
        find_16 = i.get_text()
    #for i in soup.find(href="?page=2&scrollToRow=50"):
    #    find_100 = i.get_text()    
    no_100 = soup.find(href="?page=2&scrollToRow=50")
    if no_100 is not None:
        find_100 = no_100.get_text()    
    #find_100 = str("a")
    #find_100 = soup.find(href="?page=2&scrollToRow=50")
    #for i in soup.find(href="?page=2&scrollToRow=50"):
    #    if i is not None:
    #        find_100 = i.get_text()  
    #        print(find_100)
    #print(find_100.strip())
    #return(find_1,find_16,find_100)

    time.sleep(0.5)
    #all_s = [find_1.strip(),find_16.strip(),find_100.strip()]
    #print(all_s)
    
    find_1 = find_1.strip()
    find_16 = find_16.strip()
    find_100 = find_100.strip()
    print(" No1: " + find_1 + " / No16: " + find_16 +" / No100: "+ find_100)
    
   
    
    #lst_gen12 = "sam***_j7, gra***99, jas***rice1, haw***ur, Not***nk, two***phong67, sol***on, fer***ja, Mos***PaTiPan9, Fri***hip, bas***ab"
    lst_gen12 = "alu***d,way***d,sav***k50,hac***,pon***ba07,nat***it1199,Mov***aven,bac***s,sil***n,gra***99,boo***my,sso***ss,jat***9,Hok***do,Mon***za,Nav***4X,eld***orld,win***09,xik***4,not***0,noo***789,mom***199"

    #all_li = soup.find_all('li')
    #all_li = BeautifulSoup('<div class="no p-0 text-center"></div>','xml')
    #print(all_li)
    
    y= int(0)
    all_find_user = []
    for i in soup.findAll("div",{"username"}):
        #print(i)
        
        find_users = i.get_text()   
        find_users = find_users.strip()
        

        #find_nums = find_nums.gettext(soup.findAll("div",{"no p-0 text-center"}))
        y = y+1
        
        if find_users in lst_gen12 :
            #z = str(find_users)
            #all_find_user.append(find_users)
            #def get_find_user():    
            print(find_users + " Tee : "  + str(y))
            #return(find_users)
            kum_y = "อันดับ:" + str(y)  +"\n"
            merge_find_user = [find_users,kum_y]
            all_find_user.append(merge_find_user)
            #print(y)
        #print(find_users)
            
    #for i in range(len(all_find_user)): 
    #    print("{} : {}".format(i, all_find_user[i]))
    print(len(all_find_user))

    token = "GVkgMapvmyx4de0mblxgx6f3NxTSC4MFQ7vTYwH57nR"
    uri = "https://notify-api.line.me/api/notify"
    header = {"Authorization": "Bearer "+token}
    #msg = {"message": "  "}
    #resp = requests.post(uri,headers=header,data=msg)
        
    if find_1 in lst_gen12 :
        yee_msg = yee_round + " => " + find_1 + " :ยิงได้ที่ 1"
        msg = {"message": yee_msg }
        resp = requests.post(uri,headers=header,data=msg)
        print("=> " + find_1 + " :Ying 1")
    if find_16 in lst_gen12 :
        yee_msg = yee_round + " => " + find_16 + " :ยิงได้ที่ 16"
        msg = {"message": yee_msg }
        resp = requests.post(uri,headers=header,data=msg)
        print("=> " + find_16 + " :Ying 16")
    if find_100 in lst_gen12 :
        yee_msg = yee_round + " => " + find_100 + " :ยิงได้ที่ 100"
        msg = {"message": yee_msg }
        resp = requests.post(uri,headers=header,data=msg)
        print("=> " + find_100 + " :Ying 100")
    if True :
        yee_msg = " ---- yee KEE ----- "
        msg = {"message": yee_msg }
        resp = requests.post(uri,headers=header,data=msg)
        print("=> " + find_100 + " :Ying 100")
    if True:
        yee_msg = all_find_user
        msg = {"message": yee_msg }
        resp = requests.post(uri,headers=header,data=msg) 
        print("---------------close----------------------")
    return(find_1,find_16,find_100,all_find_user)


#### get round yeekeee ############
def get_round_yeekee():
    this_date = datetime.now()
    time_at_noon = datetime(2023,6,22,00,0,30,115421)
    this_date_str = this_date.strftime("%Y-%m-%d")
    first_round_str = this_date_str +" 06:03:33"
    first_time_obj = datetime.strptime(first_round_str,"%Y-%m-%d %H:%M:%S")
    now_time = datetime.today()

    if now_time < first_time_obj:
        first_time_obj = first_time_obj - timedelta(days=1)
    
    c = now_time - first_time_obj
        #print(first_time_obj)
    #print(c)
    round_yeekee = c.total_seconds()
    num_round_yeekee = round(round_yeekee/900)
    
    #if num_round_yeekee > 203:
    #    num_round_yeekee_plus = num_round_yeekee + 6
    #print("num" + str(num_round_yeekee))
    #print(type(num_round_yeekee))
    return(num_round_yeekee)
    
def compare_str():
    list_of_str = ["ddd","hello"," sam***_j7","san***e938"]
    #current_str = 


#start of methods
#this_rounds = get_round_yeekee.gettext()
#first_round = int(172) + get_round_yeekee() #buging time over at nigth 00.01 ++
first_round = int(172) + get_round_yeekee()
url_lotto = 'https://thailotto.io/member/lottery/yeekee/{}'
if first_round > 203 :
   first_round = first_round + 5

url_now = url_lotto.format(first_round)
print(url_now)

loop_get_name()

#time_ying = str("a")
#try:
#    time_ying = inputimeout(prompt='เวลายิง >>', timeout=10)
#except TimeoutOccurred:
#    time_ying = 'no input'

#og_sys = sys.stdout.read()

#filename = f"C:/xampp/htdocs/fastapi/scrap python/log_lotto/log_{datetime.now().strftime('%Y_%m_%d')}.log"
#with open(filename, "a+") as f:
    #f.write(url_now)
    #all_loop = loop_get_name()
    #time_lotto = input('input: ')
    #print(type(time_lotto))
    #all_ying = "เวลายิง = " + str(time_lotto)
    #print(all_ying)
    #f.write(f"\ntime_Ying = {loop_get_name()}")
    #f.write(f"\ntime to ying = {time_ying}")
    #f.write(f"\nJob Done @{datetime.now().strftime('%Y_%m_%d_%H:%M:%S')}")
    #f.write("\n<<----------------------------------------------------->>")


##<<<<<<<<<<<<<<<#old start of methods -----------------------------------------------------
#first_round = 172
#url_lotto = 'https://thailotto.io/member/lottery/yeekee/{}'
#for i in range(1,get_round_yeekee()):
#    url_now = url_lotto.format(first_round)    
#    if first_round == 203 :
#        first_round = first_round + 5
#        print(url_now)
#    loop_get_name()
#    first_round +=1
#    print("--------------  end loop ---------------")   
## -------------------------------------------------------------------------------------------->>>>>>>>>

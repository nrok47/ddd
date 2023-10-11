from selenium import webdriver
#from google import Create_Service


from oauth2client.service_account import ServiceAccountCredentials
import gspread

import sys
import datetime
from bs4 import BeautifulSoup
import datetime
from datetime import datetime
import locale
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import date
from selenium.common.exceptions import NoSuchElementException

import requests
####      selenium         #######
driver = webdriver.Chrome()
driver.get("https://thailotto.io/login")
login = driver.find_element("xpath",'/html/body/div[2]/a[1]')
login.click()
#chang3 --<
usernames = 'Mona1iza'
passwords = 'Ttt21345'
driver.find_element("xpath",'//*[@id="username"]').send_keys(usernames)
driver.find_element("xpath",'//*[@id="password"]').send_keys(passwords)
driver.find_element("xpath",'//*[@id="modal-login"]/div/div/form/div/div[4]/button').click()
total_money = driver.find_element("xpath",'/html/body/header/div/div[2]/a[1]/div').text
print(total_money)
total_money = total_money.replace(',', '')  # ลบเครื่องหมาย ,
total_money = float(total_money)
####### ------------------------- ######### -------------- get ค่าแนะนำ ------------- ####
#driver.find_element("xpath",'//*[@id="popup-dialog"]/div[1]/button').click()
try:
    element1 = driver.find_element("xpath", '//*[@id="popup-dialog"]/div[1]/button')
    element1.click()
except NoSuchElementException:
    pass
driver.find_element("xpath",'//*[@id="navbarNav"]/ul/li[7]/a').click() 
driver.find_element("xpath",'//*[@id="app"]/div[1]/div[1]/div[4]/div/a[3]').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

numbers = soup.find_all('li', class_='d-flex justify-content-between')

today = date.today()
output_day = today.day
if output_day in [1,2,3,4,5,6,7,8,9]:
    output_day = f"0{output_day}"
result = []
for number in numbers:
    text = number.get_text(strip=True)
    if "ตุลาคม" in text and "2566" in text:
        lines = text.splitlines()
        day = lines[0].strip()
        value = lines[3].strip().replace("2566", "")
        #print(type(day))
        if day == str(output_day) :
            result.append(f"{value}")

output = " | ".join(result)
output = output.replace(',', '')
output = float(output)
print(output)

### -------------- get ค่าแนะนำ ------------- ####
# Load credentials from the downloaded JSON file  https://docs.google.com/spreadsheets/d/19z7cN6LoPc3eC7SINLqQIzyGtvDl_eYg5aE1MApEvKI/edit#gid=1468127569
#scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive",
    ]

credentials = ServiceAccountCredentials.from_json_keyfile_name(r"C:\xampp\htdocs\fastapi\scrap python\get_money_key.json", scope)

# Authenticate and access the Google Sheets API
client = gspread.authorize(credentials)

# Open the spreadsheet by its title
spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/19z7cN6LoPc3eC7SINLqQIzyGtvDl_eYg5aE1MApEvKI/edit#gid=1468127569')

# Select a worksheet within the spreadsheet
worksheet = spreadsheet.sheet1

# Specify the values to be inserted
#values = ['Value 1', 'Value 2', 'Value 3']

# Append the values to the first column
#worksheet.append_row(values)

# Optional: Insert values in a specific range
# cell_list = worksheet.range('A1:A3')
# for i, cell in enumerate(cell_list):
#     cell.value = values[i]
# worksheet.update_cells(cell_list)


# Find the last row in the worksheet
last_row = len(worksheet.col_values(1)) + 1
#last_row_e = len(worksheet.col_values(1)) + 1

# Find the last row in the column
#chang1 --<
col_letter = 'I'  # The column letter you want to find the last row for
column_values = worksheet.col_values(ord(col_letter.lower()) - 96)  # Convert column letter to column index
last_row_ee = len(column_values) + 1
print(last_row_ee)

# Define the cell range for column E in the last row
cell_range = f"I{last_row_ee}" #chang2 --<

# Update the value in the specified cell range
worksheet.update(cell_range, total_money)

## --------------------------ลง ค่า แนะนำ ใน ชีท ------------------------------------##
# Find the last row in the worksheet
#last_row = len(worksheet.col_values(1)) + 1
#last_row_e = len(worksheet.col_values(1)) + 1

if total_money < 909 :
## ส่ง token line
    token = "GVkgMapvmyx4de0mblxgx6f3NxTSC4MFQ7vTYwH57nR"
    uri = "https://notify-api.line.me/api/notify"
    header = {"Authorization": "Bearer "+token}
    yee_msg = " ตัว => "+ str(usernames) + " เหลือ "+ str(total_money) 
    msg = {"message": yee_msg }
    esp = requests.post(uri,headers=header,data=msg)

# Find the last row in the column
#chang1 --<
col_letter = 'CP'  # The column letter you want to find the last row for
#column_values = worksheet.col_values(ord(col_letter.lower()) - 96)  # Convert column letter to column index
column_index = sum((ord(c) - 64) * (26 ** i) for i, c in enumerate(col_letter[::-1]))
column_values = worksheet.col_values(column_index)

#last_row_ee = len(column_values) + 1
#print(last_row_ee)
# Define the cell range for column E in the last row
cell_range_nn = f"CP{last_row_ee}" #chang2 --<

# Update the value in the specified cell range
worksheet.update(cell_range_nn, output)

driver.quit()
sys.exit()
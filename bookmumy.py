from selenium import webdriver
#from google import Create_Service

import sys
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import requests
####      selenium         #######
driver = webdriver.Chrome()
driver.get("https://thailotto.io/login")
login = driver.find_element("xpath",'/html/body/div[2]/a[1]')
login.click()
#chang3 --<
usernames = 'bookmumy'
passwords = 'Boomboy1234'
driver.find_element("xpath",'//*[@id="username"]').send_keys(usernames)
driver.find_element("xpath",'//*[@id="password"]').send_keys(passwords)
driver.find_element("xpath",'//*[@id="modal-login"]/div/div/form/div/div[4]/button').click()
total_money = driver.find_element("xpath",'/html/body/header/div/div[2]/a[1]/div').text
print(total_money)
total_money = total_money.replace(',', '')  # ลบเครื่องหมาย ,
total_money = float(total_money)
####### ------------------------- ######

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
col_letter = 'Q'  # The column letter you want to find the last row for
column_values = worksheet.col_values(ord(col_letter.lower()) - 96)  # Convert column letter to column index
last_row_ee = len(column_values) + 1
print(last_row_ee)

# Define the cell range for column E in the last row
cell_range = f"Q{last_row_ee}" #chang2 --<

# Update the value in the specified cell range
worksheet.update(cell_range, total_money)
if total_money < 909 :
## ส่ง token line
    token = "GVkgMapvmyx4de0mblxgx6f3NxTSC4MFQ7vTYwH57nR"
    uri = "https://notify-api.line.me/api/notify"
    header = {"Authorization": "Bearer "+token}
    yee_msg = " ตัว => "+ str(usernames) + " เหลือ "+ str(total_money) 
    msg = {"message": yee_msg }
    esp = requests.post(uri,headers=header,data=msg)
driver.quit()
sys.exit()
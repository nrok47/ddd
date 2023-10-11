from __future__ import unicode_literals
from selenium import webdriver
#from google import Create_Service

import sys
from oauth2client.service_account import ServiceAccountCredentials
import gspread

import datetime
from bs4 import BeautifulSoup
import datetime
from datetime import datetime, timedelta
import locale
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import date
from selenium.common.exceptions import NoSuchElementException

import requests
import time
import io

import pandas as pd
import json
import csv
from google.oauth2 import service_account

from inputimeout import inputimeout, TimeoutOccurred
import array

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

last_row = len(worksheet.col_values(1)) + 1
#last_row_e = len(worksheet.col_values(1)) + 1

# Find the last row in the column
#chang1 --<
col_letter = 'BI'  # The column letter you want to find the last row for
#column_values = worksheet.col_values(ord(col_letter.lower()) - 96)  # Convert column letter to column index
column_index = sum((ord(c) - 64) * (26 ** i) for i, c in enumerate(col_letter[::-1]))
column_values = worksheet.col_values(column_index)

last_row_ee = len(column_values)
print(last_row_ee)

# Define the cell range for column E in the last row
cell_range = f"CQ{last_row_ee}" #chang2 --<
print(cell_range)
# Update the value in the specified cell range
all_sum_ying = worksheet.get(cell_range)

# Get the current date and time
current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
cell_to_update = f"CT{last_row_ee}"
worksheet.update_acell(cell_to_update, current_datetime)

## ส่ง token line
token = "GVkgMapvmyx4de0mblxgx6f3NxTSC4MFQ7vTYwH57nR"
uri = "https://notify-api.line.me/api/notify"
header = {"Authorization": "Bearer "+token}
        
yee_msg = " กำไรรวมวันนี้ => " + str(all_sum_ying) + " บาท"
msg = {"message": yee_msg }
esp = requests.post(uri,headers=header,data=msg)
print("  => ok " )

print(all_sum_ying)

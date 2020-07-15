import os
import sys
import time

import pyautogui
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="Chromedriver's path"
)

# open Application
os.system("open /Applications/Google\ Chrome.app")

# open site
driver.get("https://web.whatsapp.com/")

time.sleep(4)

# send msg
Name = input("write Name or Group:")

time.sleep(2)

answer = input("Sure? Y/N:")
if answer == "Y":
    print("alright")
else:
    os.system("pkill Chrome")
    sys.exit

time.sleep(2)

driver.find_element_by_xpath("//span[@title='" + Name + "']").click()
f = open("Text", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

time.sleep(15)
# close Application
os.system("pkill Chrome")

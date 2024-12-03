from selenium import webdriver
from selenium.webdriver.common.by import By
import time
web = webdriver.Edge()
web.maximize_window()


try:
    with open("wordlist.txt","r") as file:
        contents = file.readlines()
        for line in contents:
            web.get("https://www.saucedemo.com/")
            web.find_element(By.ID,"user-name").send_keys(line.strip())
            web.find_element(By.ID,"password").send_keys(line.strip())
            web.find_element(By.ID,"login-button").click()
            time.sleep(2)
except:
    print("Some Error Occour")
    pass
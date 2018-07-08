# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 23:10:05 2018

@author: morim
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
from time import sleep


def sleep_scroll():
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def account_login():

    email= input("Your Email adress:")
    password= input("Your Password:")
    return email, password

if __name__ == '__main__': 
    
    email, password= account_login()
    
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://twitter.com/login")
    
    sleep(3)
    
    user_email = driver.find_element_by_css_selector("#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) > input")
    user_pass = driver.find_element_by_css_selector("#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input")
    user_email.send_keys(email)
    user_pass.send_keys(password)
    user_pass.send_keys(keys.ENTER)
    
    sleep(3)
    
    follower_click= driver.find_element_by_css_selector("#page-container > div.dashboard.dashboard-left > div.DashboardProfileCard.module > div > div.ProfileCardStats > ul > li:nth-child(3) > a > span.ProfileCardStats-statValue").click()
    
    for i in range(5):
        sleep_scroll()
    
    follower= driver.find_elements_by_css_selector("div > div > div.ProfileCard-userFields > div > div > a") 
    bio= driver.find_elements_by_css_selector("div > div > div.ProfileCard-userFields > p") 
    
    
    for i,(f,b) in enumerate(zip(follower,bio)):
        print("{}:".format(i+1))
        print(f.text)
        print(b.text)
        print("\n")
    
    driver.close()
                                                    
                                                    
                                                    
                                                    
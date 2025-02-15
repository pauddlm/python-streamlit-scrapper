from selenium import webdriver
import os

def driver_init():
    
    driver = webdriver.Chrome()

    driver.get(os.getenv("URL_TODOTEST"))

    return driver

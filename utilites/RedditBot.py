from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from utilites.TxtFileHelper import DeleteLineBreaks
from flask import render_template
import time
from .AccountCracker import wait_for_element

## post - comment
karma = []


class Website:
    def __init__(self, username, password, url):
        self.url = url
        self.username = username
        self.password = password

        # options = webdriver.ChromeOptions()
        # options.add_argument("headless")
        #self.driver = webdriver.Chrome("C:\\chromedriver.exe", options=options)
        self.driver = webdriver.Chrome("C:\\chromedriver.exe")
        self.driver.get(self.url)

    def login(self):
        wait_for_element(self.driver, "/html/body/div/div/div[2]/div/form/fieldset/input[1]")
        self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/form/fieldset/input[1]").clear()  # Empty the field
        self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/form/fieldset/input[1]").send_keys(self.username)
        self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/form/fieldset/input[2]").send_keys(self.password)
        self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/form/fieldset/button").click()


def run(username, password):
    web = Website(username, password)




import os
import logging
import requests
from selenium import webdriver
from stations import stations
import time

n_komnat = [1, 2, 3, 4, 5, 6, 7, 9]

def main():
    driver = webdriver.Chrome("/home/ni/Best_project/my_cian_parser/chromedriver.exe")
    for a in n_komnat:
        for i in range(1, 441):
            driver.get(f"https://www.cian.ru/export/xls/offers/?deal_type=sale&engine_version=2&foot_min=45&metro[0]={i}&object_type[0]=1&offer_type=flat&only_foot=2&room{a}=1")
            time.sleep(2)
    # n_rooms = driver.find_element_by_id("mainFilter_roomType")
    # n_rooms.click()
    # search = driver.find_element_by_id("geo-suggest-input")
    # search_button = driver.find_element_by_class_name("_93444fe79c--text--2P6bT")
    # for i in stations:
    #     search.send_keys(i)
    #     # print(f"Value is: метро {i}" % search.get_attribute("Value"))
    #     selecting_station = driver.find_element_by_class_name("_93444fe79c--relative--3lNYL")
    #     selecting_station.click()
    #     search_button.click()

if __name__ == "__main__":
    main()
# coding = utf-8
import requests
import time
from selenium import webdriver
d=webdriver.Edge()
time.sleep(1)
url='http://www.heibanke.com/lesson/crawler_ex01/'
playload={'username':'nihao'}
d.get(url)
for i in range(31):
    playload['password']=i
    print(str(playload))
    r=requests.post(url,data=playload)
    
    d.find_element_by_class_name("form-control").click()
    time.sleep(1)
    d.find_element_by_class_name("form-control").send_keys(playload['username'])
    time.sleep(1)
    d.find_element_by_id("id_password").send_keys(playload['password'])
    time.sleep(1)
    d.find_element_by_id("id_submit").click()
    time.sleep(1)
    if u"成功" in r.text:
        print(u'闯关成功!')
        break
    else:
        d.back()
        time.sleep(2)

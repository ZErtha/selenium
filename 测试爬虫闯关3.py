# coding = utf-8
import requests 
from time import sleep
from selenium import webdriver
from PIL import Image 
import pytesseract 

d=webdriver.Edge()

def run_url():
    url='http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/'
    d.get(url)
    sleep(1)
    d.find_element_by_id("id_register").click()

def run_url_zc():#注册窗口
    sleep(1)
    nic="qnizenmhuis"
    d.find_element_by_id("id_username").send_keys(nic)#点击昵称输入
    
    sleep(1)
    d.find_element_by_id("id_email").send_keys("1234567890@qq.com")#点击邮件输入
    
    sleep(1)
    mima='123456'
    d.find_element_by_id("id_password").send_keys(mima)#点击密码输入
    
    sleep(1)
    d.find_element_by_id("id_re_password").send_keys(mima)#点击重复密码输入

def run_yzm():#获取验证码
    d.save_screenshot('printscreen.png')
    imgelement=d.find_element_by_tag_name("img")
    location = imgelement.location#获取验证码x,y轴坐标
    size = imgelement.size#获取验证码的长宽
    rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
              int(location['y'] + size['height']))#写成我们需要截图的位置坐标
    i = Image.open("printscreen.png")#打开截图
    frame4 = i.crop(rangle)#使用Image的crop函数，从截图中再次截取我们需要的区域
    frame4.save('save.png')#保存我们接下来的验证码图片 进行打码time
    #这样获取到的图片就是验证码了，不过是最简单的那种还需要进行调整
    a=pytesseract.image_to_string(Image.open('save.png'))
    print(a)

    sleep(1)
    d.find_element_by_id("id_captcha_1").send_keys(a)#点击验证码输入框输入验证码
    sleep(1)
    d.find_element_by_class_name("btn btn-default").click()

def main():
    run_url()
    run_url_zc()
    run_yzm()

if __name__ == '__main__':
    main()

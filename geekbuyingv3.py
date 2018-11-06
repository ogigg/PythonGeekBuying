import requests
import json
import time
from adb.client import Client as AdbClient


client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("57e6b612")

file = open("dane.txt","w") 
with open(("konta.txt")) as f:
    line = f.readlines()
emails = [x.strip() for x in line] 
password=emails[0]
emails=emails[1:]
for email in emails:
        s = requests.Session()
        s.get('https://www.geekbuying.com/main/signin')

        auth = {
                'EmailAddress': email
                , 'PassWord': password
                , 'VerificationCode': ''
                }
        s.post('https://www.geekbuying.com/Main/AjaxSignIn', data=auth)
        promo = {'day': '7'}
        a=s.post('http://promotion.geekbuying.com/LuckyDraw/AddSigned', data=promo, timeout=1)
        print(email)
        print (a.content)
        file.write(email)
        file.write(": ")
        file.write(a.text)
        file.write("\n")
        time.sleep(2)
        device.shell("svc data disable")
        time.sleep(1)
        device.shell("svc data enable")
        time.sleep(6)
file.close() 

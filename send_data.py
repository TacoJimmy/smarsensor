import requests
import time
import get_data

def req_post():
    try:
        #get temperature
        cgpt_th = get_data.evi_th()
        value_temp = cgpt_th[0]
        url_temp = 'https://strawberry.cgptiot.com.tw/iot/Temperature.php?id=1680001-1&data='+str(value_temp)
        html = requests.post(url_temp)
        print(html.text)
        #get humidity
        value_humi = cgpt_th[1]
        url_humi = 'https://strawberry.cgptiot.com.tw/iot/Humidity.php?id=1680001-1&data='+str(value_humi)
        html = requests.post(url_humi)
        print(html.text)
        # get 乳液
        value_liquid = cgpt_th[2]
        url_humi = 'https://strawberry.cgptiot.com.tw/iot/HandLotion.php?id=1680001-1&data='+str(value_liquid)
        html = requests.post(url_humi)
        print(html.text)
        # get 廁所紙
        value_paper = cgpt_th[3]
        url_humi = 'https://strawberry.cgptiot.com.tw/iot/ToiletPaper.php?id=1680001-1&data='+str(value_paper)
        html = requests.post(url_humi)
        print(html.text)
        # get 人流
        value_human = cgpt_th[4]
        url_humi = 'https://strawberry.cgptiot.com.tw/iot/HumanTraffic.php?id=1680001&data='+str(value_human)
        html = requests.post(url_humi)
        print(html.text)
    except:
        #something error
        print('error')

if __name__ == '__main__':
    while True:
        req_post()
        time.sleep(120)
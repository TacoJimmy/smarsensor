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
    except:
        #something error
        print('error')

if __name__ == '__main__':
    while True:
        req_post()
        time.sleep(120)
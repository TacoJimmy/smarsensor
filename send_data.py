import requests
import time
import get_data

def req_post():
    try:
        cgpt_th = get_data.evi_th()
        temp_payload = {'data':30}
        html = requests.post('https://strawberry.cgptiot.com.tw/iot/Temperature.php?id=1680001-1',data = temp_payload)
        #humi_payload = {'data':cgpt_th[1]}
        #html = requests.post('https://strawberry.cgptiot.com.tw/iot/Humidity.php?id=1680001-1',data = humi_payload)
        
        print(html.text) 
    except:
        print('error')

if __name__ == '__main__':
    while True:
        req_post()
        time.sleep(10)
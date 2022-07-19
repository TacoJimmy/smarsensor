import requests
import time

def req_post():
    payload = {'data':60}
    html = requests.post('https://strawberry.cgptiot.com.tw/iot/Humidity.php?id=1680001-1',data = payload)
    print(html.text) 

if __name__ == '__main__':
    while True:
        req_post()
        time.sleep(10)
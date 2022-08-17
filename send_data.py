import requests
import time
import get_data
import schedule 


def req_post():
    try:
        #get temperature
        cgpt_th = get_data.evi_th()
        time.sleep(1)
        value_temp = cgpt_th[0]
        url_temp = 'https://strawberry.cgptiot.com.tw/iot/Temperature.php?id=1680001-1&data='+str(value_temp)
        html = requests.post(url_temp)
        print(value_temp)
        #get humidity
        value_humi = cgpt_th[1]
        url_humi = 'https://strawberry.cgptiot.com.tw/iot/Humidity.php?id=1680001-1&data='+str(value_humi)
        html = requests.post(url_humi)
        print(value_humi)
        # get 乳液
        value_liquid = cgpt_th[2]
        url_humi = 'https://strawberry.cgptiot.com.tw/iot/HandLotion.php?id=1680001-1&data='+str(value_liquid)
        html = requests.post(url_humi)
        print(value_liquid)
        # get 廁所紙
        value_paper = cgpt_th[3]
        url_humi = 'https://strawberry.cgptiot.com.tw/iot/ToiletPaper.php?id=1680001-1&data='+str(value_paper)
        html = requests.post(url_humi)
        print(value_paper)
        # get 人流
        value_human = get_data.clear_people_count
        url_humi = 'https://strawberry.cgptiot.com.tw/iot/HumanTraffic.php?id=1680001&data='+str(value_human)
        html = requests.post(url_humi)
        print(value_human)
        # get 無人
        '''
        value_people = cgpt_th[5]
        url_humi = 'https://strawberry.cgptiot.com.tw/iot/People.php?id=1680001-1&data='+str(value_people)
        html = requests.post(url_humi)
        '''
        #print(html.text)
        # get 臭味
        value_smelly = cgpt_th[6]
        url_humi = 'https://strawberry.cgptiot.com.tw/iot/Smelly.php?id=1680001-1&data='+str(value_smelly)
        html = requests.post(url_humi)
        print(value_smelly)
        print("Work Done")
    except:
        #something error
        print('error')

schedule.every(2).minutes.do(req_post)  
schedule.every(0.5).seconds.do(get_data.human_count)  

if __name__ == '__main__':
    while True:
        schedule.run_pending()  
        time.sleep(0.5)
        
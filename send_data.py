import requests
import time
import get_data
import schedule 

people_count = 0

def req_post():
    try:
        #get temperature
        cgpt_th = get_data.evi_th()
        time.sleep(1)
        value_temp = round(cgpt_th[0],1)
        url_temp = 'https://strawberry.cgptiot.com.tw/iot/Temperature.php?id=1680001-1&data='+str(value_temp)
        html = requests.post(url_temp)
        #print(value_temp)
        #get humidity
        value_humi = round(cgpt_th[1],1)
        url_humi = 'https://strawberry.cgptiot.com.tw/iot/Humidity.php?id=1680001-1&data='+str(value_humi)
        html = requests.post(url_humi)
        #print(value_humi)
        # get 乳液
        value_liquid = round(cgpt_th[2],1)
        url_humi = 'https://strawberry.cgptiot.com.tw/iot/HandLotion.php?id=1680001-1&data='+str(value_liquid)
        html = requests.post(url_humi)
        #print(value_liquid)
        # get 廁所紙
        value_paper = round(cgpt_th[3],1)
        url_humi = 'https://strawberry.cgptiot.com.tw/iot/ToiletPaper.php?id=1680001-1&data='+str(value_paper)
        html = requests.post(url_humi)
        #print(value_paper)
        # get 人流
        value_human = clear_people_count()
        url_humi = 'https://strawberry.cgptiot.com.tw/iot/HumanTraffic.php?id=1680001&data='+str(value_human)
        html = requests.post(url_humi)
        #print(value_human)
        # get 無人
        '''
        value_people = cgpt_th[5]
        url_humi = 'https://strawberry.cgptiot.com.tw/iot/People.php?id=1680001-1&data='+str(value_people)
        html = requests.post(url_humi)
        '''
        #print(html.text)
        # get 臭味
        value_smelly = round(cgpt_th[6],1)
        url_humi = 'https://strawberry.cgptiot.com.tw/iot/Smelly.php?id=1680001-1&data='+str(value_smelly)
        html = requests.post(url_humi)
        #print(value_smelly)
        print("Work Done")
    except:
        #something error
        print('error')



def human_count():
    global people_count
    people_statu = get_data.get_people()
    try:
        if people_statu >= 1000:
                people_count+=1
                time.sleep(2)
        #print (people_count)
        return people_count
    except:
        pass

def clear_people_count():
    global people_count
    
    total_count = people_count
    
    people_count = 0
    return total_count


def check_tissue():
    try:
        tissue_statu = get_data.get_tissue()
        if tissue_statu >= 1000:
            url_tissue = 'https://strawberry.cgptiot.com.tw/iot/ToiletPaper.php?id=1680001-1&data='+str(tissue_statu)
            html = requests.post(url_tissue)
    except:
        pass

def check_HandLotion():
    try:
        HandLotion_statu = get_data.get_HandLotion()
        if HandLotion_statu <= 500:
            #url_HandLotion = 'https://strawberry.cgptiot.com.tw/iot/HandLotion.php.php?id=1680001-1&data='+str(HandLotion_statu)
            url_HandLotion = 'https://strawberry.cgptiot.com.tw/iot/HandLotion.php?id=1680001-1&data='+str(HandLotion_statu)
            html = requests.post(url_HandLotion)
            print (html)
        print ("for check")
        print (HandLotion_statu)
    except:
        pass

schedule.every(2).minutes.do(req_post) 
schedule.every(1).seconds.do(human_count)
schedule.every(5).seconds.do(check_tissue)
schedule.every(5).seconds.do(check_HandLotion)  

if __name__ == '__main__':
    while True:
        schedule.run_pending()  
        time.sleep(0.1)
        
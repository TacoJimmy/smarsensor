import time
import serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

people_count = 0

def evi_th():
    evi_th_value = [0,0,0,0,0,0,0]
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port='/dev/ttyS1', baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
        master.set_timeout(5.0)
        master.set_verbose(True)
        evi_th_data = master.execute(1, cst.READ_INPUT_REGISTERS, 1, 2) #0溫度 1濕度
        time.sleep(2)
        evi_wc_data01 = master.execute(2, cst.READ_HOLDING_REGISTERS, 1, 3) #1無人 # 2臭味 3乳液
        time.sleep(2)
        evi_wc_data02 = master.execute(3, cst.READ_HOLDING_REGISTERS, 2, 2) # 2廁所紙 3人流
        time.sleep(2)
        
        evi_th_value[0] = evi_th_data[0]*0.1 #溫度
        evi_th_value[1] = evi_th_data[1]*0.1 #濕度
        evi_th_value[2] = evi_wc_data01[2]   #乳液
        evi_th_value[3] = evi_wc_data02[0]   #廁所紙
        evi_th_value[4] = evi_wc_data02[1]   #人流
        evi_th_value[5] = evi_wc_data01[0]   #無人
        evi_th_value[6] = evi_wc_data01[1]   #臭味
        time.sleep(0.5)
    except:
        evi_th_value = [0,0,0,0,0,0,0]

    return (evi_th_value)
    #return (evi_wc_data01)

def get_people():
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port='/dev/ttyS1', baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
        master.set_timeout(5.0)
        master.set_verbose(True)
        evi_th_data = master.execute(3, cst.READ_HOLDING_REGISTERS, 3, 1)
        return (evi_th_data[0])
    except:
        pass
    
    

def get_tissue():
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port='/dev/ttyS1', baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
        master.set_timeout(5.0)
        master.set_verbose(True)
        evi_th_data = master.execute(3, cst.READ_HOLDING_REGISTERS, 2, 1)
        return (evi_th_data[0])
    except:
        pass
    
    

def get_HandLotion():
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port='/dev/ttyS1', baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
        master.set_timeout(5.0)
        master.set_verbose(True)
        evi_th_data = master.execute(2, cst.READ_HOLDING_REGISTERS, 3, 1)
        return (evi_th_data[0])
    except:
        pass
    
    

def get_people():
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port='/dev/ttyS1', baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
        master.set_timeout(5.0)
        master.set_verbose(True)
        evi_th_data = master.execute(3, cst.READ_HOLDING_REGISTERS, 3, 1)
        return (evi_th_data[0])
    except:
        pass
    
    


if __name__ == '__main__':
    while True:
        th_data = evi_th()
        
        print (th_data)
        time.sleep(2)
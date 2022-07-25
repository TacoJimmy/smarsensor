import time
import serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

def evi_th():
    evi_th_value = [0,0,0,0,0]
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port='/dev/ttyS1', baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
        master.set_timeout(5.0)
        master.set_verbose(True)
        evi_th_data = master.execute(1, cst.READ_INPUT_REGISTERS, 1, 2)
        time.sleep(2)
        evi_wc_data01 = master.execute(2, cst.READ_HOLDING_REGISTERS, 2, 1)
        time.sleep(2)
        evi_wc_data02 = master.execute(3, cst.READ_HOLDING_REGISTERS, 2, 2)
        time.sleep(2)
        evi_th_value[0] = evi_th_data[0]*0.1
        evi_th_value[1] = evi_th_data[1]*0.1
        evi_th_value[2] = evi_wc_data01[0]
        evi_th_value[3] = evi_wc_data02[0]
        evi_th_value[4] = evi_wc_data02[1]

        time.sleep(0.5)
    except:
        evi_th_value = [0,0,0,0,0]

    return (evi_th_value)

if __name__ == '__main__':
    while True:
        th_data = evi_th()
        
        print (th_data)
        time.sleep(10)
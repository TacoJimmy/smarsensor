import time
import serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

def evi_th():
    master = modbus_rtu.RtuMaster(serial.Serial(port='/dev/ttyS1', baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
    master.set_timeout(5.0)
    master.set_verbose(True)
    evi_th_data = master.execute(1, cst.READ_HOLDING_REGISTERS, 1, 2)
    time.sleep(0.5)

    return evi_th_data

if __name__ == '__main__':
    while True:
        th_data = evi_th()
        
        print (th_data)
        time.sleep(120)
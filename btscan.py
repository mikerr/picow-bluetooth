import bluetooth
import binascii
import time

_IRQ_SCAN_RESULT = const(5)
devices = {}

def bt_irq(event, data):
    if event == _IRQ_SCAN_RESULT:        
        addr_type, addr, connectable, rssi, adv_data = data
        address = binascii.hexlify(addr).decode()
        devices[address] = rssi

ble = bluetooth.BLE() 
ble.active('active')
ble.irq(bt_irq)
ble.gap_scan(2000,100)
time.sleep(2)
print (devices)

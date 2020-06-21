import psutil
from w3mo import w3mo
import time
w3mo_name ="W3moCharger"
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
if plugged==False: plugged="Not Plugged In"
else: plugged="Plugged In"
print(percent+'% | '+plugged)

if percent < str('20'):
    print("less then 20%, lets start charging")
    x = w3mo.discover(return_type=dict)
    x = w3mo.discover(return_type=list)
    devices = w3mo.discover(return_type=list)
    device = devices[0]['obj']
    print("Device Name = {}".format(device.name))
    print("Device State = {}".format(device.state))
    
    if device.name == w3mo_name :
        device.set_state(1)
    else:
        print("w3mo ("+w3mo_name+") not found")
if percent >= str('21'):
    print("Higher then 21%, lets stop charging")
    x = w3mo.discover(return_type=dict)
    x = w3mo.discover(return_type=list)
    devices = w3mo.discover(return_type=list)
    device = devices[0]['obj']
    print("Device Name = {}".format(device.name))
    print("Device State = {}".format(device.state))
    
    if device.name == w3mo_name :
        device.set_state(0)
    else:
        print("w3mo ("+w3mo_name+") not found")

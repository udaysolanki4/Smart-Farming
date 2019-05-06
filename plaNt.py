
import RPi.GPIO as r
import serial as s
import time
import firebase from firebase
firebase=firebase.FirebaseApplication('Enter Firebase API')

r.setmode(r.BCM)
r.setup(21, r.IN)
while True:
    import Adafruit_DHT as d
    h,t=d.read_retry(d.DHT11,4)
    r1=str(t)
    r2=str(h) 
    d1=r.input(21)
    print d1
    firebase.put('node name',"atm humidity",r2)
    firebase.put('node name',"atm temp",r1)
    if d1==0:
        firebase.put('node name',"soil moisture","detected")
    else:
        firebase.put('node name',"soil moisture","not detected")
    print(r1)
    print(r2)
    time.sleep(1)
r.setup(17,r.OUT)
r.output(17,0)


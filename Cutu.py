from operator import truediv
from os import uname_result
from sre_constants import JUMP
import time
from turtle import distance
from adafruit_servokit import ServoKit
import board
import digitalio

pompa = digitalio.DigitalInOut(board.D22)
pompa.direction = digitalio.Direction.OUTPUT
pompa.value = True

touch = digitalio.DigitalInOut(board.D4)
touch.direction = digitalio.Direction.INPUT

disttrig = digitalio.DigitalInOut(board.D17)
disttrig.direction = digitalio.Direction.OUTPUT

distecho = digitalio.DigitalInOut(board.D27)
distecho.direction = digitalio.Direction.INPUT

disttrig.value = False


kit = ServoKit(channels=16)

timp = 0.1
schema = 0.01
merg = 0.1

umr_spt_dr = 8
umr_spt_st = 7
umr_fat_dr = 9
umr_fat_st = 6

cot_spt_dr = 13
cot_spt_st = 3
cot_fat_dr = 12
cot_fat_st = 2

glz_spt_dr = 15
glz_fat_st = 1
glz_fat_dr = 14
glz_spt_st = 0

dance_speed = 2


def dance():
    a=1
    for a in range(1, 21, dance_speed):
        kit.servo[umr_spt_dr].angle = 90-a
        time.sleep(schema)
        kit.servo[umr_spt_st].angle = 100-a
        time.sleep(schema)
        kit.servo[umr_fat_dr].angle = 100+a
        time.sleep(schema)
        kit.servo[umr_fat_st].angle = 90+a
        time.sleep(schema)
    time.sleep(0.2)


    for i in range(10):
     for j in range(1, 41, dance_speed):
        kit.servo[umr_spt_dr].angle = 70+j
        time.sleep(schema)
        kit.servo[umr_spt_st].angle = 80+j
        time.sleep(schema)
        kit.servo[umr_fat_dr].angle = 120-j
        time.sleep(schema)
        kit.servo[umr_fat_st].angle = 110-j
     time.sleep(0.2)
     j=1
     for j in range(1, 41, dance_speed):
        kit.servo[umr_spt_dr].angle = 110-j
        time.sleep(schema)
        kit.servo[umr_spt_st].angle = 120-j
        time.sleep(schema)
        kit.servo[umr_fat_dr].angle = 80+j
        time.sleep(schema)
        kit.servo[umr_fat_st].angle = 70+j
     time.sleep(0.2)


    a=1
    for a in range(1, 21, 2):
        kit.servo[umr_spt_dr].angle = 70+a
        time.sleep(schema)
        kit.servo[umr_spt_st].angle = 80+a
        time.sleep(schema)
        kit.servo[umr_fat_dr].angle = 120-a
        time.sleep(schema)
        kit.servo[umr_fat_st].angle = 110-a
        time.sleep(schema)



def walk():

     kit.servo[cot_fat_dr].angle = 150
     time.sleep(merg)
     kit.servo[glz_fat_dr].angle = 150
     time.sleep(merg)
 
     kit.servo[glz_spt_st].angle = 160
     time.sleep(merg)
     kit.servo[cot_spt_st].angle = 100
     time.sleep(merg)
     kit.servo[glz_spt_st].angle = 100
     time.sleep(merg)

     kit.servo[cot_fat_st].angle = 40
     time.sleep(merg)
     kit.servo[glz_fat_st].angle = 40
     time.sleep(merg)

     kit.servo[glz_spt_dr].angle = 30
     time.sleep(merg)
     kit.servo[cot_spt_dr].angle = 100
     time.sleep(merg)
     kit.servo[glz_spt_dr].angle = 100
     time.sleep(merg)

     kit.servo[glz_fat_dr].angle = 120
     time.sleep(merg)
     kit.servo[cot_fat_dr].angle = 120
     time.sleep(merg)

     kit.servo[glz_fat_st].angle = 70
     time.sleep(merg)
     kit.servo[cot_fat_st].angle = 70
     time.sleep(merg)  

     kit.servo[cot_spt_st].angle = 120
     time.sleep(merg)
     kit.servo[glz_spt_st].angle = 120
     time.sleep(merg)

     kit.servo[cot_spt_dr].angle = 70
     time.sleep(merg)
     kit.servo[glz_spt_dr].angle = 70
     time.sleep(merg)   

def stanga():
     kit.servo[cot_fat_dr].angle = 140
     time.sleep(merg)
     kit.servo[glz_fat_dr].angle = 140
     time.sleep(merg)

     kit.servo[cot_fat_st].angle = 50
     time.sleep(merg)
     kit.servo[glz_fat_st].angle = 50
     time.sleep(merg)

     kit.servo[glz_spt_dr].angle = 30
     time.sleep(merg)
     kit.servo[cot_spt_dr].angle = 100
     time.sleep(merg)
     kit.servo[glz_spt_dr].angle = 100
     time.sleep(merg)

     kit.servo[glz_fat_dr].angle = 120
     time.sleep(merg)
     kit.servo[cot_fat_dr].angle = 120
     time.sleep(merg)

     kit.servo[glz_fat_st].angle = 70
     time.sleep(merg)
     kit.servo[cot_fat_st].angle = 70
     time.sleep(merg)  

     kit.servo[cot_spt_dr].angle = 70
     time.sleep(merg)
     kit.servo[glz_spt_dr].angle = 70
     time.sleep(merg) 

def dreapta():
     kit.servo[cot_fat_dr].angle = 140
     time.sleep(merg)
     kit.servo[glz_fat_dr].angle = 140
     time.sleep(merg)
 
     kit.servo[glz_spt_st].angle = 160
     time.sleep(merg)
     kit.servo[cot_spt_st].angle = 100
     time.sleep(merg)
     kit.servo[glz_spt_st].angle = 100
     time.sleep(merg)

     kit.servo[cot_fat_st].angle = 50
     time.sleep(merg)
     kit.servo[glz_fat_st].angle = 50
     time.sleep(merg)


     kit.servo[glz_fat_dr].angle = 120
     time.sleep(merg)
     kit.servo[cot_fat_dr].angle = 120
     time.sleep(merg)

     kit.servo[glz_fat_st].angle = 70
     time.sleep(merg)
     kit.servo[cot_fat_st].angle = 70
     time.sleep(merg)  

     kit.servo[cot_spt_st].angle = 120
     time.sleep(merg)
     kit.servo[glz_spt_st].angle = 120
     time.sleep(merg)

def default():
    kit.servo[umr_spt_dr].angle = 90
    time.sleep(timp)
    kit.servo[umr_spt_st].angle = 117
    time.sleep(timp)
    kit.servo[umr_fat_dr].angle = 100
    time.sleep(timp)
    kit.servo[umr_fat_st].angle = 90

    time.sleep(timp)
    kit.servo[cot_spt_dr].angle = 70
    time.sleep(timp)
    kit.servo[cot_spt_st].angle = 120
    time.sleep(timp)
    kit.servo[cot_fat_dr].angle = 120
    time.sleep(timp)
    kit.servo[cot_fat_st].angle = 70
    time.sleep(timp)

    kit.servo[glz_spt_dr].angle = 70
    time.sleep(timp)
    kit.servo[glz_spt_st].angle = 120
    time.sleep(timp)
    kit.servo[glz_fat_dr].angle = 120
    time.sleep(timp)
    kit.servo[glz_fat_st].angle = 70

def dist():

     disttrig.value = True
     time.sleep(0.00001)
     disttrig.value = False

     while distecho.value==False:
      puls_start = time.time()

     while distecho.value==True:
      puls_end = time.time()

     durata = puls_end - puls_start
     distanta = durata * 17150
     distanta = round(distanta,2)
     print(distanta)
     return distanta


def pomp():
    pompa.value = False
    print("on")
    time.sleep(2)
    pompa.value = True
    print("off")
    time.sleep(2)




    # default
if __name__ == "__main__":
    default()
    while(True):
        if touch.value==True:
          while(True):
            walk()
            if dist()<10:
                pomp()
                for i in range(14):
                   dreapta()
                for i in range(20):
                    walk()
                exit()
            
   
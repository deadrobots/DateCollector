#!/usr/bin/python
from wallaby import *
import utils as u
import constants as c


def driveTimed(left, right, time):
    motor(c.LMOTOR, left)
    motor(c.RMOTOR, right)
    msleep(time)
    ao()

def sleep(time):
    driveTimed(0, 0, time)

def drive(left, right):
    motor(c.LMOTOR,left)
    motor(c.RMOTOR,right)

def lineFollowLeft(time):
    sec = seconds()
    while(seconds()-sec<time):
        if(u.onBlackFront()):
            drive(40,70)#was 45
        else:
            drive(70,40)#was 45
    drive(0,0)

def lineFollowRight(time):
    sec = seconds()
    while(seconds()-sec<time):
        if(u.onBlackFront()):
            drive(60,55)
        else:
            drive(55,60)
    drive(0,0)
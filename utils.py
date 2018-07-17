'''
Created on Jan 3, 2016
@author: graysonelias
'''

'''
This module provides some of our standard methods.
'''

import constants as c

from wallaby import ao
from wallaby import msleep
from wallaby import digital
from wallaby import seconds
from wallaby import freeze
from wallaby import set_servo_position
from wallaby import get_servo_position
import drive as d
import wallaby as w

def waitForButton():
    print("Press Right Button...")
    while not digital(c.RIGHT_BUTTON):
        pass
    msleep(1)
    print("Pressed")
    msleep(1000)


def DEBUG():
    freeze(c.LMOTOR)
    freeze(c.RMOTOR)
    print('Program stop for DEBUG\nSeconds: ', seconds() - c.startTime)
    ao()
    exit(0)


def DEBUGwithWait():
    freeze(c.LMOTOR)
    freeze(c.RMOTOR)
    print ('Program stop for DEBUG\nSeconds: ', seconds() - c.startTime)
    ao()
    msleep(5000)

# Servo Constants
DELAY = 10

# Servo Control #

def move_servo(servo, endPos, speed=10):  # Moves a servo with increment "speed".
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = get_servo_position(servo)
    if speed == 0:
        speed = 2047
    if endPos >= 2048:
        print("Programmer Error")
        exit(0)
    if endPos < 0:
        print("Programmer Error")
        exit(0)
    if now > endPos:
        speed = -speed
    for i in range(int(now), int(endPos), int(speed)):
        set_servo_position(servo, i)
        msleep(DELAY)
    set_servo_position(servo, endPos)
    msleep(DELAY)


def move_servo_timed(servo, endPos, time):  # Moves a servo over a specific time.
    if time == 0:
        speed = 2047
    else:
        speed = abs((DELAY * (get_servo_position(servo) - endPos)) / time)
    move_servo(servo, endPos, speed)


# Loop break timers #

time = 0  # This represents how long to wait before breaking a loop.


def setWait(DELAY):  # Sets wait time in seconds before breaking a loop.
    global time
    time = seconds() + DELAY


def getWait():  # Used to break a loop after using "setWait". An example would be: setWiat(10) | while true and getWait(): do something().
    return seconds() < time


def onBlackFront():
    return w.analog(c.FRONT_TOPHAT) > c.onBlack


def timedLineFollowLeft(time):
    sec = seconds() + time
    while seconds() < sec:
        if onBlackFront():
            d.driveTimed(20, 90, 20)
        else:
            d.driveTimed(90, 20, 20)
        msleep(10)


# Follows black line on right for specified amount of time
def timedLineFollowRight(time):
    sec = seconds() + time
    while seconds() < sec:
        if not onBlackFront():
            d.driveTimed(20, 90, 20)
        else:
            d.driveTimed(90, 20, 20)
        msleep(10)


def timedLineFollowRightSmooth(time):
    sec = seconds() + time
    while seconds() < sec:
        if not onBlackFront():
            d.driveTimed(20, 40, 20)
        else:
            d.driveTimed(40, 20, 20)
        msleep(10)


def lineFollowRightSmoothCount(amount):
    count = 0
    while count < amount:
        if not onBlackFront():
            d.driveTimed(10, 30, 10)
            count = count + 1
        else:
            d.driveTimed(30, 10, 10)
            count = 0


def timedLineFollowLeftSmooth(time):
    sec = seconds() + time
    while seconds() < sec:
        if onBlackFront():
            d.driveTimed(20, 40, 20)
        else:
            d.driveTimed(40, 20, 20)
        msleep(10)

def smoothLineFollowLeft(time, speed):
    #Max speed is 80
    #Proportional adjustment LF
    sec = seconds() + time
    while seconds() < sec:
        num = ((w.analog(4) - 1500) / 120)
        d.driveTimed(speed-num, speed+num, 10)

def smoothLineFollowLeftCondition(speed):
    #Max speed is 80
    #Proportional adjustment LF
    sec = seconds() + 7
    while w.analog(c.LEFT_TOPHAT) < 2000 and seconds()<sec:
        num = ((w.analog(4) - 1500) / 60)
        d.driveTimed(speed-num, speed+num, 10)


def timedLineFollowLeftBack(time):  # follows on starboard side
    sec = seconds() + time
    while seconds() < sec:
        if onBlackBack():
            d.driveTimed(-90, -20, 20)
        else:
            d.driveTimed(-20, -90, 20)
        msleep(10)


def crossBlackFront():
    while not onBlackFront():  # wait for black
        pass
    while onBlackFront():  # wait for white
        pass
    ao()

def wait_for_selection(force=False):    #asks for prompt twice... FIX THIS
    #asks for response; used to determine running seeding or head-to-head code
    seeding1= False
    if c.ALLOW_BUTTON_WAIT or force:
        print "Press Left Button for Seeding...\nPress Right Button for Head-to-Head"
        while not w.right_button():
            if w.left_button():
                seeding1 = True
                print "Pressed Left"
                msleep(1000)
                return seeding1
            pass
        msleep(1)
        print "Pressed Right"
        msleep(1000)
        return seeding1

'''
Created on Jan 3, 2016
@author: graysonelias
'''

'''
This module provides some of our standard methods.
'''

import constants as c

from wallaby import *
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
        num = ((w.analog(4) - 1500) / 75)
        d.driveTimed(speed-num, speed+num, 10)


def smoothLineFollowLeftCondition(speed):
    #Proportional adjustment LF
    sec = seconds() + 7
    while w.analog(c.LEFT_TOPHAT) < 2000 and seconds()<sec:
        num = ((w.analog(4) - 1500) / 75)
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

def wait_for_selection(force=False):
    seeding1= False
    if c.ALLOW_BUTTON_WAIT or force:
        print "Press Left Button for Seeding...\nPress Right Button for Head-to-Head"
        while not right_button():
            if left_button():
                seeding1 = True
                print "Pressed Left"
                msleep(1000)
                return seeding1
            pass
        msleep(1)
        print "Pressed Right"
        while right_button():
            pass
        return seeding1

def wait_4_light(ignore=False):
    if ignore:
        waitForButton()
        return
    while not calibrate(c.STARTLIGHT):
        pass
    _wait_4(c.STARTLIGHT)


def calibrate(port):
    print("Press LEFT button with light on")
    while not left_button():
        pass
    while left_button():
        pass
    lightOn = analog(port)
    print("On value =", lightOn)
    if lightOn > 1500:
        print("Bad calibration")
        return False
    msleep(1000)
    print("Press RIGHT button with light off")
    while not right_button():
        pass
    while right_button():
        pass
    lightOff = analog(port)
    print("Off value =", lightOff)
    if lightOff < 1500:
        print("Bad calibration")
        return False

    if (lightOff - lightOn) < 1000:
        print("Bad calibration")
        return False
    c.startLightThresh = (lightOff + lightOn) / 2
    print("Good calibration! ", c.startLightThresh)
    print('{} {} {}'.format(lightOff, lightOn, c.startLightThresh))
    return True

def _wait_4(port):
    print("waiting for light!! ")
    while analog(port) > c.startLightThresh:
        pass



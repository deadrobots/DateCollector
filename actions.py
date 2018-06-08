import drive as x
import utils as u
import constants as c
from wallaby import *
import motorsPlusPlus as mpp
import camera as p

colorOrder = []

def init():
    #The starting position is marked with pencil on the closest box on the right side
    #If you cant see the lines, the bot should be flush to the wall parallel to the tram
    #For a more exact placement, the left wheel should be 4.75 inches from the black tape
    #starting positions
    if(c.isClone):
        print("IS BLUE")
    else:
        print("IS GREEN")
    enable_servos()
    startTest()
    #msleep(500)
    u.waitForButton()

def calibrate_drive ():
    print("calibrating")
    if (c.isClone):
        print("IS BLUE")
    else:
        print("IS GREEN")
    mpp.drive_speed(24, 80)
    u.waitForButton()
    mpp.drive_speed(24, -80)
    u.waitForButton()

def startTest():
    print("Running Start Test")
    mpp.drive_speed(3, 30)
    mpp.drive_speed(-3, 30)
    u.move_servo(c.servoArmBin, c.armUp)
    u.move_servo(c.servoArmBin, c.armDown)
    '''u.move_servo(c.servoSlider, c.sliderOut)
    u.move_servo(c.servoSlider, c.sliderBack)
    u.move_servo(c.servoClawPoms, c.clawOpen)
    u.move_servo(c.servoClawPoms, c.clawClosed)'''
    mpp.drive_date_motor(50, 1000)

def driveOutStartBox():
    if (c.isClone):
        #drives out of start box to pom
        mpp.drive_speed(4, 80)
        mpp.rotate(-85, 50)
        u.move_servo(c.servoArmBin, c.armUp)
        mpp.drive_speed(-27, 80)
        mpp.rotate(62, 50)
        msleep(500)
    else:
        mpp.drive_speed(3.5, 80)  # 9.4
        mpp.rotate(-90, 50)#-90
        u.move_servo(c.servoArmBin, c.armUp)
        mpp.drive_speed(-27, 80)#-20.75
        #u.move_servo(c.servoClawPoms, c.clawOpen)
        mpp.rotate(66, 50)
        msleep(1000)

def driveUntilTree():
    print("Looking for Trees")
    if (c.isClone):
        mpp.drive_speed(10, 50)
        mpp.rotate(-10, 30)
        while analog(c.ET) < c.onTree:
            mpp.drive_timed(50, 50, 0.01)
            print(analog(c.ET))
        print("Saw Tree")
        u.waitForButton()
        mpp.drive_speed(2, 50)
        #mpp.drive_timed(5, 40, 1.5)
        mpp.pivot_right(10, 25)
        u.waitForButton()
    else:
        mpp.pivot_right(-8, 25)
        mpp.drive_speed(10, 50)
        while analog(c.ET) < c.onTree:
            mpp.drive_timed(50, 50, 0.01)
            print(analog(c.ET))
        print("Saw Tree")
        mpp.drive_speed(2, 50)
        #u.waitForButton()

def driveFirstThreeTrees():
    print("Driving to First Trees")
    if c.isClone:
        #mpp.drive_speed(-7, 40)
        mpp.drive_speed(-8, 50)
        #mpp.drive_speed(1.5, 40)
        #mpp.drive_timed(-60, -30, 2)
        u.move_servo(c.servoArmBin, c.armDown)
        msleep(500)
        mpp.drive_speed(1.5, 50)
        mpp.get_poms_timed(50, 7000)
        msleep(1000)
        driveUntilTree()
        mpp.get_poms_timed(50, 7000)
        msleep(1000)
        driveUntilTree()
        mpp.get_poms_timed(50, 7000)
        msleep(1000)
    else:
        mpp.drive_speed(-6, 50)
        u.move_servo(c.servoArmBin, c.armDown)
        #mpp.drive_timed(20, 80, 1)
        mpp.pivot_right(10, 25)
        mpp.drive_speed(1, 20)
        msleep(250)
        mpp.get_poms_timed(50, 7000)
        msleep(1000)
        driveUntilTree()
        mpp.get_poms_timed(50, 7000)
        msleep(1000)
        driveUntilTree()
        mpp.get_poms_timed(50, 7000)
        msleep(1000)

def driveToNextTrees():
    u.move_servo(c.servoArmBin, c.armUp, 25)
    mpp.drive_speed(-4.7, 60)
    mpp.rotate(-90, 50)
    mpp.drive_speed(-7, 80)
    msleep(500)
    mpp.drive_speed(14, 80)
    msleep(500)
    mpp.rotate(89, 50)
    msleep(5000)
    mpp.drive_speed(44, 90)
    u.DEBUG()
    msleep(500)
    mpp.rotate(-90, 50)
    mpp.drive_speed(-14, 80)
    msleep(500)
    mpp.drive_speed(5, 80)
    mpp.rotate(90, 50)
    mpp.drive_speed(-11.75, 50)
    msleep(500)

def driveFinalThreeTrees():
    u.move_servo(c.servoArmBin, c.armDown, 25)
    mpp.drive_speed(.75, 50)
    collectPoms()
    msleep(500)
    mpp.drive_speed(13, 50)
    collectPoms()
    msleep(500)
    mpp.drive_speed(13, 50)
    collectPoms()
    msleep(500)

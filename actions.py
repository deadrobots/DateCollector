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
        print("IS CLONE")
    else:
        print("IS PRIME")
    enable_servos()
    startTest()
    #msleep(500)
    u.waitForButton()

def startTest():
    print("Running Start Test")
    mpp.drive_speed(3, 30)
    mpp.drive_speed(-3, 30)
    u.move_servo(c.servoArmBin, c.armUp)
    u.move_servo(c.servoArmPoms, c.pomArmOut)
    u.move_servo(c.servoArmPoms, c.pomArmBack)
    u.move_servo(c.servoClawPoms, c.pomClawOpen)
    u.move_servo(c.servoClawPoms, c.pomClawClosed)

def driveOutStartBox():
    if (c.isClone):#drives out of start box to pom
        mpp.drive_speed(3, 50)
        mpp.rotate(-75, 20)
        mpp.drive_timed(-60, -43, 10)
        #mpp.rotate(80, 50)
    else:
        mpp.drive_speed(3.5, 80)  # 9.4
        mpp.rotate(-90, 50)
        mpp.drive_speed(-27.5, 80)
        mpp.rotate(80, 50)

def collectPoms():
    #extends arm then collects poms
    u.move_servo(c.servoArmPoms, c.pomArmOut)
    u.move_servo(c.servoClawPoms, c.pomClawOpen)
    u.move_servo(c.servoClawPoms, c.pomClawClosed)
    u.move_servo(c.servoArmPoms, c.pomArmBack)

def driveFirstThreeTrees():
    mpp.drive_speed(-5.5, 30)
    u.move_servo(c.servoArmBin, c.armDown, 25)
    mpp.drive_speed(.75, 40)
    collectPoms()
    msleep(500)
    mpp.drive_speed(13.5, 50)
    collectPoms()
    msleep(500)
    mpp.drive_speed(13.5, 50)
    collectPoms()
    msleep(500)

def driveToNextTrees():
    u.move_servo(c.servoArmBin, c.armUp, 25)
    mpp.drive_speed(-5, 60)
    mpp.rotate(-90, 50)
    mpp.drive_speed(-5, 80)
    mpp.drive_speed(13, 80)
    mpp.rotate(95, 50)
    mpp.drive_speed(40, 90)
    mpp.rotate(-90, 50)
    mpp.drive_speed(-14, 80)
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

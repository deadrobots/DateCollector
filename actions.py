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
        print "IS CLONE"
    else:
        print "IS PRIME"
    enable_servos()
    set_servo_position(c.servoArm, c.armUp)
    msleep(400)
    u.waitForButton()

def driveOutStartBox():
    #drives out of start box to pom
    mpp.drive_speed(3.5, 80)   #9.4
    mpp.rotate(-90, 50)
    mpp.drive_speed(-27.5, 80)
    mpp.rotate(90, 50)
    mpp.drive_speed(-5.5, 30)
    u.move_servo(c.servoArm, c.armDown, 25)
    mpp.drive_speed(.75, 40)
    msleep(2000)
    mpp.drive_speed(13.5, 50)
    msleep(2000)
    mpp.drive_speed(13.5, 50)
    msleep(2000)
    u.move_servo(c.servoArm, c.armUp, 25)
    mpp.drive_speed(-5, 60)
    mpp.rotate(-90, 50)
    mpp.drive_speed(-5, 80)
    mpp.drive_speed(13, 80)
    mpp.rotate(92, 50)
    mpp.drive_speed(33, 90)
    mpp.rotate(-90, 50)
    mpp.drive_speed(-9.2, 80)
    mpp.rotate(90, 50)
    mpp.drive_speed(-5.5, 50)
    u.move_servo(c.servoArm, c.armDown, 25)
    mpp.drive_speed(.75, 50)
    msleep(2000)
    mpp.drive_speed(13, 50)
    msleep(2000)
    mpp.drive_speed(13, 50)
    msleep(2000)

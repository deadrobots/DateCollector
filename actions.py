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
    if(c.isBlue):
        print("IS BLUE")
    elif c.isGreen:
        print("IS GREEN")
    elif c.isYellow:
        print("IS YELLOW")
    enable_servos()
    startTest()
    #msleep(500)
    u.waitForButton()

def calibrate_drive ():
    if (c.isBlue):
        print("IS BLUE")
    elif c.isGreen:
        print("IS GREEN")
    elif c.isYellow:
        print("IS YELLOW")
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
    if (c.isBlue):
        #drives out of start box to pom
        mpp.drive_speed(4, 80)
        mpp.rotate(-85, 50)
        u.move_servo(c.servoArmBin, c.armUp)
        mpp.drive_speed(-27, 80)
        mpp.rotate(62, 50)
        msleep(500)
    elif c.isGreen:
        mpp.drive_speed(3.5, 80)  # 9.4
        mpp.rotate(-90, 50)#-90
        u.move_servo(c.servoArmBin, c.armUp)
        mpp.drive_speed(-27, 80)#-20.75
        #u.move_servo(c.servoClawPoms, c.clawOpen)
        mpp.rotate(90, 50) #was 66 #was 58
        mpp.drive_speed(-5, 40)
        mpp.drive_speed(3, 40)
        mpp.rotate(-30, 50)
        msleep(1000)
    elif c.isYellow:
        mpp.drive_speed(3.5, 80)
        mpp.rotate(-80, 50)
        u.move_servo(c.servoArmBin, c.armUp)
        mpp.drive_speed(-27, 80) #was -26
        mpp.rotate(85, 50) #was 78
        mpp.drive_speed(-6, 40)
        mpp.drive_speed(3, 40)
        mpp.rotate(-30, 50)
        msleep(1000)

def driveUntilTree():
    print("Looking for Trees")
    if (c.isBlue):
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
    elif c.isGreen:
        mpp.pivot_right(-8, 25)#-8
        mpp.drive_speed(6, 50)
        mpp.pivot_right(4, 25)
        while analog(c.ET) < c.onTree:
            mpp.drive_timed(50, 50, 0.01)
            print(analog(c.ET))
        print("Saw Tree")
        mpp.pivot_right(9, 25)#10
        mpp.drive_speed(.3, 50)
        # mpp.drive_timed(5, 40, 1.5)
        #mpp.drive_speed(2, 50)
        #u.waitForButton()
    elif c.isYellow:
        mpp.pivot_right(-8, 25)
        mpp.drive_speed(6, 50)
        mpp.pivot_right(4, 25)
        while analog(c.ET) < c.onTree:
            mpp.drive_timed(50, 50, 0.01)
            print(analog(c.ET))
        print("Saw Tree")
        mpp.pivot_right(9, 25) #was 5
        mpp.drive_speed(1, 50) #was 2.5

def driveFirstThreeTrees():
    print("Driving to First Trees")
    if c.isBlue:
        #mpp.drive_speed(-7, 40)
        mpp.drive_speed(-8.5, 50)
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
    elif c.isGreen:
        mpp.drive_speed(-7, 50)
        u.move_servo(c.servoArmBin, c.armDown)
        mpp.drive_speed(0.73, 20)
        msleep(250)
        motor_power(c.RMOTOR,10)
        mpp.get_poms_timed(50, 7050)
        u.DEBUG()
        msleep(1000)
        driveUntilTree()
        mpp.get_poms_timed(50, 7000)
        msleep(1000)
        driveUntilTree()
        mpp.get_poms_timed(50, 7000)
        msleep(1000)
    elif c.isYellow:
        mpp.drive_speed(-7, 50)
        u.move_servo(c.servoArmBin, c.armDown)
        mpp.drive_speed(0.73, 20)
        msleep(250)
        motor_power(c.RMOTOR,10)
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
    mpp.drive_speed(17, 80)#14
    msleep(500)
    mpp.rotate(89, 50)
    msleep(1000)
    if c.isGreen:
        u.amazinglyPerfectLineFolloe(7.5, 80)
    elif c.isBlue:
        u.amazinglyPerfectLineFolloe(7.5, 80)
    elif c.isYellow:
        u.amazinglyPerfectLineFolloe(5, 80)
    #mpp.drive_speed(44, 90)
    msleep(500)
    mpp.rotate(-90, 50)
    mpp.drive_speed(-19, 80)
    msleep(500)
    mpp.drive_speed(5, 80)
    mpp.rotate(93, 50)
    mpp.drive_speed(-14, 50)
    msleep(500)

def driveFinalThreeTrees():
    if c.isYellow:
        mpp.drive_speed(3, 40)
        mpp.rotate(-28, 50)
        msleep(1000)
        #mpp.drive_speed(-7, 50)
        mpp.drive_timed(-75,-100,1.5)
        u.move_servo(c.servoArmBin, c.armDown)
        u.waitForButton()
        mpp.get_poms_timed(50, 7000)
        msleep(1000)
        driveUntilTree()
        mpp.get_poms_timed(50, 7000)
        msleep(1000)
        driveUntilTree()
        mpp.get_poms_timed(50, 7000)
        msleep(1000)


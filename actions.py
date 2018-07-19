import drive as x
import utils as u
import constants as c
from wallaby import *
import motorsPlusPlus as mpp
import camera as p

def init():
    #The starting position is marked with pencil on the closest box on the right side
    #If you cant see the lines, the bot should be flush to the wall parallel to the tram
    #For a more exact placement, the left wheel should be 4.75 inches from the black tape
    print("Init")
    if(c.isBlue):
        print("IS BLUE")
    elif c.isGreen:
        print("IS GREEN")
    elif c.isYellow:
        print("IS YELLOW")
    enable_servos()
    startTest()

def startTest():
    print("Running Start Test")
    while analog(c.LEFT_TOPHAT) < 2000:
        mpp.drive_speed(.1, 80)
    msleep(750)
    while analog(c.RIGHT_TOPHAT) < 1500:
        mpp.drive_speed(.1, 80)
    mpp.drive_speed(-9, 70)
    u.move_servo(c.servoDateWheel, c.wheelOut)
    print "Do the ET check!!!! (put you hand in front)"
    while analog(c.ET) < 1000:
        pass
    u.move_servo(c.servoDateWheel, c.wheelIn)
    mpp.new_get_poms_timed(50, 2000)
    u.move_servo(c.servoArmBin, c.armDown, 20)
    u.move_servo(c.servoArmBin, c.armUp, 20)
    u.move_servo(c.servoPipeWheel, c.pipeOut, 20)
    u.move_servo(c.servoPipeWheel, c.pipeBin, 20)
    ao()

def driveOutStartBox():
    #Starts from the start box, drives to first date tree and positions itself to collect
    print("Drive Out of Start Box")
    if c.isBlue:
        mpp.drive_speed(-1.5, 70)
        mpp.drive_speed(3.9, 100)
        msleep(200)
        mpp.rotate(-89, 60) #-85.8
        msleep(200)
        mpp.drive_speed(-28.3, 100)  # 28.5
        u.move_servo(c.servoPipeWheel, c.pipeStraight, 20)
        u.move_servo(c.servoDateWheel, c.wheelOut, 20)
        mpp.drive_speed(.7, 80) #was 0.45
        msleep(100)
        mpp.rotate(95, 80) #89#99
        msleep(100)
        mpp.drive_speed(-7.5, 90)  # 5
        mpp.drive_speed(3, 90)
        msleep(100)
        mpp.rotate(-23, 80)  # was -21
        msleep(100)
    elif c.isGreen:
        mpp.drive_speed(-1.5, 70)
        mpp.drive_speed(3.9, 100)
        msleep(200)
        mpp.rotate(-89, 80)  # -89
        msleep(200)
        mpp.drive_speed(-30, 100)  # 28.3
        u.move_servo(c.servoPipeWheel, c.pipeStraight, 20)
        u.move_servo(c.servoDateWheel, c.wheelOut, 20)
        mpp.drive_speed(1.6, 80)  # was 0.7
        msleep(100)
        mpp.rotate(97, 80)  #95
        msleep(100)
        mpp.drive_speed(-7.5, 90)  # 5
        mpp.drive_speed(3, 90)
        msleep(100)
        mpp.rotate(-23, 80)  # was -21
        msleep(100)

def driveUntilTree():
    #Helper function for driveFirstThreeTrees()
    #Drives from one date tree to the next
    print("Looking for Trees")
    sec = seconds() + 5
    while analog(c.ET) < c.onTree and seconds()<sec:
        mpp.drive_speed(.05, 90)
        print(analog(c.ET))
    print("Saw Tree")
    u.move_servo(c.servoArmBin, c.armDown, 20)

def driveFirstTrees():
    print "driveFirstTrees"
    mpp.drive_speed(-3.3, 100)#-9
    msleep(100)
    mpp.pivot_left(-40, 70)
    msleep(100)
    mpp.drive_speed(-2, 70)
    mpp.drive_speed(.5, 70)  # .73, 35
    msleep(100)
    mpp.pivot_right(6, 80) #8
    u.move_servo(c.servoDateWheel, c.wheelIn + 100, 20)
    u.move_servo(c.servoDateWheel, c.wheelIn, 8)
    mpp.new_get_poms_timed(100, 7000)
    msleep(100)
    u.move_servo(c.servoDateWheel, c.wheelOut, 20)
    mpp.pivot_right(-3, 70)
    mpp.drive_speed(2, 70)
    mpp.pivot_right(3, 70)
    mpp.pivot_right(9, 70)

def driveFirstTreesH2H():
    print "driveFirstTrees"
    mpp.drive_speed(-3.3, 100)#-9
    msleep(100)
    mpp.pivot_left(-40, 70)
    msleep(100)
    mpp.drive_speed(-2, 70)
    mpp.drive_speed(.5, 70)  # .73, 35
    msleep(100)
    mpp.pivot_right(8, 80) #8
    u.move_servo(c.servoDateWheel, c.wheelIn + 100, 20)
    u.move_servo(c.servoDateWheel, c.wheelIn, 8)
    mpp.new_get_poms_timed(100, 5000)
    msleep(100)
    u.move_servo(c.servoDateWheel, c.wheelOut, 20)
    u.move_servo(c.servoArmBin, c.armDown, 20)
    u.move_servo(c.servoPipeWheel, c.pipeBin, 20)

def getSecondDateBin():
    mpp.drive_speed(4, 70)
    u.move_servo(c.servoArmBin, c.armDown, 30)
    mpp.drive_speed(2.5, 70)
    u.move_servo(c.servoPipeWheel, c.pipeBin, 20)
    mpp.pivot_right(6, 70)

def grabFirstPoms():
    print "grabFirstPoms"
    mpp.drive_speed(5, 85) #2.8
    driveUntilTree()
    msleep(100)
    mpp.drive_speed(-0.075, 80)
    mpp.pivot_right(6, 80) #8
    u.move_servo(c.servoDateWheel, c.wheelIn + 100, 30)
    u.move_servo(c.servoDateWheel, c.wheelIn - 100, 10)
    mpp.new_get_poms_timed(100, 5000)
    msleep(100)
    u.move_servo(c.servoDateWheel, c.wheelOut, 20)
    mpp.drive_speed(2, 80)
    mpp.pivot_right(4, 80)
    u.move_servo(c.servoPipeWheel, c.pipeBin, 30)
    mpp.drive_speed(6, 85)
    driveUntilTree()
    mpp.drive_speed(0.6, 60)
    mpp.pivot_right(-4, 80)
    mpp.drive_speed(-0.5, 80)
    mpp.pivot_right(6, 80) #was 6
    u.move_servo(c.servoDateWheel, c.wheelIn + 100, 30)
    u.move_servo(c.servoDateWheel, c.wheelIn - 50, 10)
    mpp.new_get_poms_timed(100, 5000)
    mpp.pivot_right(-4, 80)

def driveToNextTrees():
    print("Driving to Next Set of Trees")
    u.move_servo(c.servoArmBin, c.armUp, 40)
    mpp.drive_speed(-4.2, 80)
    mpp.rotate(-90, 80)
    mpp.drive_speed(-7, 90)
    mpp.drive_speed(17, 100)  # 14
    msleep(100)
    mpp.rotate(95, 80) #89
    u.move_servo(c.servoPipeWheel, c.pipeOut, 40)
    u.smoothLineFollowLeftCondition(85)
    u.smoothLineFollowLeft(3.3, 85)
    if analog(c.RIGHT_TOPHAT) > c.onBlack:
        while analog(c.RIGHT_TOPHAT) > c.onBlack:
            mpp.rotate(1, 60)
    elif analog(c.RIGHT_TOPHAT) < 1000:
        while analog(c.RIGHT_TOPHAT) < 1000:
            mpp.rotate(-1, 60)
    mpp.rotate(-90, 80)
    u.move_servo(c.servoPipeWheel, c.pipeOut, 40)
    mpp.drive_speed(-9.6, 90)
    u.move_servo(c.servoPipeWheel, 200, 25)
    mpp.rotate(93, 70)
    u.move_servo(c.servoPipeWheel, c.pipeOut, 25)
    mpp.drive_speed(6, 85) #7
    mpp.drive_speed(-1.5, 85) #-3
    u.move_servo(c.servoPipeWheel, 200, 25)
    mpp.rotate(-92, 85)
    mpp.drive_speed(-10.5, 100)

def getThirdDateBin():
    mpp.drive_speed(5.8, 100)
    u.move_servo(c.servoPipeWheel, c.pipeStraight, 25)
    mpp.rotate(101, 75)#92#99
    mpp.drive_speed(2, 80) #2.8
    u.move_servo(c.servoPipeWheel, 900, 20)
    mpp.drive_timed(-90, -60, 2) #was -85
    tim = seconds()
    while analog(c.ET) < (c.onTree - 500) and seconds()-tim < 2.8:
        mpp.drive_timed(-90, -60, .05) #was -85, -60
    if seconds()-tim > 2.8:
        print("Fourth tree timeout")
        mpp.rotate(16, 80)
        mpp.drive_speed(-.6, 70)
    mpp.pivot_right(15, 65)
    u.move_servo(c.servoPipeWheel, c.pipeBin, 25)
    print "Saw Tree"
    mpp.pivot_right(6, 75)
    mpp.drive_speed(1.5, 80)
    mpp.rotate(-18, 80) #-20
    mpp.drive_speed(-4.5, 80) #-6.5
    mpp.pivot_left(-25, 80)
    msleep(100)
    mpp.pivot_right(25, 75) #was 18 degrees
    mpp.new_get_poms_timed(100, 8000) #6000
    mpp.pivot_right(-3, 60)

def getThirdDateBinH2H():
    mpp.drive_speed(5.8, 100)
    u.move_servo(c.servoPipeWheel, c.pipeStraight, 25)
    mpp.rotate(100, 75) #95
    mpp.drive_speed(8, 80) #was 6
    u.move_servo(c.servoPipeWheel, 900, 20)
    mpp.drive_timed(-90, -60, 2) #was -100, -60
    tim = seconds()
    while analog(c.ET) < (c.onTree - 500) and seconds()-tim < 2.8:
        mpp.drive_timed(-90, -60, .05) #was -100, -60
    if seconds()-tim > 2.8:
        print("Fourth tree timeout")
        mpp.rotate(16, 80)
        mpp.drive_speed(-.6, 70)
        mpp.pivot_right(15, 65)
        u.move_servo(c.servoPipeWheel, c.pipeBin, 25)
        print "Saw Tree"
        mpp.pivot_right(6, 75)
        mpp.drive_speed(1.5, 80)
        mpp.rotate(-15, 80) #-20
    mpp.pivot_right(15, 65)
    u.move_servo(c.servoPipeWheel, c.pipeBin, 25)
    print "Saw Tree"
    mpp.pivot_right(6, 75)
    mpp.drive_speed(1.5, 80)
    mpp.rotate(-20, 80)  # -18
    mpp.drive_speed(-5.5, 80) #-4.5
    mpp.pivot_left(-25, 80)
    msleep(100)
    mpp.pivot_right(25, 75) #was 18 degrees
    mpp.new_get_poms_timed(100, 8000) #6000
    mpp.pivot_right(-3, 60)
    u.move_servo(c.servoDateWheel, c.wheelOut, 25)
    mpp.drive_speed(-0.4, 80)
    mpp.rotate(10, 80)
    u.move_servo(c.servoArmBin, c.armDown, 25)
    u.move_servo(c.servoPipeWheel, c.pipeBin, 25)
    mpp.pivot_right(13, 85)


def driveFinalThreeTrees():
    # Goes from each of the last three trees collecting poms
    print("Collect Final Three Sets of Poms")
    u.move_servo(c.servoDateWheel, c.wheelOut, 25)
    mpp.drive_speed(-.4, 80)
    mpp.rotate(10, 80)
    u.move_servo(c.servoArmBin, c.armDown, 25)
    u.move_servo(c.servoPipeWheel, c.pipeBin, 25)
    mpp.pivot_right(13, 85)
    mpp.drive_speed(5, 85)
    driveUntilTree()
    mpp.drive_speed(.5, 70) #0.3
    u.move_servo(c.servoDateWheel, c.wheelIn + 100, 30)
    u.move_servo(c.servoDateWheel, c.wheelIn + 70, 10)
    mpp.new_get_poms_timed(100, 7000)
    msleep(100)
    u.move_servo(c.servoArmBin, c.armUp, 25)
    mpp.drive_speed(-2, 80)
    mpp.pivot_right(-5, 80)
    u.move_servo(c.servoDateWheel, c.wheelOut, 25)
    u.move_servo(c.servoPipeWheel, c.pipeStraight, 25)
    mpp.drive_speed(1, 80)
    mpp.pivot_right(10, 80)
    mpp.drive_speed(1.5, 80)
    #mpp.pivot_left(-7, 70)
    #mpp.drive_speed(3, 60)
    #mpp.drive_speed(2.5, 60)
    mpp.drive_speed(1.5, 90)
    u.move_servo(c.servoPipeWheel, c.pipeBin, 25)
    mpp.pivot_right(16, 80)
    mpp.drive_speed(1, 85)
    u.move_servo(c.servoArmBin, c.armDown, 25)
    mpp.drive_speed(3, 85)
    driveUntilTree()
    mpp.drive_speed(.2, 70)
    u.move_servo(c.servoDateWheel, c.wheelIn + 100, 30)
    u.move_servo(c.servoDateWheel, c.wheelIn + 50, 10)
    mpp.new_get_poms_timed(100, 8000)
    mpp.new_get_poms_timed(100, 8000)
    u.move_servo(c.servoDateWheel, c.wheelOut, 30)

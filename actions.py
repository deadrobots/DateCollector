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
    print("Init")
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
    c.startTime = seconds()
    shut_down_in(119.5)

def startTest():
    print("Running Start Test")
    # if not c.isYellow:
    # u.move_servo(c.servoArmBin, c.armDown)
    # u.move_servo(c.servoArmBin, c.armUp)
    # u.move_servo(c.servoPipeWheel, c.pipeOut)
    # u.move_servo(c.servoPipeWheel, c.pipeBin)
    # mpp.drive_date_motor(50, 1000)
    # print "Do the ET check!!!! (put you hand in front)"
    # while analog(c.ET) < 1000:
    #     pass
    # else:
    #mpp.drive_speed(6, 70)
    #mpp.drive_speed(-6.5, 70)
    while analog(c.LEFT_TOPHAT) < 2000:
        mpp.drive_speed(.1, 80)
    msleep(500)
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
    # if (c.isBlue):
    #     mpp.drive_speed(4, 90)
    #     msleep(300)
    #     mpp.rotate(-80, 70)
    #     msleep(300)
    #     u.move_servo(c.servoArmBin,c.armUp)
    #     mpp.drive_speed(-27.2, 90) #27
    #     mpp.drive_speed(1.4, 70)
    #     u.move_servo(c.servoPipeWheel, c.pipeStraight)
    #     mpp.rotate(90, 70)
    #     mpp.drive_speed(-6, 80) #5
    #     mpp.drive_speed(3, 80)
    #     mpp.rotate(-26, 70)  # was -27
    #     msleep(500)
    # elif c.isGreen:
    #     mpp.drive_speed(3.5, 80)  # 9.4
    #     mpp.rotate(-92, 50)#-90
    #     u.move_servo(c.servoArmBin, c.armUp)
    #     mpp.drive_speed(-26.9, 80)
    #     mpp.rotate(90, 50)
    #     mpp.drive_speed(-5, 40)
    #     mpp.drive_speed(3, 40)
    #     mpp.rotate(-28, 50) #was -30
    #     msleep(1000)
    # elif c.isYellow:
    mpp.drive_speed(-1.5, 70)
    mpp.drive_speed(3.9, 100)
    msleep(200)
    mpp.rotate(-85.8, 80) #-85
    msleep(200)
    mpp.drive_speed(-28.3, 100)  # 27.1
    u.move_servo(c.servoPipeWheel, c.pipeStraight, 20)
    u.move_servo(c.servoDateWheel, c.wheelOut, 20)
    mpp.drive_speed(.45, 80)
    msleep(100)
    mpp.rotate(95, 80) #89#99
    msleep(100)
    mpp.drive_speed(-7.5, 90)  # 5
    mpp.drive_speed(3, 90)
    msleep(100)
    mpp.rotate(-21, 80)  # was -19
    msleep(100)
    '''
    mpp.drive_speed(3.5, 80)
    mpp.rotate(-80, 50)
    u.move_servo(c.servoArmBin, c.armUp)
    mpp.drive_speed(-27, 80) #was -26
    mpp.rotate(85, 50) #was 78
    mpp.drive_speed(-6, 40)
    mpp.drive_speed(3, 40)
    mpp.rotate(-30, 50)
    msleep(1000)'''

def driveUntilTree():
    #Helper function for driveFirstThreeTrees()
    #Drives from one date tree to the next
    print("Looking for Trees")
    if (c.isBlue):
        while analog(c.ET) < c.onTree:
            mpp.drive_speed(.05, 90)
            print(analog(c.ET))
        print("Saw Tree")
        u.move_servo(c.servoArmBin, c.armDown, 20)
    elif c.isGreen:
        mpp.pivot_right(-8, 25)#-8
        mpp.drive_speed(4, 50)
        mpp.pivot_right(8, 25)
        while analog(c.ET) < c.onTree:
            mpp.drive_timed(50, 50, 0.01)
            print(analog(c.ET))
        print("Saw Tree")
        mpp.pivot_right(2, 25)#10
        mpp.drive_speed(1.4, 50)#1.4
    elif c.isYellow:
        msleep(200)
        while analog(c.ET) < c.onTree:
            mpp.drive_speed(.1, 70)
            print(analog(c.ET))
        msleep(200)
        print("Saw Tree")

def driveFirstTrees():
    print "driveFirstTrees"
    # if c.isBlue:
    #     #Please reorganize functions if you have time
    #     #Make shorter functions
    #     mpp.drive_speed(-9, 70)
    #     u.move_servo(c.servoArmBin, c.armDown)
    #     mpp.drive_speed(1.0, 35)  # .73
    #     msleep(250)
    #     mpp.pivot_right(4, 60)
    #     # motor_power(c.RMOTOR, 10)
    #     mpp.get_poms_timed(80, 7500)
    #     mpp.pivot_right(-4, 60)
    #     msleep(400)
    #     u.move_servo(c.servoArmBin, c.armUp)
    #     u.move_servo(c.servoPipeWheel,c.pipeStraight)
    #     #u.waitForButton()
    #     mpp.pivot_right(-16, 50)  # -8
    #     mpp.drive_speed(3, 60)
    #     mpp.pivot_right(24, 50)
    #     mpp.drive_speed(4, 60)
    # elif c.isGreen:
    #     mpp.drive_speed(-7, 50)
    #     mpp.drive_speed(0.5, 20)  # .73
    #     mpp.pivot_right(3, 50)
    #     msleep(250)
    #     # motor_power(c.RMOTOR, 10)
    #     mpp.get_poms_timed(70, 6000)
    #     msleep(1000)
    # elif c.isYellow:
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
    mpp.new_get_poms_timed(90, 5000)
    msleep(100)
    mpp.pivot_right(-3, 70)
    mpp.drive_speed(2, 70)
    mpp.pivot_right(3, 70)
    #mpp.pivot_right(-7, 70)
    #mpp.pivot_left(7, 60)
    #mpp.drive_speed(4, 60)
    #mpp.pivot_right(9, 60)
    u.move_servo(c.servoDateWheel, c.wheelOut, 20)
    mpp.pivot_right(9, 70)

def getSecondDateBin():
    mpp.drive_speed(4, 70)
    u.move_servo(c.servoArmBin, c.armDown, 30)
    mpp.drive_speed(2.5, 70)
    u.move_servo(c.servoPipeWheel, c.pipeBin, 20)
    mpp.pivot_right(6, 70)

def grabFirstPoms():
    print "grabFirstPoms"
    # if c.isBlue:
    #     driveUntilTree()
    #     mpp.drive_speed(-.6, 60)
    #     msleep(300)
    #     mpp.pivot_right(4, 60)
    #     u.move_servo(c.servoPipeWheel, c.pipeBin)
    #     mpp.get_poms_timed(70, 6800)
    #     mpp.pivot_right(-3, 60)
    #     msleep(400)
    #     mpp.pivot_right(-6, 45)  # -8
    #     mpp.drive_speed(3, 70)
    #     mpp.pivot_right(6, 45)
    #     driveUntilTree()
    #     mpp.drive_speed(-1, 60)
    #     mpp.pivot_right(5, 60)
    #     mpp.get_poms_timed(75, 6000)
    #     mpp.pivot_right(-3, 60)
    #     msleep(400)
    # elif c.isGreen:
    #     driveUntilTree()
    #     u.move_servo(c.servoArmBin, c.armDown)
    #     u.waitForButton()
    #     mpp.get_poms_timed(70, 7500)
    #     msleep(1000)
    #     driveUntilTree()
    #     mpp.get_poms_timed(70, 7500)
    #     msleep(1000)
    # elif c.isYellow:
    mpp.drive_speed(2.8, 85)
    driveUntilTree()
    msleep(100)
    mpp.pivot_right(8, 80)
    u.move_servo(c.servoDateWheel, c.wheelIn + 100, 30)
    u.move_servo(c.servoDateWheel, c.wheelIn - 100, 10)
    mpp.new_get_poms_timed(95, 5000)
    msleep(100)
    mpp.drive_speed(2, 80)
    mpp.pivot_right(4, 80)
    u.move_servo(c.servoDateWheel, c.wheelOut, 20)
    u.move_servo(c.servoPipeWheel, c.pipeBin, 30)
    mpp.drive_speed(6, 85)
    driveUntilTree()
    #mpp.drive_speed(.6, 60)
    mpp.pivot_right(6, 80)
    mpp.drive_speed(0.5, 80)
    u.move_servo(c.servoDateWheel, c.wheelIn + 100, 30)
    u.move_servo(c.servoDateWheel, c.wheelIn - 50, 10)
    mpp.new_get_poms_timed(95, 5000)
    mpp.pivot_right(-4, 80)

def driveToNextTrees():
    #Uses an amazingly smooth line follow to go from one set of trees to the other
    print("Driving to Next Set of Trees")
    u.move_servo(c.servoArmBin, c.armUp, 25)
    mpp.drive_speed(-4.7, 70)
    mpp.rotate(-90, 70)
    mpp.drive_speed(-7, 80)
    msleep(500)
    mpp.drive_speed(17, 80)#14
    msleep(5000)
    mpp.rotate(100, 65)
    msleep(1000)
    if c.isGreen:
        u.smoothLineFollowLeft(7.2, 80)
    elif c.isBlue:
        u.smoothLineFollowLeft(7.5, 80)
    elif c.isYellow:
        u.smoothLineFollowLeft(5, 80)
    #mpp.drive_speed(44, 90)
    msleep(500)
    if c.isGreen:
        mpp.rotate(-95, 50)
    else:
        mpp.rotate(-90, 50)
    mpp.drive_speed(-20, 80)
    msleep(500)
    mpp.drive_speed(5.5, 80)
    if c.isGreen:
        mpp.rotate(94.5, 50)
    elif c.isBlue:
        mpp.rotate(93, 50)
    elif c.isYellow:
        mpp.rotate(93, 50)
    msleep(500)

def driveToNextTrees2():
    print("Driving to Next Set of Trees")
    u.move_servo(c.servoArmBin, c.armUp, 40)
    mpp.drive_speed(-4.2, 80)
    if c.isBlue:
        mpp.rotate(-90, 80)
        mpp.drive_speed(-7, 90)
        mpp.drive_speed(17, 100)  # 14
        msleep(100)
        mpp.rotate(101, 80) #89
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
        mpp.drive_speed(5.8, 100)
        u.move_servo(c.servoPipeWheel, c.pipeStraight, 25)
        mpp.rotate(101, 75)#92#99
        mpp.drive_speed(2.8, 80) #2.5
        u.move_servo(c.servoPipeWheel, 900)
        mpp.drive_timed(-85, -60, 2) #was -90
        tim = seconds()
        while analog(c.ET) < (c.onTree - 500) and seconds()-tim < 2.8:
            mpp.drive_timed(-85, -60, .05) #was -90, -60
        if seconds()-tim > 2.8:
            print("Fourth tree timeout")
            mpp.rotate(16, 80)
            mpp.drive_speed(-.6, 70)
        mpp.pivot_right(15, 65)
        u.move_servo(c.servoPipeWheel, c.pipeBin, 25)
        print "Saw Tree"
        mpp.pivot_right(6, 75)
        mpp.drive_speed(1.5, 80)
        u.move_servo(c.servoPipeWheel, c.pipeBin, 25)
        mpp.rotate(-18, 80) #-20
        mpp.drive_speed(-4.5, 80) #-6.5
        mpp.pivot_left(-25, 80)
        msleep(100)
        mpp.pivot_right(25, 75) #was 18 degrees
        #mpp.drive_speed(.2, 50)
        #mpp.pivot_right(3, 50)
        mpp.new_get_poms_timed(95, 4500)
    elif c.isGreen:
        mpp.rotate(-92, 50)
        mpp.drive_speed(-7, 80)
        msleep(300)
        mpp.drive_speed(17, 80)  # 14
        msleep(300)
        mpp.rotate(89, 50)
        msleep(300)
        u.smoothLineFollowLeft(5.75, 80)
        msleep(500)
        mpp.rotate(-95, 50)
        mpp.drive_speed(-19.5, 60)
    else:
        mpp.rotate(-90, 50)
        mpp.drive_speed(-7, 80)
        msleep(300)
        mpp.drive_speed(17, 80)  # 14
        msleep(300)
        mpp.rotate(89, 50)
        msleep(300)
        msleep(500)
        mpp.rotate(-90, 50)
        mpp.drive_speed(-20, 80)
    #u.waitForButton()
    mpp.pivot_right(-3, 60)
    #mpp.drive_speed(5.5, 80)
    #if c.isGreen:
    #    mpp.rotate(94.5, 50)
    #else:
    #    mpp.rotate(93, 50)
    #msleep(500)

def driveFinalThreeTrees():
    # Goes from each of the last three trees collecting poms
    print("Collect Final Three Sets of Poms")
    if c.isYellow:
        mpp.drive_speed(3, 40)
        mpp.rotate(-28, 50)
        msleep(1000)
        mpp.drive_timed(-75,-100,1.5)
        u.move_servo(c.servoArmBin, c.armDown, 20)
        u.waitForButton()
        mpp.new_get_poms_timed(50, 7000)
        msleep(1000)
        driveUntilTree()
        mpp.new_get_poms_timed(50, 7000)
        msleep(1000)
        driveUntilTree()
        mpp.new_get_poms_timed(50, 7000)
        msleep(1000)
    if c.isGreen:
        mpp.drive_speed(-3, 40) #was -9.5
        u.waitForButton()
        mpp.rotate(-14, 50)
        mpp.drive_speed(-8, 40)
        u.waitForButton()
        u.move_servo(c.servoArmBin, c.armDown, 20)
        mpp.pivot_right(17, 25)
        mpp.drive_speed(.2, 50)
        u.waitForButton()
        mpp.new_get_poms_timed(50, 9300)
        msleep(1000)
        u.DEBUG()
        driveUntilTree()
        mpp.drive_speed(.2, 50)
        mpp.new_get_poms_timed(50, 9300)
        msleep(1000)
        mpp.pivot_right(-8, 25)  # -8
        mpp.drive_speed(4, 50)
        mpp.pivot_right(8, 25)
        mpp.drive_speed(9.5, 50)
        mpp.pivot_right(4, 25)
        mpp.new_get_poms_timed(50, 9300)
    if c.isBlue:
        u.move_servo(c.servoDateWheel, c.wheelOut, 25)
        mpp.drive_speed(-.4, 80)
        mpp.rotate(10, 80)
        u.move_servo(c.servoArmBin, c.armDown, 25)
        u.move_servo(c.servoPipeWheel, c.pipeBin, 25)
        mpp.pivot_right(13, 85)
        mpp.drive_speed(5, 85)
        driveUntilTree()
        mpp.drive_speed(.3, 70)
        u.move_servo(c.servoDateWheel, c.wheelIn + 100, 30)
        u.move_servo(c.servoDateWheel, c.wheelIn + 70, 10)
        mpp.new_get_poms_timed(95, 7000)
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
        u.move_servo(c.servoArmBin, c.armDown, 25)
        mpp.drive_speed(4, 85)
        driveUntilTree()
        mpp.drive_speed(.2, 70)
        u.move_servo(c.servoDateWheel, c.wheelIn + 100, 30)
        u.move_servo(c.servoDateWheel, c.wheelIn + 50, 10)
        mpp.new_get_poms_timed(95, 20000)

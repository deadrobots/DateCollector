#!/usr/bin/python
import os, sys
from wallaby import *
import actions as act
import utils as u
import constants as c
import drive as x
import drive as d
import motorsPlusPlus as mpp

def main():
    print ("Running code")
    # mpp.drive_speed(24,100)
    # u.waitForButton()
    # mpp.drive_speed(-24,100)
    # u.DEBUG()
    act.init()
    act.driveOutStartBox()
    act.driveFirstTrees()
    act.grabFirstPoms()
    act.driveToNextTrees2()
    u.DEBUG()
    #act.driveToNextTrees()
    act.driveFinalThreeTrees()
    u.DEBUG()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()

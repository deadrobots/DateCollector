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
    #mpp.drive_speed(20, 100)
    #u.waitForButton()
    #mpp.drive_speed(-20, 100)
    act.init()
    act.driveOutStartBox()
    act.driveFirstTrees()
    act.getSecondDateBin()
    act.grabFirstPoms() #this pulls poms on the first 2 trees
    #Work on the driveToNextTrees2 function
    act.driveToNextTrees2()
    #act.driveToNextTrees()
    act.driveFinalThreeTrees()
    u.DEBUG()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()

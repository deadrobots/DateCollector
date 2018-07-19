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
    #########################HEY READ THIS IF UR NOT AJ OR KAT :)###############################
    #So we have both head 2 head and seeding fairly consistent for blue bot
    #We've gotten 4800 max for seeding and 2100 max for head 2 head!!!
    #The next step is to work on the clone (seeding and head 2 head)
    #We've started working on seeding for clone (Green Bot) but we've only finished the first tree
    #So work on that  ^^^^^^^^^^^^^^^
    #We also need to work on Head 2 Head for clone
    #Good Luck!
    print ("Running code")
    #Calibration drive
    # mpp.calibrate_drive()
    # u.DEBUG()
    act.init()
    if u.wait_for_selection():
        #Seeding
        c.startTime = seconds()
        shut_down_in(119.5)
        print("Running Seeding")
        act.driveOutStartBox()
        act.driveFirstTrees()
        act.getSecondDateBin()
        act.grabFirstPoms()
        act.driveToNextTrees()
        act.getThirdDateBin()
        act.driveFinalThreeTrees()
    else:
        #Head 2 Head
        c.startTime = seconds()
        shut_down_in(119.5)
        print("Running Head 2 Head")
        act.driveOutStartBox()
        act.driveFirstTreesH2H()
        act.grabFirstPoms()
        act.driveToNextTrees()
        act.getThirdDateBinH2H()
        act.grabFirstPoms()
    u.DEBUG()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()

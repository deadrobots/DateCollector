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
    print ("Running")
    act.init()
    act.driveOutStartBox()
    u.DEBUG()
    act.driveFirstThreeTrees()
    act.driveToNextTrees()
    act.driveFinalThreeTrees()
    u.DEBUG()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()

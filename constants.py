import wallaby as w

# Time
startTime = -1

# Digital ports
GREEN_CLONE_SWITCH = 9
YELLOW_CLONE_SWITCH = 8
RIGHT_BUTTON = 13

isGreen = w.digital(GREEN_CLONE_SWITCH)
isYellow = w.digital(YELLOW_CLONE_SWITCH)
isBlue = not isGreen and not isYellow

# Motor ports
LMOTOR = 3
RMOTOR = 0
if isBlue:
    DATEMOTOR = 2
else:
    DATEMOTOR = 1

#Analog Ports
ET = 0

# Servos
servoArmBin = 0
servoPipeWheel = 2

# camera channels
ORANGE = 0
RED = 1
GREEN = 2
YELLOW = 3

# color tolerances
COLOR_PROXIMITY = 20
ORANGE_AREA = 500
RGY_AREA = 100

# Tophat
LEFT_TOPHAT = 5
RIGHT_TOPHAT = 4
onBlack = 2000

#ET
onTree = 2000

if isGreen:
    # Servo Positions
    armUp = 530
    armDown = 1100
elif isYellow:
    # Servo Positions
    armUp = 1110
    armDown = 1850
elif isBlue:
    armUp = 1580
    armDown = 1010
    pipeBin = 1500
    pipeStraight = 2000
    pipeOut = 890

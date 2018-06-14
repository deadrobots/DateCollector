import wallaby as w

# Time
startTime = -1

# Motor ports
LMOTOR = 3
RMOTOR = 0
DATEMOTOR = 1

# Digital ports
GREEN_CLONE_SWITCH = 9
YELLOW_CLONE_SWITCH = 8
RIGHT_BUTTON = 13

#Analog Ports
ET = 0

isGreen = w.digital(GREEN_CLONE_SWITCH)
isYellow = w.digital(YELLOW_CLONE_SWITCH)
isBlue = not isGreen and not isYellow

# Servos
servoArmBin = 0

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
FRONT_TOPHAT = 5
SIDE_TOPHAT = 6
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

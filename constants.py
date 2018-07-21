import wallaby as w
# Time
startTime = -1

# Digital ports
GREEN_CLONE_SWITCH = 9
YELLOW_CLONE_SWITCH = 8
RIGHT_BUTTON = 13
ALLOW_BUTTON_WAIT = True

isGreen = w.digital(GREEN_CLONE_SWITCH)
isYellow =  False
'''w.digital(YELLOW_CLONE_SWITCH)'''
isBlue = not isGreen and not isYellow

# Motor ports
LMOTOR = 3
RMOTOR = 0
if isBlue:
    DATEMOTOR1 = 1
    DATEMOTOR2 = 2
elif isGreen:
    DATEMOTOR1 = 2  #was 1
    DATEMOTOR2 =  1
elif isYellow:
    DATEMOTOR1 = 1
    DATEMOTOR2 = 2

#Analog Ports
ET = 0
LightSensor = 5

# Servos
servoArmBin = 1
servoPipeWheel = 2
servoDateWheel = 3

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
LEFT_TOPHAT = 1
RIGHT_TOPHAT = 4
onBlack = 2000

#ET
onTree = 2000

if isGreen:
    # Servo Positions
    armUp = 1000
    armDown = 400
    wheelOut = 2047
    wheelIn = 1600 #1560
    pipeStraight = 2047
    pipeOut = 890
    pipeBin = 1600 #1500
elif isYellow:
    # Servo Positions
    armUp = 1110
    armDown = 1850
    wheelIn = 1320
    wheelOut = 1900
    pipeBin = 560
    pipeStraight = 1100   #1100
    pipeOut = 50
elif isBlue:
    armUp = 1500
    armDown = 900
    pipeBin = 1500
    wheelIn = 1500 #1460
    wheelOut = 1950
    pipeStraight = 2047
    pipeOut = 890

from wallaby import *
import constants as c
import motorsPlusPlus as x
import actions as a


def cameraInit():
    #Initializes/Opens up camera
    print("Running!")
    if camera_open_black() == 0:
        print("camera does not open")
        exit(0)
    else:
        print("camera open")
    if camera_update() == 0:
        print("no update")
    else:
        print("update")
    i=0
    while(i < 5):
        camera_update()
        i+=1
        msleep(600)


def getCenterColorAvg():
    #Determines what color block is within the orange card
    #This uses mode of the returned colors..
    i = 0
    while (i < 5):
        camera_update()
        i += 1
        msleep(60)
    redCount = 0
    greenCount = 0
    yellowCount = 0
    startTime = seconds()
    while (seconds() - startTime < .5):
        camera_update()
        msleep(50)
        if get_object_count(c.ORANGE) > 0 and get_object_area(c.ORANGE,0) > c.ORANGE_AREA:
            print(" ")
            print("color proximity:" + str(colorProximity(c.RED)))
            print("get obj area:" + str(get_object_area(c.RED,0)))
            print("get obj count:" + str((get_object_count(c.RED) > 0)))

            if get_object_count(c.YELLOW) > 0 and get_object_area(c.YELLOW,0) > c.RGY_AREA and colorProximity(c.YELLOW):
                yellowCount += 1
            if (get_object_count(c.GREEN) > 0) and get_object_area(c.GREEN,0) > c.RGY_AREA and colorProximity(c.GREEN):
                greenCount += 1
            if (get_object_count(c.RED) > 0) and get_object_area(c.RED,0) > c.RGY_AREA and colorProximity(c.RED):
                redCount += 1
        else:
            print("I see approximately no orange")
    print("Colors are:")
    print(redCount)
    print(greenCount)
    print(yellowCount)
    print("what it returns is:")

    if max(redCount, greenCount, yellowCount)==0:
        return 0
    elif max(redCount, greenCount, yellowCount) == greenCount:
        return c.GREEN
    elif max(redCount, greenCount, yellowCount) == redCount:
        return c.RED
    elif max(redCount, greenCount, yellowCount) == yellowCount:
        return c.YELLOW

def colorProximity(color):
    #Tests to see if the center of the colored block is within a certain proximity to the center of the orange card
    if abs(get_object_center_x(color, 0)- get_object_center_x(c.ORANGE,0)) < c.COLOR_PROXIMITY:
        return True
    return False

def colorValue(color):
    #Prints data (x,y,area) of the selected color channel
    print(colorDefine(color))
    print("objects=" + str(get_object_count(color))),
    print(", x=" + str(get_object_center_x(color, 0))),
    print(", y=" + str(get_object_center_y(color, 0))),
    print(", area=" + str(get_object_area(color, 0)))

def colorDefine(color):
    #Converts channel number to color
    if color==c.ORANGE:
        return "Nothing"
    elif color==c.RED:
        return "RED"
    elif color==c.GREEN:
        return "GREEN"
    elif color==c.YELLOW:
        return "YELLOW"

def determineOrder(list):
    #Logic to determine which color block is in which place
    #If one of the first two spots checked is empty, robot drives to final scoring zone to check last color
    #Prints a list with order of colors
    if c.RED in list and c.GREEN in list:
        list.append(c.YELLOW)
    elif c.GREEN in list and c.YELLOW in list:
        list.append(c.RED)
    elif c.RED in list and c.YELLOW in list:
        list.append(c.GREEN)
    elif c.ORANGE in list:
        x.line_follow_forward(23)
        checkColor(list)
        n = list.index(c.ORANGE)
        print(n)
        if c.RED in list and c.GREEN in list:
            list[n] = c.YELLOW
        elif c.GREEN in list and c.YELLOW in list:
            list[n] = c.RED
        elif c.RED in list and c.YELLOW in list:
            list[n] = c.GREEN
        print(list[n])
    print("final order: "),
    print([colorDefine(list[0]), colorDefine(list[1]), colorDefine(list[2])])


def checkColor(list):
    #Finds color and adds it to the list
    s = getCenterColorAvg()
    list.append(s)
    print(list[-1])
    return list[-1]

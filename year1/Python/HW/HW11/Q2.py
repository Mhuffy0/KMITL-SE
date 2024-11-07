import turtle
import math

def RobotBattle():
    robotList = [];
    turtle.speed(0)
    while True:
        turtle.clear()
        for robot in robotList:
            robot.draw()

        print("==== Robots ====")
        i=0
        for robot in robotList:
            print(i, " : ", )
            robot.displayStatus()
            i += 1
        print("================")

        choice = input("Enter which robot to order, 'c' to create new robot, 'q' to quit: ")
        if choice == "q":
            break
        elif choice == "c":
            print("Enter type of robots to create")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikerBot: ")
            if robotType == "r":
                newRobot = Robot()
            elif robotType == "m":
                newRobot = MedicBot()
            elif robotType == "s":
                newRobot = StrikerBot()
            robotList = robotList + [newRobot]
        else:
            if len(robotList) >= 1:    
                n = int(choice)
                robotList[n].command(robotList)
            else:
                print("Create Some Robot")
                continue
        i = 0
        for robot in robotList:
            if (robot.health <= 0):
                del robotList[i]
            i += 1
    
    # turtle.done()
            


class Robot(object):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.health = 100
        self.energy = 100
    def move(self, x, y):
        if self.energy - 10 >= 0:
            self.energy -= 10
            self.x = x
            self.y = y
    def draw(self):
        self.dw = turtle.Turtle()
        self.dw.speed(0)
        self.dw.penup()
        self.dw.goto(self.x,self.y)
        self.dw.pendown()
        self.dw.circle(50)
    def displayStatus(self):
        print(f"x= {self.x}, y= {self.y}, health= {self.health}, energy= {self.energy}")
    def command(self, robotList):
        print("Possible actions: move")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX, newY)

class MedicBot(Robot):
    def __init__(self):
        super().__init__()
    def heal(self, r):
        distance = math.sqrt(((r.x - self.x)**2) + ((r.y - self.y)**2))
        if self.energy >= 20 and distance <= 10:
            self.energy -= 20
            r.health += 10
    def command(self, robotList):
        option = input("What you want to action [m-move] [h-heal]: ")
        match option:    
            case "m":
                super().command(robotList)
            case "h":
                rob = int(input("Which robot want to heal: "))
                self.heal(robotList[rob])
            case _:
                print("Not in option")

class StrikerBot(Robot):
    def __init__(self):
        super().__init__()
        self.missile = 5
    def strike(self,r):
        distance = math.sqrt(((r.x - self.x)**2) + ((r.y - self.y)**2))
        if self.energy >= 20 and self.missile > 0 and distance <= 10:
            self.energy -= 20
            self.missile -= 1
            r.health -= 50
        else:
            print("Out-of-range")
    def displayStatus(self):
        print(f"x= {self.x}, y= {self.y}, health= {self.health}, energy= {self.energy}, missile= {self.missile}")
    def command(self, robotList):
        option = input("What you want to action [m-move] [s-strike]: ")
        match option:    
            case "m":
                super().command(robotList)
            case "s":
                rob = int(input("Which robot want to strike: "))
                self.strike(robotList[rob])
            case _:
                print("Not in option")

RobotBattle()
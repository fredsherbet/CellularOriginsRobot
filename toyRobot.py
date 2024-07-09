#!/usr/bin/env python3
import sys

# Information about 'the world' (not the robot) is contained here
WORLD_DATA = {
        "DIRECTIONS":
        {
            "NORTH": {
                "LEFT": "WEST",
                "RIGHT": "EAST",
                "MOVE": [0, 1]
            },
            "SOUTH": {
                "LEFT": "EAST",
                "RIGHT": "WEST",
                "MOVE": [0, -1]
            },
            "EAST": {
                "LEFT": "NORTH",
                "RIGHT": "SOUTH",
                "MOVE": [1, 0]
            },
            "WEST": {
                "LEFT": "SOUTH",
                "RIGHT": "NORTH",
                "MOVE": [-1, 0]
            }
        },
        "GRID": [5, 5]
}

class ToyRobot:
    def __init__(self):
        self.active = False
        self.position = None
        self.direction = None

    def move(self) -> None:
        if not self.active:
            return
        move = WORLD_DATA["DIRECTIONS"][self.direction]["MOVE"]
        x = self.position[0] + move[0]
        y = self.position[1] + move[1]
        if 0 <= x < WORLD_DATA["GRID"][0] and 0 <= y < WORLD_DATA["GRID"][1]:
            self.position = (x, y)

    def left(self) -> None:
        if not self.active:
            return
        self.direction = WORLD_DATA["DIRECTIONS"][self.direction]["LEFT"]

    def right(self) -> None:
        if not self.active:
            return
        self.direction = WORLD_DATA["DIRECTIONS"][self.direction]["RIGHT"]

    def place(self, x: int, y: int, direction: str) -> None:
        if self.active:
            return
        if not (0 <= x < WORLD_DATA["GRID"][0] and 0 <= y < WORLD_DATA["GRID"][1]):
            print("Invalid position. Position should be within {}x{} grid.".format(WORLD_DATA["GRID"][0], WORLD_DATA["GRID"][1]))
            return
        if direction not in WORLD_DATA["DIRECTIONS"]:
            print("Invalid direction. Use one of NORTH, SOUTH, EAST, WEST.")
            return

        self.position = (x, y)
        self.active = True
        self.direction = direction

    def report(self) -> None:
        if not self.active:
            return
        print(self.position[0], self.position[1], self.direction)


def main(args = None) -> None:
    # Create an instance of ToyRobot
    robot = ToyRobot()
    while True:
        try:
            if args:
                command = args[0]
                if (command == "PLACE"):
                    args.pop(0)
                    command = command + " " + args[0]
                args.pop(0)
            else:
                command = input("Enter command to control robot: ")
            if command == "EXIT":
                return 0
            elif command == "REPORT":
                robot.report()
            elif command == "MOVE":
                robot.move()
            elif command == "LEFT":
                robot.left()
            elif command == "RIGHT":
                robot.right()
            else:
                command = command.split()
                if len(command) == 2:
                    if command[0] == "PLACE":
                        x, y, direction = command[1].split(",")
                        robot.place(int(x), int(y), direction)
                    else:
                        print("Invalid command. Use one of REPORT, MOVE, LEFT, RIGHT, PLACE x,y,direction.")
                elif len(command) == 1:
                    if command[0] == "PLACE":
                        print("Invalid command. Use PLACE x,y,direction.")
                    else:
                        print("Invalid command. Use one of REPORT, MOVE, LEFT, RIGHT, PLACE x,y,direction.")
                else:
                    print("Invalid command. Use one of REPORT, MOVE, LEFT, RIGHT, PLACE x,y,direction.")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main(sys.argv[1:])

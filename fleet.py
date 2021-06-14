from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        walle = Robot("Wall-E", 5)
        optimus = Robot("Optimus Prime", 10)
        r2d2 = Robot("R2-D2", 5)
        self.robots.append(walle)
        self.robots.append(optimus)
        self.robots.append(r2d2)


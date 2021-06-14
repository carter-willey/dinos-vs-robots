from herd import Herd
from fleet import Fleet
import time

class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def run_game(self):
        pass
    def display_welcome(self):
        print("Welcome to the ultimate battle between dinosaurs and robots!")
        time.sleep(1.5)
        print("Let's begin")
        print("Dinosaurs attack first")
    def battle(self):
        #we want to alternate dino and robot.
        #if health = 0 we should remove that dino/robot from the list
        game_state = True
        if len(self.fleet.robots) == 0 or len(self.herd.dinosaurs) == 0:
            game_state = False


        pass
    def dino_turn(self, dinosaur):
        robot_to_attack_response = int(input("Robot's number?: "))
        robot_being_attacked = self.fleet.robots[robot_to_attack_response - 1]
        dinosaur.attack(robot_being_attacked)
        #if robot_being_attacked.health <= 0:

        print(self.fleet.robots[attack_response-1].health)
        print(self.fleet.robots[attack_response-1].name)

    def robo_turn(self, robot):
        dino_to_attack_response = int(input("Dinosaur's number?: "))
        dino_being_attacked = self.herd.dinosaurs[dino_to_attack_response - 1]
        robot.attack(dino_being_attacked)
    def show_dino_opponent_options(self):
        print("Which robot would you like to attack?")
        i = 1
        for robot in self.fleet.robots:
            print(f"{i}. {robot.name} - {robot.health}HP")
            i += 1
    def show_robo_opponent_options(self):
        print("Which dinosaur would you like to attack?")
        i = 1
        for dinosaur in self.herd.dinosaurs:
            print(f"{i}. {dinosaur.type} - {dinosaur.health}HP")
            i += 1
    def display_winners(self):
        pass
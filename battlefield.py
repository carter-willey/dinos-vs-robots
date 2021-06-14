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
        game_state = True
        dino_attackers = True

        dino_attacker_index = 0
        robots_attacker_index = 0
        while game_state:
            
            self.dino_turn(self.herd.dinosaurs[dino_attacker_index])
            dino_attacker_index += 1
            self.robo_turn(self.fleet.robots[robots_attacker_index])
            robots_attacker_index += 1

        # if len(self.fleet.robots) == 0 or len(self.herd.dinosaurs) == 0:
        #  game_state = False

    def dino_turn(self, dinosaur):

        print(f"{dinosaur.type}'s turn to attack!")
        self.show_dino_opponent_options()
        robot_to_attack_response = int(input("Robot's number?: "))
        time.sleep(.75)
        robot_being_attacked = self.fleet.robots[robot_to_attack_response - 1]
        dinosaur.attack(robot_being_attacked)
        time.sleep(1.25)

    def show_dino_opponent_options(self):
        print("Which robot would you like to attack?")
        i = 1
        for robot in self.fleet.robots:
            print(f"{i}. {robot.name} - {robot.health}HP")
            i += 1

    def robo_turn(self, robot):
        print(f"{robot.name}'s turn to attack!")
        self.show_robo_opponent_options()
        dino_to_attack_response = int(input("Dinosaur's number?: "))
        time.sleep(.75)
        dino_being_attacked = self.herd.dinosaurs[dino_to_attack_response - 1]
        robot.attack(dino_being_attacked)
        time.sleep(1.25)

    def show_robo_opponent_options(self):
        print("Which dinosaur would you like to attack?")
        i = 1
        for dinosaur in self.herd.dinosaurs:
            print(f"{i}. {dinosaur.type} - {dinosaur.health}HP")
            i += 1

    def display_winners(self):
        pass

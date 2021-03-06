from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        trex = Dinosaur("T-Rex", 40)
        stego = Dinosaur("Stegosaurus", 40)
        ceratops = Dinosaur("Triceratops", 20)
        self.dinosaurs.append(trex)
        self.dinosaurs.append(stego)
        self.dinosaurs.append(ceratops)

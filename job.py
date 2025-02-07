class Part:
    def __init__(self, name, materials):
        self.name = name
        self.materials = materials

    def change_materials(self, new_material):
        self.materials = new_material

    def __str__(self):
        return f"name_material : {self.name}, new_material : {self.materials}"
        
class Ship:
    def __init__(self, name, part):
        self.name =name
        self.__part = part

    def get_part(self):
        return self.__part
    
    def set_part(self, part):
        self.__part = part

    def display_state(self):
        return f"name : {self.name}, part : {self.get_part()}"

    def replace_part(self, part_name, new_part):
        dict_part = self.get_part()
        print(dict_part)
        
class RacingShip(Ship):
    def __init__(self, name, part, speed):
        super().__init__(name, part)
        self.speed = speed
    
    def display_speed(self):
        print( self.display_state() + f", la vitesse maximale est de : {self.speed}")
        



part1 = Part("mat", "bois")
part2 = Part("voile", "tissu")
race_ship = RacingShip("argonaute",part1, 15)

race_ship.set_part(part1)
race_ship.set_part(part2)

race_ship.display_state()
race_ship.display_speed()

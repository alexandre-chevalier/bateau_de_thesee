class Part:
    def __init__(self, name, materials):
        self.name = name
        self.materials = materials

    def change_materials(self, new_material):
        self.materials = new_material

    def __str__(self):
        return f"name_material : {self.name}, new_material : {self.materials}"

    def __repr__(self):
        return f"Part(name={self.name}, materials={self.materials})"


class Ship:
    def __init__(self, name):
        self.name =name
        self.__part = {}

    def get_part(self):
        return self.__part
    
    def add_part(self, part):
        self.get_part()[part.name] = part
        

    def display_state(self):
        parts = ', '.join(str(part) for part in self.__part.values())
        return f"Name: {self.name}, Parts: [{parts}]"

    def history_part(self, old_part, new_part):
        list_modif = f"cette piece :  {old_part} a ete remplacer par celle ci :{new_part}, "
        self.history.append(list_modif)
        print(self.history)

    def replace_part(self, part_name, new_part):
        dict_part = self.get_part()
        if part_name in dict_part:
            dict_part[part_name] = new_part
            self.history_part(part_name, new_part.name)
        else:
            print(f"cette piece {part_name} n'a pas ete trouvé")
        


class RacingShip(Ship):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed
        self.history = []
    
    def display_speed(self):
        print( self.display_state() + f", la vitesse maximale est de : {self.speed}")
        
part1 = Part("mat", "bois")
part2 = Part("voile", "tissu")
part3 = Part("ancre", "soie")
part4 = Part("gouvernail", "acier")
race_ship = RacingShip("argonaute", 15)

race_ship.add_part(part1)
race_ship.add_part(part2)
race_ship.replace_part(part2.name, part3)
race_ship.replace_part(part1.name, part4)
race_ship.display_state()
race_ship.display_speed()

for i in race_ship.history:
    print(i)

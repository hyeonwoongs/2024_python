# # marine, attack unit, soldier. can use a gun
# name = "marine"
# hp = 30
# damage = 5
#
# print("{0} unit is produced.".format(name))
# print("hp is {0}, damage is {1}.\n".format(hp, damage))
#
# # tank, attack unit, tank. can fire a cannon.(normal mode / siege mode)
# tank_name = "tank"
# tank_hp = 100
# tank_damage = 30
#
# print("{0} unit is produced.".format(tank_name))
# print("hp is {0}, damage is {1}.\n".format(tank_hp, tank_damage))
#
# tank2_name = "tank"
# tank2_hp = 100
# tank2_damage = 30
#
# print("{0} unit is produced.".format(tank2_name))
# print("hp is {0}, damage is {1}.\n".format(tank2_hp, tank2_damage))
#
# def attack(name, location, damage):
#     print("{0} : attack {1} direction. [damage {2}]".format\
#               (name, location, damage))
#
# attack(name, "1am", damage)
# attack(tank_name, "1am", tank_damage)
# attack(tank2_name, "1am", tank2_damage)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} unit is produced.".format(self.name))
        print("hp is {0}, damage is {1}\n".format(self.hp, self.damage))

marine1 = Unit("marine", 30, 5)
marine2 = Unit("marine", 30, 5)
tank = Unit("tank", 100, 30)

#wraith : flying unit, flight. clocking (hidden)
wraith1 = Unit("wraith", 40, 20)
print("unit name : {0}, damage : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("wraith", 40, 20)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} is hidden.".format(wraith2.name))
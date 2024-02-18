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

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} unit is produced.".format(self.name))
#         print("hp is {0}, damage is {1}\n".format(self.hp, self.damage))

class AttackUnit:
    def __init__(self,name, hp, damage):
            self.name = name
            self.hp = hp
            self.damage = damage

    def attack(self, location):
        print("{0} : attack {1} direction. [damage {2}]\n"\
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} is attacked. [damage {1}]".format(self.name, damage))
        self.hp -= damage
        print("remain hp of {0} is {1}.\n".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} unit is died.".format(self.name))


fireblamer1 = AttackUnit("fireblamer", 100, 30)
fireblamer1.attack("1am")

glazepenguine1 = AttackUnit("glazepenguine", 80, 40)
glazepenguine1.damaged(20)
glazepenguine1.damaged(20)
glazepenguine1.damaged(20)
glazepenguine1.damaged(20)
class Pokemon:
     def __init__(self, name):
          self.name = name


#class Pikachu:
class Pikachu(Pokemon): # is-a
     pass

p1 = Pikachu("피카츄")
print(p1.name)
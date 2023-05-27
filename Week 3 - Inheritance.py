class FarmAnimal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def eat(self):
        pass
    
    def sleep(self):
        pass

class Cow(FarmAnimal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
        
    def moo(self):
        print("The cow moo's.")
        
    def eat(self):
        print("The cow is eating.")
        
class Chicken(FarmAnimal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
        
    def cluck(self):
        print("The chicken begins clucking around.")
        
    def eat(self):
        print("The chicken is eating grain.")
        
class Sheep(FarmAnimal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
        
    def baa(self):
        print("The sheep starts to baa.")
        
    def eat(self):
        print("The sheep is eating.")
        
def farm_test():
    cow = Cow("Bessie","5","Brown")
    chicken = Chicken("Henny","1","White")
    sheep = Sheep("Tom","4","Black")
    
    cow.moo()
    chicken.cluck()
    sheep.baa()
    print()
    print("The",cow.color,"cow's name is", cow.name, "and is", cow.age, "year(s) old.")
    print("The",chicken.color,"chicken's name is", chicken.name, "and is", chicken.age, "year(s) old.")
    print("The",sheep.color,"sheep's name is", sheep.name, "and is", sheep.age, "year(s) old.")

farm_test()


"""
PART B

1. The parent class is Spell, while the child classes are Accio and Confundo
2. The base class is Spell, while the sub-classes are Accio and Confundo
3. The output of this code is such:

Accio
Summoning Charm Accio
No description
Confundo Confundus Charm
Causes the victim to become confused and befuddled.

4. When study_spell(Confundo()) is executed, get_description method of the Confundo class is
called since Confundo is an instance of the Confundo Class

5. class Accio(Spell):
    def __init__(self):
        Spell.__init__(self,"Accio", "Summoning Charm")
    
    def get_description(self):
        return "This charm summons an object to the caster, potentially over a significant distance"
"""
        
        
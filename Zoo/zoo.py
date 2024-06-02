# Name:Tala khaled
# Email:talakh1798@gmail.com

class Animal:
    def __init__(self,name , age , health_level,happiness):
        self.name=name
        self.age=age
        self.health_level=health_level
        self.happiness=happiness

    def display_info(self) :
        print(f"Animal Name : {self.name} Health : {self.health_level} Happines : {self.happiness}") 

    def feed(self):
        self.health_level+=10
        self.happiness+=10

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health_level=60, happiness=70)
        self.color="Gold"

    def feed(self):
        super().feed()

class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health_level=40, happiness=70)
        self.color="Orange"

    def feed(self):
       super().feed()

class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health_level=60, happiness=35) 

    def feed(self):
       super().feed()              

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name , age):
        self.animals.append( Lion(name ,age) )
    def add_tiger(self, name ,age):
        self.animals.append( Tiger(name , age ) )
    def add_bear(self, name, age): 
        self.animals.append(Bear(name, age))
    
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala ",6)
zoo1.add_lion("Simba",7)
zoo1.add_tiger("Rajah",8)
zoo1.add_tiger("Shere Khan",9)
zoo1.print_all_info()
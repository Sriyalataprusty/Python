# Composition 

class Engine:
    
    def __init__(self, cc):
        self.power = cc
        
    def starting(self):
        print(f"The {self.power}cc engine is starting. ")

class Car:
    car_engine = Engine
    
    def __init__(self):
        self.engine =  self.car_engine(165)   
        
    def driving(self,name):
        self.name = name
        print(f"{self.name} is driving a car. ")

farari = Car()
farari.driving("Tuin")
farari.engine.starting()

# class Car(Engine):
        
#     def driving(self,name):
#         self.name = name
#         print(f"{self.name} is driving the car. ")

# farari = Car(200)
# farari.driving("Tuin")
# farari.starting()
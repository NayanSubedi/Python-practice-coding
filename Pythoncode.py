class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

class Bugatti(Car):
    def __init__(self):
        color = input("What color is your Bugatti? : ")
        super().__init__(color, "Bugatti")
        self.OwnerName = input("Enter the OwnerName of Bugatti : ")
        self.ModelName= input("Enter the model name of Bugatti: ")
        self.Engine_capacity = input("Enter the Engine capacity of Bugatti: ")
        self.TopSpeed = input("Enter the TopSpeed of Bugatii in KM/H: ")
        self.Horsepower = input("Enter the horsepower of Bugatti: ")

class Ferrari(Car):
    def __init__(self):
        color = input("What color is your Ferrari?: ")
        super().__init__(color, "Ferrari")
        self.OwnerName = input("Enter the OwnerName of Bugatti : ")
        self.ModelName= input("Enter the model name of Ferrari: ")
        self.Engine_capacity = input("Enter the Engine capacity of Ferrari: ")
        self.TopSpeed = input("Enter the TopSpeed of Ferrari in KM/H: ")
        self.Horsepower = input("Enter the horsepower of Ferrari: ")

class Lamborghini(Car):
    def __init__(self):
        color = input("Enter the color of Lamborghini: ")
        super().__init__(color, "Lamborghini")
        self.OwnerName = input("Enter the OwnerName of Lamborghini : ")
        self.ModelName= input("Enter the model name of Lamborghini: ")
        self.Engine_capacity = input("Enter the Engine capacity of Lamborghini: ")
        self.TopSpeed = input("Enter the TopSpeed of Lamborghini in KM/H: ")
        self.Horsepower = input("Enter the Horsepower of Lamborghini: ")

bugatti = Bugatti()
print("Brand:", bugatti.brand)
print("Color:", bugatti.color)
print("OwnerName:", bugatti.OwnerName)
print("ModelName:", bugatti.ModelName)
print("Engine_capacity:", bugatti.Engine_capacity)
print("TopSpeed:", bugatti.TopSpeed)
print("Horsepower:", bugatti.Horsepower)

ferrari = Ferrari()
print("Brand:", ferrari.brand)
print("Color:", ferrari.color)
print("OwnerName:", ferrari.OwnerName)
print("ModelName:", ferrari.ModelName)
print("Engine_capacity:", ferrari.Engine_capacity)
print("TopSpeed:", ferrari.TopSpeed)
print("Horsepower:", ferrari.Horsepower)

lamborghini = Lamborghini()
print("Brand:", lamborghini.brand)
print("Color:", lamborghini.color)
print("OwnerName:", lamborghini.OwnerName)
print("ModelName:", lamborghini.ModelName)
print("engine_capacity:", lamborghini.Engine_capacity)
print("topSpeed:", lamborghini.TopSpeed)
print("horsepower:", lamborghini.Horsepower)
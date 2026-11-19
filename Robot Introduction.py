class Robot:
    species = "robot"

    def __init__(self, name, battery):
        self.name = name
        if battery < 0:
            battery = 0
        self.battery = battery

    def introduce(self):
        return f"My name is {self.name}. I am a robot."

    def show_battery(self):
        return f"{self.name} has {self.battery}% battery."

    def charge(self):
        if self.battery < 100:
            self.battery = 100
        return f"{self.name} is now fully charged."


tom = Robot("Tom", 75)
jerry = Robot("Jerry", 40)

print(tom.introduce())
print(jerry.introduce())

print(tom.show_battery())
print(jerry.show_battery())

print(tom.charge())
print(jerry.charge())

print(tom.show_battery())
print(jerry.show_battery())





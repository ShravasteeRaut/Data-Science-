class Parrot:
    species = "bird"                                          
    def __init__(self, name, age):                             
        self.name = name
        if age < 0:                                            
            age = 0
        self.age = age

    def sing(self, song):
        if song == "":
            return f"{self.name} hums quietly."
        return f"{self.name} sings {song}"

    def dance(self):
        return f"{self.name} is now dancing"

    def birthday(self):
        self.age = self.age + 1
        return self.age


parrot_name = input("Name of the first parrot? ")
blu = Parrot(parrot_name, 10)                                       
woo = Parrot("Woo", 15)
song = input("Which song does the parrot sing? ")
print(blu.sing(song))                                       
print(blu.sing(""))                                           
print(blu.dance())
print("After the birthday", blu.name, "is", blu.birthday())
print(woo.name, "is still", woo.age)                           

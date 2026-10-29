import datetime

name = input("Enter your name: ")
mood = input("How are you feeling today? (happy/sad/stressed): ")
energy = int(input("Enter your energy level (1-10): "))

now = datetime.datetime.now()

print("\nHello,", name)
print("Date and Time:", now)

if mood == "happy":
    print("Advice: Keep smiling and spread happiness!")

elif mood == "sad":
    print("Advice: Take a break and do something you enjoy!")

elif mood == "stressed":
    print("Advice: Stay calm and take a few deep breaths!")

else:
    print("Advice: Stay positive and take care of yourself!")

if energy >= 7:
    print("Energy Level: High - Great time to complete your tasks!")

elif energy >= 4:
    print("Energy Level: Medium - Take small breaks while working!")

else:
    print("Energy Level: Low - Rest and recharge yourself!")

print("Have a wonderful day,", name + "!")
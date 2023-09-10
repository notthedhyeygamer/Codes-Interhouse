#Made By Dhyey Dave
#First we let the user give an input

num1 = int(input("Enter 1 for log and 2 to retrieve: "))
a = int(input("Enter 1 for Harry, 2 for Rohan: "))
b = int(input("Enter 1 for food and 2 for exercise: "))

def getdate(): #This function helps us to get the date and time
    import datetime
    return datetime.datetime.now()

if num1 == 1 and a == 1 and b == 1: #Here we code what to do to harry's food diet if the user presses 1 to log
    f = open("harryfood.txt","a")
    inp = str(input("Enter the food harry ate: "))
    time = str(getdate())
    print("["+time+"]"+inp+"\n")
    print("Item added successfully")
    f.close()
elif num1 == 1 and a == 1 and b == 2: #Here we code what to do to harry's exercises if the user presses 1 to log
    f1 = open("harryexercise.txt","a")
    inp1 = str(input("Enter the exercise harry did: "))
    time = str(getdate())
    print("["+time+"]"+inp1+"\n")
    print("Item added successfully")
    f1.close()
elif num1 == 1 and a == 2 and b == 1: #Here we code what to do to rohan's food diet if the user presses 1 to log
    f2 = open("rohanfood.txt","a")
    inp2 = str(input("Enter the food rohan ate: "))
    time = str(getdate())
    print("["+time+"]"+inp2+"\n")
    print("Item added successfully")
    f2.close()
elif num1 == 1 and a == 2 and b == 2: #Here we code what to do to rohan's exercises if the user presses 1 to log
    f3 = open("rohanfood.txt","a")
    inp3 =str(input("Enter the exercise rohan did: "))
    time = str(getdate())
    print("["+time+"]"+inp3+"\n")
    print("Item added successfully")
    f3.close()

#Here we code what to do if the user wants to retrieve inforation about harry or rohans food diet or exercise plan
if num1 == 2:
    if a == 1 and b == 1:
        f = open("harryfood.txt", "rt")
        print(f.read())
        f.close()
    elif a == 1 and b == 2:
        f1 = open("harryexercise.txt", "rt")
        print(f1.read())
        f1.close()
    elif a == 2 and b == 1:
        f2 = open("rohanfood.txt", "rt")
        print(f2.read())
        f2.close()
    elif a == 2 and b== 2:
        f3 = open("rohanexercise.txt", "rt")
        print(f3.read())
        f3.close()
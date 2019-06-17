import math
def plus(x, y):
    print(x + y)
def minus(x, y):
    print(x - y)
def division(x, y):
    print(x/y)
def multiplikation(x, y):
    (x * y)
def upphojt(x, y):
    print(x**y)
def roten(x):
    print(math.sqrt(a))
    
def plus(x, y, z):
    print(x + y + z)
def minus(x, y, z):
    print(x - y - z)
def division(x, y, z):
    print(x/y/z)
def multiplikation(x, y, z):
    print(x*y*z)
    

print("Vilket räknesätt vill du använda")
print("1. plus")
print("2. minus")
print("3. division")
print("4. multiplikation")
print("5. upphöjt")
print("6. roten")

val = input("Skriv (1,2,3,4,5,6) beroende på vilket räknesätt du vill använda")
if val == "6":
    a = int(input("Skriv in ett tal"))
else:
    tal1= int(input("Första talet"))
    tal2= int(input("Andra talet"))
    if val == "1" or "2" or "3" or "4":
        tal3 = input("Skulle du vilja ha en tredje siffra?")
        if tal3 == "ja" or "Ja":
                z = int(input("Tredje talet"))
                if val == "1":
                    plus(tal1, tal2, z)
                if val == "2":
                    minus(tal1, tal2, z)
                if val == "4":
                    multiplikation(tal1, tal2, z)
                if val == "3":
                    if tal2 or tal3 == 0:
                        print("Man kan inte göra så")
                    else:
                        division(tal1, tal2, z) 
                                
                     
if val == "1":
    plus(x, y)
if val == "2":
    minus(x, y)
if val == "4":
    multiplikation(tal1, tal2)
if val == "3":
    if tal2 == 0:
        print("Man kan inte göra så")
    else:
        division(tal1, tal2) 
if val == "5":
    upphojt(tal1, tal2)
if val == "6":
    if a < 0:
        print("Det funkar inte")
    else:
        roten(a)
    
    



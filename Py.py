from time import sleep
x=("1000")	
hi = ["pistol", "shotgun"]
def ar():
    hi.append("assault rifle")
    print("you now have")
    print(hi)
    sleep(3)
    x1=int(x)-600
    print("your balance is now")
    print(x1)
    
    
def s():
    hi.append("sniper")
    print("you now have")
    print(hi)
    sleep(3)
    x2=int(x)-950
    print("your balance is now")
    print(x2)
    
def pa():
    hi.append("pistol ammo")
    print("you now have")
    print(hi)
    skeep(3)
    x3=int(x)-100
    print("your balance is now")
    print(x3)
    
def stuff():
    print("what would you like to buy?")

    trader=input("1)assault rifle ,2)sniper ,3)pistol ammo")
    if trader=="1":
        ar()
	
	
    elif trader=="2":
        s()

    elif trader=="3":
        pa()

    else:
        print(" we dont sell" + buy_choice + " sorry")

def kill():
    print("you now have")
    hi.append("sniper")
    hi.append("assault rifle")
    hi.append("pistol ammo")
    print("you killed the trader...")
    sleep(2)
    print("damn...")
    sleep(2)
    print("I didn't think anyone wold choose that option, it was just there to make the code longer")
    sleep(5)
    print("well here are your weapons you sick, sick person")
    sleep(5)
    print("you now have")
    print(hi)
    sleep(5)
    print("I hope the zombies get you, it's the least you desserve")
    
	  
print("it is the zombe apocalypse")
sleep(2)
print("you find a local trader on the road")
sleep(2)
print("your balance is ")
print( x )
sleep(2)
print("you have")
sleep(.5)
print(hi) 

print("1)would you like to trade")
sleep(2)
print("or")
sleep(2)
print("2)kill him and take all of his weapons")
z=input("make your choice")

if z=="1":
    stuff()
	
elif z=="2":
    kill()
	
else:
    print("you are supposed to choose either number 1 OR 2")
    print("it's quite simple really")









	
		

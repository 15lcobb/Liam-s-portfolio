from time import sleep #allows sleep to be used
x=("1000") #this is the amount of money the player has

hi = ["pistol", "shotgun"] this is what the player has 

def ar():    #defs allow pieces of code to be inserted into the code using just a word
    hi.append("assault rifle")    #adds assault rifle to the player
    print("you now have")
    print(hi)
    sleep(3)    #this stops the programme for 3 seconds
    x1=int(x)-600    #this changes the amount of money the player has
    print("your balance is now")
    print(x1)
    
    
def s():
    hi.append("sniper")    #adds a sniper to the character
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
    x3=int(x)-100 #adds pistol ammo to the character
    print("your balance is now")
    print(x3)
    
def stuff():
    print("what would you like to buy?")

    trader=input("1)assault rifle ,2)sniper ,3)pistol ammo")    #inputs allow users of the code to chooses an option
    if trader=="1":
        ar()    #uses def ar():
	
	
    elif trader=="2":
        s()    #uses def s():

    elif trader=="3":
        pa()    #uses def pa():

    else:
        print("the question was simple")
	sleep(2)
	print("just type 1,2 or 3")
	
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
    sleep(2)
    print("it's quite simple really")









	
		


# number=int(input("enter any num: "))
# if number>0:
# 	print("it is positive")
# elif number==0:
# 	print("it is zero")
# elif number<0:
# 	print("it is negative")	
# else:
# 	print("nothing")
		

# a=int(input("enter any a :"))
# b=int(input("enter any b: "))
# c=int(input("enter any c: "))
# if a+b>b:
# 	print("valid")
# if a+c>b:
# 	print("valid")
# if c+b>a:
# 	print("valid")


# x=int(input("enter any x: "))
# y=int(input("enter any y: "))
# z=int(input("enter any z: "))
# if x==y==z:
# 	print("equelatuial")
# elif x==y or y==z or z==x:
# 	print("iscoceles")
# else:
# 	print("scalane")


from random import randint # allows you to generate a random number
# variables for the alien
alive = True
stamina = 10
# this function runs each time you attack the alien
def report(stamin):
# syntactic error in if else statements
    if stamin > 8:
        return ("   The alien is strong! It resists your pathetic attack!")
    elif stamin > 5:
        return ("  With a loud grunt, the alien stands firm.")
    elif stamin > 3:
        return  ("   Your attack seems to be having an effect! The alien stumbles!")
    elif stamin > 0:
        return ("  The alien is certain to fall soon! It staggers and reels!")
    else:
        return ("  That's it! The alien is finished!")
print(report(2))

# main function - accepts your input for fight with the alien
def fight(stam): # stamina
    while stam > 0:
      # won't enter this loop ever. The function will always return False.
        response = input("> Enter a move 1.Hit 2.attack 3.fight 4.run")
        if "hit" in response or "attack" in response:
            less = randint(0, stam)
            stam -= less # subtract random int from stamina
            print(report(stam))# see function above
        elif "fight" in response:
            print ("  Fight how? You have no weapons, silly space traveler!")
        elif "run" in response:
            print ("  Sadly, there is nowhere to run."),
            print ("  The spaceship is not very big.")
        else:
            print ("  The alien zaps you with its powerful ray gun!")
            return True
        stam = stam - 1
    return False
fight(2)

print ("     A threatening alien wants to fight you!\n")
# quotes at the end.

# call the function - what it returns will be the value of alive
alive = fight(4)
if alive == True: # means if alive == True
    print ("    \nThe alien lives on, and you, sadly, do not.\n")
else:
    print ("    \nThe alien has been vanquished. Good work!\n")
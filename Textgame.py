print("Welcome to my first game!")

name = input("What's your name? ")
print("Hello, ", name)
age = int(input("What is your age? "))

health = 10


if age >= 18:
    print("You are old enough to play.")
    wants_to_play = input("Do you want to play? (yes/no) ").lower()
    if wants_to_play == "yes":
        print("You are starting with", health, "health")
        print("Lets Play!")

        left_or_right = input("First choice....Left or Right? (left/right) ").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake....do you swim across or go around? (across/around) ").lower()

            if ans == "around":
                print("You go around and reached the other side of the lake.")
            elif ans == "across":
                print("You managed to get across but were bit by a fish and lost 5 health")
                health -= 5
                print("Your health is at", health)     


            ans = input("You notice a house and a river. Which do you go to? (river/house) ").lower()
            if ans == "house":
                print("You've entered the house and are greeted by the owner... He doesn't like you.")
                ans = input("Give him a gift or spit in his eye? (gift/spit) ").lower()
                if ans == "spit":
                    print("He did not like that and hit you over the head with a cane. You lose 5 health.")
                    health -= 5
            
                if health <= 0:
                    print("You now have 0 health and you lose the game...Sucks to suck,", name,)
                else:
                    print("Well,",name, ", your health is", health,  "and you're not dead and im over this so You Win. Congratulations or whatever.")
                    quit()
                
                if ans == "gift":
                    print("He decided not to hit you with a cane. You have", health, "health left. You survived. I don't want to do this anymore, You win,", name,)
            else:
                print("You fell in the river and drowned. Sucks to suck.")    
        else:
            print("You fell in that giant well directly to your right that literally anyone could see. Seriously, how did you miss that? Sucks to suck. Buh bye!")

    else:
        print("Geez, fine. Buh Bye")
else:
    print("You are not old enough to play. I don't know why this is a question in the first place. See ya.")
    
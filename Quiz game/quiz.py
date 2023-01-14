from art import tprint

score=0
total_questions=3

def quiz():
        answer=input("Ready to play? (Y/N): ")
        if answer=="y" or answer=="Y":
            print(" ")
            answer=input("1. When was I born? A: July 2007 B: September 2009 C: July 2008 : ")
            if answer=='c' or answer=='C':
                score += 1
                print("Correct")
            else: 
                print("Wrong")

            print(" ")
            answer=input("2. What is my favourite color? A: Purple B: Blue C: Black : ")
            if answer=='a' or answer=='A':
                score += 1
                print("Correct")
            else: 
                print("Wrong")

            print(" ")
            answer=input("3. Which one is wrong? A: I am a food lover B: I hate sushi C: I like ice cream : ")
            if answer=='b' or answer=='B':
                score += 1
                print("Correct")
            else: 
                print("Wrong")

            print(" ")
            print(" ")
            print("Thanks for playing this simple quiz!")
            point=(score/total_questions)*100
            print(" ")
            print("Questions answered right: ",score)
            print("Points obtained: ", point)
            print(" ")
            print("Bye!")
            print(" ")
            exit()

        elif answer=="n" or answer=="N":
            print(" ")
            print("Not then.")
            print(" ")
            exit() 

        else:
            print(" ")
            quiz()

print(" ")
print(" ")
tprint("Made by Bruno")
print(" ")
print("Welcome to Bruno's epic quiz game.")
print(" ")
quiz()
            

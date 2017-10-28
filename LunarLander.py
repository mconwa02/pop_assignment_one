''' Michelle Conway MCONWA02'''

# altitude  = a  #metres
# velocity  = v  #metres/second
# fuel      = f  #Litres

import math 

def my_game(a,v,f):
    print("Your altitude is " + str(round(a, 2)) +" metres above the moon")
    print("Your velocity is " + str(round(v, 2)) + " metres/second towards the moon")
    print("You have "+ str(round(f, 2)) +" litres of fuel reamaining")
    print("Do you want to play?")
    v += 1.6 
    a -= v
    f -= 1
    s = input()
    if s[0] == 'y' or s[0] == 'Y':
        while a > 0 and f >0:
            print("Your altitude is " + str(round(a, 2)) +" metres above the moon")
            print("Your velocity is " + str(round(v, 2)) + " metres/second towards the moon")
            print("You have "+ str(round(f, 2)) +" litres of fuel reamaining")
            print("Do you want to play again?")
            s = input()
            if s[0] == 'y' or s[0] == 'Y':
                v += 1.6 -0.15
                a -= v
                f -= 1
            elif s[0] == 'n' or s[0] == 'N':
                a = 0
                print("Thank you for playing, Goodbye!")
            else:
                print("Do you want to play again?")
                s = input()
        else:
            print("Game Over")
            if a < 0 and v <= 10:
                print("Your altitude is 0 metres above the moon")
                print("Your velocity is " + str(round(v, 2)) + " metres/second towards the moon")
                if f <= 0:
                    print("You have 0 litres of fuel reamaining")
                else:
                    print("You have "+ str(round(f, 2)) +" litres of fuel reamaining")
                print("Congratulation you have landed safely!")      
            elif a < 0 and v > 10:
                print("You blasted a " + str(round(abs(a), 2)) + " meter crater in the moon!")
                print("Your velocity is " + str(round(v, 2)) + " metres/second towards the moon")          
                if f <= 0:
                    print("You have 0 litres of fuel reamaining")
                else:
                    print("You have "+ str(round(f, 2)) +" litres of fuel reamaining")                
    elif s[0] == 'n' or s[0] == 'N':
        print("Thank you for playing, Goodbye!")
    else:
        while s[0] not in ['n', 'N', 'y', 'Y']:
            print("Do you want to play again?")
            s = input()
        else:
            print("Game Over")
            
if __name__ == '__main__':
    answer = my_game(1000.0, 0.0 , 1000.0)
    print(answer)

''' Michelle Conway MCONWA02'''

# altitude  = a  #metres
# velocity  = v  #metres/second
# fuel      = f  #Litres

import math 

def my_game(a,v,f):
    print("Your altitude is " + str(round(a, 2)) +" metres above the moon")
    print("Your velocity is " + str(round(v, 2)) + " metres/second towards the moon")
    print("You have "+ str(round(f, 2)) +" litres of fuel reamaining")
    v += 1.6 
    a -= v
    f -= 1
    while a > 0:
        print("Your altitude is " + str(round(a, 2)) +" metres above the moon")
        print("Your velocity is " + str(round(v, 2)) + " metres/second towards the moon")
        print("You have "+ str(round(f, 2)) +" litres of fuel reamaining")            
        v += 1.6 -0.15
        a -= v
        f -= 1

if __name__ == '__main__':
    answer = my_game(1000.0, 0.0 , 1000.0)
    print(answer)

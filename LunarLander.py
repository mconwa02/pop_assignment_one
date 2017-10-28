''' Michelle Conway MCONWA02'''

# altitude  = a  #metres
# velocity  = v  #metres/second
# fuel      = f  #Litres

def my_game(a,v,f):
    print("Your altitude is " + str(a) +" metres above the moon")
    print("Your velocity is " + str(v) + " metres/second towards the moon")
    print("You have "+ str(f) +" litres of fuel reamaining")
    v += 1.6 
    a -= v
    f -= 1
    while a > 0:
        print("Your altitude is " + str(a) +" metres above the moon")
        print("Your velocity is " + str(v) + " metres/second towards the moon")
        print("You have "+ str(f) +" litres of fuel reamaining")            
        v += 1.6 -0.15
        a -= v
        f -= 1

if __name__ == '__main__':
    answer = my_game(1000.0, 0.0 , 1000.0)
    print(answer)

import random
listA=['rock','paper','scissors']
GameOver=True
while(GameOver):
    play=input("Press Enter to Play . Press Q to exit")
    if(play=='Q' or play=='q'):
         GameOver=False
    else:
        print('''"This is Rock Paper Scissores Game"''')
        user=input('''" Enter any word from Rock, Paper & Scissors: " ''')
        rock,paper,scissors='rock','paper','scissors'
        computerchoice= random.choice(listA)
        print(computerchoice)
        if(user=='rock' and computerchoice=='paper'):
         print("computer wins")
        elif(user=='paper' and computerchoice=='scissors'):
         print( "computer wins")
        elif(user=='scissors' and computerchoice== 'rock'):
         print("you won")
        elif(user=='rock' and computerchoice=='scissors' ):
         print("you won")
        elif(user=='scissors' and computerchoice=='paper'):
         print("you won")
        elif(user=='paper' and computerchoice=='rock'):
         print("you won")
        elif(user== computerchoice):
         print("draw")
        else:
         print("bad luck")

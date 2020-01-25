import random
rno=random.randint(0,20)
user_num=int(input("Guess the number="))
if(rno==user_num):
    print("Numbers are equals")
elif(rno>user_num):
    print("Too Low")
else:
    print("Too High")

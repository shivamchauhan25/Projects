import random
character=[]
for i in range(33,127):
    character.append(chr(i))
passLength=int(input("Enter the Length of the Password: "))
#noOfLetters=int(input("Enter the no of Alphabets you want: "))
#noOfdigits=int(input("Enter the no of Digits you Want: "))
password=''
# for i in range(passLength):
#     randomCharacter=random.choice(character)
#     if(randomCharacter not in password):
#         password=password+(randomCharacter)
#     else:
#         continue
# print(password)
while(True):
    randomCharacter = random.choice(character)
    if(len(password) is passLength):
        break
    elif (randomCharacter not in password):
        password = password + (randomCharacter)
    else:
        continue
print(password)

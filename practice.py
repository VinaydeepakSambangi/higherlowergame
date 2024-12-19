import random 
from gamedata import data


def answering():
    compareA=(random.choices(data))
    compareB=random.choices(data)

    while compareA[0] == compareB[0]:
        compareB = random.choices(data)
        
    print(compareA[0]['name'])
    print(compareB[0]['name'])

    followers_count_A=compareA[0]['followers']
    followers_count_B=compareB[0]['followers']
    if(followers_count_A>followers_count_B):
         return "A"
    else:
        return "B"
score=0
while True:
    correct_answer=answering()
    Given_answer=input("Enter Your Answer : ").strip().upper()
    
    if(Given_answer==correct_answer):
        print("You are Right")
        score+=1
    else:
        print("Please Play Again")
        print(score)
        break
        










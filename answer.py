#!/usr/bin/python3

round = 0
answer = " "


while round < 2:

    round += 1
    answer = input("Finish the movie title, 'Life of a _ _  ':")

    if answer.lower() == "pi": 
        print("Correct!")
        break
    elif round == 2:
        print("Finish the movie title, 'Life of a %u _ ':", answer)
        print("Sorry, the answer was Pi.")
        
    else:
        print("Sorry. Try again!")
        


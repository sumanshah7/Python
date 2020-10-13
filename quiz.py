score = 0

# Question 1
answer1 = input("What is the capital city of Nepal? \na. Janakpur \nb. Pokhara \nc. Kathmandu \nd. Gorkha \n Answer: ")
if answer1 == "c" or answer1 == "Kathmandu":
    score += 1
    print("Correct!")
    print("Score: ",score)
    print("\n")
else:
    print("Incorrect! The answer is Kathmandu")     
    print("Score: ",score)
    print("\n")
    
# Question 2
answer2 = input("Who is the first person to land on Moon? \na. Valentina Tereshkova \nb. Kalpana Chawla \nc. Jessica Meir \nd. Pete Conrad \n Answer: ")
if answer2 == "a" or answer2 == "Valentina Tereshkova":
    score += 1
    print("Correct!")
    print("Score: ",score)
    print("\n")
else:
    print("Incorrect! The answer is Valentina Tereshkova")     
    print("Score: ",score)
    print("\n")

# Question 3
answer3 = input("How many months have 28 days? \na. 1 \nb. 12 \nc. 4 \nd. 8 \n Answer: ")
if answer3 == "b" or answer3 == "12":
    score += 1
    print("Correct!")
    print("Score: ",score)
    print("\n")
else:
    print("Incorrect! The answer is 12")     
    print("Score: ",score)
    print("\n")
    
# Question 4
answer4 = input("Which animal is known as 'Ship of the Desert'? \na. Tiger \nb. Horse \nc. Camel \nd. Cow \n Answer: ")
if answer4 == "c" or answer4 == "Camel":
    score += 1
    print("Correct!")
    print("Score: ",score)
    print("\n")
else:
    print("Incorrect! The answer is Camel")     
    print("Score: ",score)
    print("\n")
   
# Question 5
answer5 = input("How many days are there in the month of February in a leap year? \na. 28 \nb. 29 \nc. 30 \nd. 31 \n Answer: ")
if answer5 == "b" or answer5 == "29":
    score += 1
    print("Correct!")
    print("Score: ",score)
    print("\n")
else:
    print("Incorrect! The answer is 29")     
    print("Score: ",score)
    print("\n")  
    
# Question 6
answer6 = input("Which is the largest animal in the world? \na. Elephant \nb. Giraffe \nc. Blue Whale \nd. Rhino \n Answer: ")
if answer6 == "c" or answer6 == "Blue Whale":
    score += 1
    print("Correct!")
    print("Score: ",score)
    print("\n")
else:
    print("Incorrect! The answer is Blue Whale")     
    print("Score: ",score)
    print("\n")   
    
# Question 7
answer7 = input("What type of bird lays the largest eggs? \na. Emu \nb. Ostrich \nc. Shoebill \nd. Cinereous Vulture \n Answer: ")
if answer7 == "b" or answer7 == "Ostrich":
    score += 1
    print("Correct!")
    print("Score: ",score)
    print("\n")
else:
    print("Incorrect! The answer is Ostrich")     
    print("Score: ",score)
    print("\n")

# Question 8
answer8 = input("Which is the nearest star to planet earth? \na. Sun \nb. Moon  \nc. Mercury \nd. Venus \n Answer: ")
if answer8 == "a" or answer8 == "Sun":
    score += 1
    print("Correct!")
    print("Score: ",score)
    print("\n")
else:
    print("Incorrect! The answer is Sun")     
    print("Score: ",score)
    print("\n")
    
# Question 9
answer9 = input("Which is the longest river on the earth? \na. Yangtze \nb. Ganga  \nc. Amazon \nd. Nile \n Answer: ")
if answer9 == "d" or answer9 == "Nile":
    score += 1
    print("Correct!")
    print("Score: ",score)
    print("\n")
else:
    print("Incorrect! The answer is Nile")     
    print("Score: ",score)
    print("\n")
    
# Question 10
answer10 = input("Which planet is known as the Red Planet? \na. Mercury \nb. Venus  \nc. Earth \nd. Mars \n Answer: ")
if answer10 == "d" or answer10 == "Mars":
    score += 1
    print("Correct!")
    print("Score: ",score)
    print("\n")
else:
    print("Incorrect! The answer is Mars")     
    print("Score: ",score)
    print("\n")

# Final Message

if score <= 1:
    print("Your total score is:",score,"- Its really bad!")
elif score <= 5:
    print("Your total score is:",score,"-You went ok.")
else:
    print("Your total score is:",score,"-You are awesome!")
        

    
    

    
     

             
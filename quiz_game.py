print("Welcome to my computer quiz!")

playing = input("Do you want to play?")
print(playing)

text = "Tim IS Great!"

print(text.lower())

if playing.lower() != "yes": 
    quit()

print("Okey! Let's play :)")
score = 0

answer = input("What does CPU stand for?")
if answer.lower() == "processing unit":
    print("Correct!")
    score += 1  # Increment the score by 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for?")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1  # Increment the score by 1
else:
    print("Incorrect!")
    
answer = input("What does PSU stand for?")
if answer.lower() == "power supply":
    print("Correct")
    score += 1  # Increment the score by 1
else:
    print("Incorrect!")
    
answer = input("What do you GPU?")
if answer.lower() == "RTX 4040":
    print("Correct your score is!" + score)
    score += 1  # Increment the score by 1
else:
    print("Incorrect!")        
        
print("You got " + str(score) + " questions correct!") 
print("You got " + str((score/4) * 100) + "%.")   
  
   
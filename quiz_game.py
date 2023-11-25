print("Welcome to my computer quiz!")

playing = input("Do you want to play?")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okey! Let's play :)")

answer = input("What does CPU stand for?")
if answer.lower() == "processing unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does RAM stand for?")
if answer.lower() == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")
    
answer = input("What does PSU stand for?")
if answer.lower() == "power supply":
    print("Correct!")
else:
    print("Incorrect!")    
    
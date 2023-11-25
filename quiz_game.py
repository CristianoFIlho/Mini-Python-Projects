print("Welcome to my computer quiz!")

playing = input("Do you want to play?")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okey! Let's play :)")

answer = input("What does CPU stand for?")
if answer.lower() == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does GPU stand for?")
if answer.lower() == "graphics processing unit":
    print("Correct!")
else:
    print("Incorrect!")
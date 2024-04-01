print("Welcome to my Family Guy quiz")

playing = input("Do you want to play? ")

if playing.upper() != "YES":
    quit()
print("OK Let's Go")
score = 0

answer = input("What is Peters youngest son's name? ")
if answer.upper() == "STEWIE":
     print("Damn right")
     score += 1
else:
    print("FAIL")

answer = input("Who has s secret relationship with Mayor West? ")
if answer.upper() == "MEG":
     print("Shhh it's a secret")
     score += 1
else:
    print("Really?")

answer = input("What street do the Griffin's live on? ")
if answer.upper() == "SPOONER":
     print("You probably know the house number too stalker")
     score += 1
else:
    print("You SUCK!")

answer = input("What kind of pet does Quagmire have? ")
if answer.upper() == "CAT":
     print("Of course he loves pussy")
     score += 1
else:
    print("Are you even trying?")

answer = input("Which one of Pete's friends live across the street? ")
if answer.upper() == "CLEVELAND":
     print("Of course he does")
     score += 1
else:
    print("Have you ever watched the show?")

print ("You got " + str(score) + " questions right!")
print ("You got " + str((score/5) * 100) + "%.")
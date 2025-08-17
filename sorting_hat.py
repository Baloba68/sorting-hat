#the dictionery for storing points for each house.
houses={
  "Gryffindor":0,
  "Ravenclaw":0,
  "Hufflepuff":0,
  "Slytherin":0,
}
#the questions.
print("Q1)Do you like Dawn or Dusk? 1)Dawn 2)Dusk")
answer=int(input("Enter 1 or 2: "))
if answer == 1:
  houses["Gryffindor"] +=1
  houses["Ravenclaw"] +=1
elif answer == 2:
  houses["Hufflepuff"] +=1
  houses["Slytherin"]  +=1
else:
  print("Wrong input")
print("Q2)When I'm dead, I want people to remember me as: 1)The Good .2)The Great .3)The wise .4)The Bold")
answer=int(input("Enter 1,2,3 or 4: "))
if answer == 1:
  houses["Hufflepuff"] +=2
elif answer == 2:
  houses["Slytherin"] +=2
elif answer == 3:
  houses["Ravenclaw"] +=2
elif answer == 4:
  houses["Gryffindor"] +=2
else:
  print("Wrong input")
print("Q3)Which kind of instrument most pleases your ear? 1)The Violin .2)The trumpet .3)The piano .4)The drum")
answer=int(input("Enter 1,2,3 or 4: "))
if answer == 1:
  houses["Slytherin"] +=4
elif answer == 2:
  houses["Hufflepuff"] +=4
elif answer == 3:
  houses["Ravenclaw"] +=4
elif answer == 4:
  houses["Gryffindor"] +=4
else:
  print("Wrong input")
#Give out the score of each house,then inform the student which house they will go to
print("Here are your scores:")
for house, score in houses.items():
    print(f"{house}: {score} points")
chosen_house = max(houses, key=houses.get)
print("You belong to", chosen_house, "!")

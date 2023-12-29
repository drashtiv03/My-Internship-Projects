print("Enter your name")
name=input()
score=0;
print("Question 1")
print("The sun rises from which direction?")
print("A)North")
print("B)West")
print("C)South")
print("D)East")
answer=input()
if answer=="D":
    print("Correct!")
    score=score+1
elif answer=="A"or answer=="B"or answer=="C":
    print("Wrong! The correct answer is D)East")
else:
    print("Invalid Answer!")
print("Question 2")
print("The largest continent of the world is")
print("A)Africa")
print("B)Asia")
print("C)Europe")
print("D)North America")
answer=input()
if answer=="B":
    print("Correct!")
    score=score+1
elif answer=="A"or answer=="D"or answer=="C":
    print("Wrong! The correct answer is B)Asia")
else:
    print("Invalid Answer!")
print("Question 3")
print("Which of the following belongs to the seven wonders of the world?")
print("A)The Lotus Temple,Delhi")
print("B)Leaning Tower of Pisa,Italy")
print("C)Canadian Rocky Mountains,Canada")
print("D)The Great Barrier Reef,Australia")
answer=input()
if answer=="B":
    print("Correct!")
    score=score+1
elif answer=="A"or answer=="D"or answer=="C":
    print("Wrong! The correct answer is B)Leaning Tower of Pisa,Italy")
else:
    print("Invalid Answer!")
print("Question 4")
print("Which of the following is not a programming language?")
print("A)Java")
print("B)C++")
print("C)Polymorphism")
print("D)Python")
answer=input()
if answer=="C":
    print("Correct!")
    score=score+1
elif answer=="A"or answer=="D"or answer=="B":
    print("Wrong! The correct answer is C)Polymorphism")
else:
    print("Invalid Answer!")
print("Question 5")
print("The great Victoria Desert is located in")
print("A)Canada")
print("B)West Africa")
print("C)Australia")
print("D)North America")
answer=input()
if answer=="C":
    print("Correct!")
    score=score+1
elif answer=="A"or answer=="B"or answer=="D":
    print("Wrong! The correct answer is C)Australia")
else:
    print("Invalid Answer!")
print(name,"! Your overall score is",score,"/5")
print("Congratulations! You have completed the quiz")
print("Thank You for Attempting the Quiz.We wish you the very best for future!")




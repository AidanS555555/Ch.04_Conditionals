'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
x=0
# Question 1
lee_movie = str(input("What Bruce Lee movie came out a month after his death?"))
if lee_movie.upper() == "ENTER THE DRAGON":
    print("Correct")
    x = 1
else:
    print("That is incorrect. The answer is Enter the Dragon")
# Question 2

cudi = int(input("What year did the album Man on the Moon come out?"))
if cudi == 2009:
    print("That is correct")
    x = x+1
else:
    print("That is not correct. Man on the Moon came out in 2009.")
# Question 3
answer= str(input("If x=2y+32, what is the value of y and x given the equation 2x+4y=128? Give your answer as x,y."))
if answer == "48,8":
    print("Correct")
    x = x+1
else:
    print("Wrong. The asnwer is 48,8")
# Question 4
lantern=int(input("What issue of showcase comics did green lantern first appear in?"))
if lantern==22:
    print("Correct")
    x = x+1
else:
    print("That is wrong, the answer is 22")
# Question 5
western=str(input("Who is the most famous actor for western/cowboy moives?"))
if western.upper() == "CLINT EASTWOOD":
    print("Correct")
    x = x+1
else:
    print("No. It's Clint Eastwood")
# Question 6
easy=int(input("What is 5+5"))
if easy == 10:
    print("Nice")
    x = x+1
else:
    print("How did you get that wrong. 10")
# Question 7
print("A.CSP")
print("B.Algebra")
print("C.World History")

teach=str(input("What class is this?"))
if teach.upper()== "A" or teach.upper()== "CSP":
    print("Correct")
    x = x+1
else:
    print("Observant, you are not. This is CSP")
# Question 8
yoda=str(input("What movie was yoda first intorduced?"))
if yoda.upper()== "EMPIRE STRIKES BACK":
    print("Good job, you have completed the quiz.")
    x = x+1
else:
    print("No, it was Empire Strikes Back")


print("This is how many questions you got correct.")
print(x)
if x == 8:
    print("Your score is 100%. You got an A")
if x == 7:
    print("Your score is 87.5%. You got a B")
if x == 6:
    print("Your score is 75%. You got a C")
if x == 5:
    print("Your score is 62.5%. You got a D")
if x == 4:
    print("Your score is 50%. You got an F")
if x == 3:
    print("Your score is 37.5%. You got an F")
if x == 2:
    print("Your score is 25%. You got an F")
if x == 1:
    print("Your score is 12.5%. You got and F")
if x == 0:
    print("Your score is 0%. You got an F")
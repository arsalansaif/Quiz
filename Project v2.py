ID=int(input("Enter ID: "))
Name=str(input("Enter Name: "))

Score=0

f1= open("Quiz.txt", "r")
for f in range (10):
    print(f1.readline())
    print(f1.readline())
    MCQ = input("Enter the Letter:")
    Answer= (f1.readline()).strip()
    Answer= Answer.lstrip("Ans:")
    if (MCQ.lower()) == Answer:
        print("Correct :)")
        Score+=1
        print("Score: ", Score)
    else:
        print("Incorrect :(")
        print("Score: ", Score)

print("Total Score is " + str(Score) + " out of 10")
f1.close()
 
f2= open("QuizResults.txt", "w")
f2.write("Name: ")
f2.write(Name)
f2.write("ID: ")
f2.write(str(ID))
f2.write("Score: " + str(Score) + " out of 10")
f2.close()

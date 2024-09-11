import random

username = str(input("What is your name : "))
question = str(input("What is do you want to ask : "))

ans1 = "Without a doubt"
ans2 = "No"
ans3 = "Somewhat Likely"
ans4 = "I don't know"
ans5 = "Yes"
ans6 = "Very Doubtful"
ans7 = "that I ask that you try again later"
ans8 = "Maybe"

choice = random.randint (1,8)

answer = ""

if choice == 1:
    answer = ans1
elif choice == 2:
    answer = ans2
elif choice == 3:
    answer = ans3
elif choice == 4:
    answer = ans4
elif choice == 5:
    answer = ans5
elif choice == 6:
    answer = ans6
elif choice == 7:
    answer = ans7
else:
    answer = ans8

print("Shaking")

print()
print("My answer is",answer)
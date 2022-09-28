# # playerName = len(input("What is your name \n"));
# #
# # # You can change the data type for string and int
# # newPlayerName = str(playerName);
# # print("This name has " + newPlayerName + " characters")
#
# # a = 123
# # print(type(a))
# #
# # newA = str(a);
# # print(type(newA))
#
# # 🚨 Don't change the code below 👇
# # two_digit_number = input("Type a two digit number: ")
# #  🚨 Don't change the code above 👆
# #
# # ####################################
# # #Write your code below this line 👇
# # print(int(two_digit_number[0]) + int(two_digit_number[1]));
#
# # 3 + 5
# # 6 - 4
# # 4 * 4
# # 1 / 6
# #
# # 2 ** 2
# #
# # # 🚨 Don't change the code below 👇
# # height = input("enter your height in m: ")
# # weight = input("enter your weight in kg: ")
# # # 🚨 Don't change the code above 👆
# #
# # #Write your code below this line 👇
# # b =  weight / (height/100)**2
# #
# # print(b)
# result = 4/6
# result / 2
# print(result)
#
# # F-String
#
# score = 0
# height = 1.8
# winning = True
#
# print(f"your score is {score} and height is {height}")
#
# # 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# # 🚨 Don't change the code above 👆
#
# days = 365
# weeks = 52
# months = 12
#
# #Write your code below this line 👇
#
# print(F"you have {age * days}, {age * 52}, and {age * months} months left))

print("Welcome to Tip Calculator")
bill = float(input("What was the total bill? \n"))
tipChoice = int(input("How much do you want to leave a tip? 10, 12, 15"))
people = int(input("How people are being divided"))

tipP = tipChoice / 100
totalCost = bill + tipP
personBillEach = totalCost / people
newpBE = round(personBillEach)
print(newpBE)
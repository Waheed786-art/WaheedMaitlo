print("Welcome To KON BANEGA CROREPATI")
print("First of all read rules and regulations with complete attention.")
print("We will ask four questions from you Okay!")
price=("$1000","$2000","$3000","$4000")
print("Price for 1st correct answer is,",price[0],"Price for 2nd correct answer is,",price[1],"Price for 3rd correct answer is,",price[2],"Price for 4th correct answer is",price[3])
print("You can stop playing anytime if you don't know the answer of the question just say \"END\" and we don't play the game further and we'll give you the price according to your correct answers.")
print("If you gave wrong answer of any of the questions no matter whether you've answered previous questions correctly, you'll be given only $100 just because you came in our show.")
print("If you answer all questions correctly then you'll get $",1000+2000+3000+4000,".\nOkay then let's Start!")
Q1 = "K2 is the _______ largest mountain in the world?"
print("Your first question is:",Q1)
opt = ("a = 1st" , "b = 2nd", "c = 3rd", "d = 4th")
print("Options:",opt)
print("which is correct option a , b , c , or d")
answer1 = (input("Enter your answer: "))
if (answer1 == "a"):
    print("Wrong Answer!\"b (2nd)\" was the right option. Better luck next time. As you answered wrong so you'll get only $100. Game has been ended. Now, you can leave!")
    exit()
elif (answer1 == "b"):
    print("Answer is correct you've won",price[0],"for your 1st correct answer.")
elif (answer1 == "c"):
    print("Wrong Answer!\"b (2nd)\" was the right option. Better luck next time. As you answered wrong so you'll get only $100. Game has been ended. Now, you can leave!")
    exit()
elif (answer1 == "d"):
    print("Wrong Answer!\"b (2nd)\" was the right option. Better luck next time. As you answered wrong so you'll get only $100. Game has been ended. Now, you can leave!")
    exit()
else:
    print("This option is not present in the list please run the program again.")
if (answer1 == "END"):
    print("You'll get all the according to your answers")
    exit()

print("Let's move to our next Question.")
Q2 = "Who is known as the father of modern computers?"
print("Question No 2:",Q2)
opt2 = ("a = Guiddo Van Rossum","b = Bjarne Stroustrup", "c = Tim Berners Lee", "d = Charles Babbage")
print("Options:",opt2)
print("which is correct option a , b , c , or d")
answer2 = (input("Enter your answer: "))
if (answer2 == "a"):
    print("Wrong Answer!\"d (Charles Babbage)\" was the right option. Better luck next time. As you answered wrong so you'll get only $100. Game has been ended. Now, you can leave!")
    exit()
elif (answer2 == "b"):
    print("Wrong Answer!\"d (Charles Babbage)\" was the right option. Better luck next time. As you answered wrong so you'll get only $100. Game has been ended. Now, you can leave!")
    exit()
elif (answer2 == "c"):
    print("Wrong Answer!\"d (Charles Babbage)\" was the right option. Better luck next time. As you answered wrong so you'll get only $100. Game has been ended. Now, you can leave!")
    exit()
elif (answer2 == "d"):
    print("Answer is correct you've won",price[1] ,"for your 2nd correct answer.")

if (answer2 == "END"):
    print("You'll get all the according to your correct answers")
    exit()
print("Let's move to our next Question.")
Q3 = "UN was established on:"
print("Question No 3:",Q3)
opt3 = ("a = 7 Oct 1948","b = 24 Oct 1944", "c = 24 Oct 1945", "d = 16 Oct 1951")
print("Options:",opt3)
print("which is correct option a , b , c , or d")
answer3 = (input("Enter your answer: "))
if (answer3 == "a"):
    print("Wrong Answer!\"c (24 Oct 1945)\" was the right option. Better luck next time. As you answered wrong so you'll get only $100. Game has been ended. Now, you can leave!")
    exit()
elif (answer3 == "b"):
    print("Wrong Answer!\"c (24 Oct 1945)\" was the right option. Better luck next time. As you answered wrong so you'll get only $100. Game has been ended. Now, you can leave!")
    exit()
elif (answer3 == "c"):
    print("Answer is correct you've won",price[2] ,"for your 3rd correct answer.")
elif (answer3 == "d"):
    print("Wrong Answer!\"c (24 Oct 1945)\" was the right option. Better luck next time. As you answered wrong so you'll get only $100. Game has been ended. Now, you can leave!")
    exit()
if (answer3 == "END"):
    print("You'll get all the money according to your correct answers")
    exit()

print("Let's move to our last Question.")
Q4 = "_________ is the largest planet in the solar system."
print("The last question, Question No 4 is:",Q4)
opt4 = ("a = Jupiter","b = Saturn", "c = Mercury", "d = Earth")
print("Options:",opt4)
print("which is correct option a , b , c , or d")
answer4 = (input("Enter your answer: "))
if (answer4 == "a"):
    print("Answer is correct you've won",price[3] ,"for your 4th correct answer.")
elif (answer4 == "b"):
    print("Wrong Answer!\"a (Jupiter)\" was the right option. Better luck next time. As you answered wrong so you'll get only $100. Game has been ended. Now, you can leave!")
    exit()
elif (answer4 == "c"):
    print("Wrong Answer!\"a (Jupiter)\" was the right option. Better luck next time. As you answered wrong so you'll get only $100. Game has been ended. Now, you can leave!")
    exit()
elif (answer4 == "d"):
    print("Wrong Answer!\"a (Jupiter)\" was the right option. Better luck next time. As you answered wrong so you'll get only $100. Game has been ended. Now, you can leave!")
    exit()
if (answer4 == "END"):
    print("You'll get all the according to your correct answers")
    exit()

if (answer1 == "b" and answer2 == "d" and answer3 == "c" and answer4 == "a" ):
    print("Congratulations! you answered all the questions correctly so you'll get $10000 altogether. Now, you're the owner of 10000 USD.\nGo and Enjoy your life.")


    
#most asked interview ques

#number = int(input("enter a number "))

#when the number is divisible by 3 then instead of printing number it should print Fizz
#when the number is divisible by 5, then instead of printing number it should print Buzz
#and if the number is divisible by both 3 and 5 eg instead of printing number it should print FizzBuzz




for game in range(1,101):
    if(game%3==0 and game%5==0):
        print("FizzBuzz")  
    elif(game%3==0):
        print("Fizz")
    elif(game%5==0):
        print("Buzz")
    else:
        print(game)     
       
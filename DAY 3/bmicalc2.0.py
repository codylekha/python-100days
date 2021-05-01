#18.5 underweight
# >18.5 below 25 normal wt
# 25 below 30 overwt
#30 <35 obese
#>35 clinically obese

height = input("enter your height in m:")
weight = input("enter your weight in kg:")

#BMI = weight/height**2

bmi = round(weight/ height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi<25:
    print(f"Your bmi is {bmi}, you are normal weight")
elif bmi<30:
    print(f"Your bmi is {bmi}, you are overweight")
elif bmi<35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinicaly obese")              
weight = eval(input("Enter weight in kg: "))
height = eval(input("Enter height in m: "))

BMI = weight / (height ** 2)
print("BMI : ", BMI)

if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal weight")
elif 25 <= BMI < 30:
    print("Overweight")
elif BMI >= 30:
    print("Obese")
else:
    print("Wrong input")
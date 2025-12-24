height=float(input("What is your height in cm?:"))
weight=float(input("What is your weight in kg?:"))
BMI=weight/(height/100)**2
if BMI <= 18.4:
    print("Under  weight",BMI)
elif BMI <= 24.9:
    print("Healthy",BMI)
elif BMI <= 29.99:
    print ("Over weight",BMI)
elif BMI <= 34.99:
    print ("Severily over weight",BMI)
elif BMI <= 39.99:
    print("Obese",BMI)
else:
    print("Severily Obese",BMI)

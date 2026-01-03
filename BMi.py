height=float(input("What is your height in cm?:"))
weight=float(input("What is your weight in kg?:"))
BMI=weight/(height/100)**2
if BMI <= 15.0:
    print("Under  weight",BMI)
elif BMI <= 20.0:
    print("Healthy",BMI)
elif BMI <= 26.0:
    print ("Over weight",BMI)
elif BMI <= 31.0:
    print ("Severily over weight",BMI)
elif BMI <= 36.0:
    print("Obese",BMI)
else:
    print("Severily Obese",BMI)

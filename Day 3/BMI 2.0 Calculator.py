#BMI Calculator = weight / (height)**2
weight = input("Enter Your Weight in Kg: ")
height = input("Enter Your Height in M: ")

weight_num = float(weight)
height_num = float(height)

BMI_cal = weight_num / (height_num)**2

if BMI_cal < 18.5:
    print(f"Your BMI is {int(BMI_cal)}, you are slightly underweight.")
elif BMI_cal >= 18.5:
    if BMI_cal < 25:
        print(f"Your BMI is {int(BMI_cal)}, you have normal weight.")
elif BMI_cal >= 25:
    if BMI_cal < 30:
        print(f"Your BMI is {int(BMI_cal)}, you are slightly overweight.")
elif BMI_cal >= 30:
    if BMI_cal < 35:
        print(f"Your BMI is {int(BMI_cal)}, you are obese.")
else:
    print(f"Your BMI is {int(BMI_cal)}, you are clinically obese.")



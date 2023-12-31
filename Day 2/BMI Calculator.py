#BMI Calculator = weight / (height)**2
weight = input("Enter Your Weight in Kg: ")
height = input("Enter Your Height in M: ")

weight_num = float(weight)
height_num = float(height)

BMI_cal = weight_num / (height_num)**2
print(f"Your BMI is {int(BMI_cal)}.")
weight = int(input('შეიყვანე შენი წონა : '))
height = int(input('შეიყვანე შენი სიმაღლე: '))

BMI =weight/height

print(BMI)

if BMI < 18.5:
   print("underweight")

   if BMI >= 18.5 < 24.9: 
      print("normal")
      
if BMI >= 25 < 29.9:
   print('overweight')

if BMI >= 30:
   print("obessity")

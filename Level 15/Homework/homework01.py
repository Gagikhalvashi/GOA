steps = int(input("შეიყვანეთ 10 წუთში გადადგმული ნაბიჯების რაოდენობა: "))
goal_reached = steps >= 1000

print("მიზანი შესრულდა:", goal_reached)
print(True and True)  # Output: True
print(True and False)  # Output: False
print(5 > 3 and 10 < 15)  # Output: True
print(2 == 2 and 3 != 3) # Output: Falsent(False and False) # Output: False

# მაგალითები
print(True and True)  # Output: True
print(True and False)  # Output: False
print(False and False) # Output: False

# რიცხვებთან
print(5 > 3 and 10 < 15)  # Output: True
print(2 == 2 and 3 != 3) # Output: False

# სტრიქონებთან
print("Python" == "Python" and "is" == "is")  # Output: True
print("Java" == "Python" and "fun" == "fun")  # Output: False

# მაგალითები
print(True or False)  # Output: True
print(False or False) # Output: False

# რიცხვებთან
print(5 > 3 or 10 > 15)  # Output: True
print(2 == 3 or 3 != 3) # Output: True

# სტრიქონებთან
print("Python" == "Python" or "Java" == "Python")  # Output: True
print("Java" == "C#" or "C#" == "C++") # Output: False

# ორივე ოპერატორის გამოყენება
x = 10
y = 5
print(x > y and x < 15)   # Output: True
print(x > y or x < 5)     # Output: True
print(not (x == y))       # Output: True (not უარყოფს მნიშვნელობას)

# უფრო რთული მაგალითი
is_raining = True
have_umbrella = False
can_go_outside = not is_raining or have_umbrella
print(can_go_outside)  # Output: False (თუ წვიმს და ქოლგა არ გაქვს, ვერ გახვალ გარეთ)


# მომხმარებლისგან ნაბიჯების რაოდენობის მიღება
steps = int(input("შეიყვანეთ 10 წუთში გადადგმული ნაბიჯების რაოდენობა: "))

# მიზნის შემოწმება და შედეგის დაბეჭდვა
goal_reached = steps >= 1000
print("მიზანი შესრულდა:", goal_reached)
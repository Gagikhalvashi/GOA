def print_opposite_number():
    number = float(input("შეიყვანეთ რიცხვი: "))
    
    if number > 0:
        print(-number)  # უარყოფითი ვარიანტი
    elif number < 0:
        print(-number)  # დადებითი ვარიანტი
    else:
        print("შესაბამისი რიცხვი არ არის (0)")

# ფუნქციის გაწვევა
print_opposite_number()

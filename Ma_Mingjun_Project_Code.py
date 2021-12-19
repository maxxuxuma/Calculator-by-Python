def calculation():
    r = 0
    a = 0
    b = 0
    item = ""
    operator = "N/A"
    print("You can use +, -, *, /, ^, RT as operation, and enter space to start execution")
    number_stack = []
    operator_list = ["+","-","*","/","^", "RT"]
    calculate_list = []
    i = 0
    while i<3: #longest operator is 3
        item = input("item: ") #numbers and items input
        calculate_list.append(item)
        i = i + 1
    for e in calculate_list:
        #preparing for calculation
        if e.isalnum() and e!="RT":
            if e =="e":
                number = 2.718
            else:
                number = float(e)
            number_stack.append(number)
        elif e in operator_list:
            for o in operator_list:
                if e==o: #finding the operator
                    operator = o
                    break
        elif e[0] == "-":
            number = float(e)
            number_stack.append(number)
        elif "." in e:
            number = float(e)
            number_stack.append(number)

    #calculation
    if operator =="+":
        a = number_stack.pop(0)
        b = number_stack.pop(-1)
        r = a + b
    if operator =="-":
        a = number_stack.pop(0)
        b = number_stack.pop(-1)
        r = a - b
    elif operator =="=":
        a = number_stack.pop(0)
        b = number_stack.pop(-1)
        r = a - b
    elif operator =="*":
        a = number_stack.pop(0)
        b = number_stack.pop(-1)
        r = a * b
    elif operator =="/":
        a = number_stack.pop(0)
        b = number_stack.pop(-1)
        try:
             r = a/b
        except ZeroDivisionError:
            print("Math Error")
            return None
        else:
            r = a/b
    elif operator =="^":
        a = number_stack.pop(0)
        b = number_stack.pop(-1)
        r = a**b
    elif operator =="RT":
        try:
            a = number_stack.pop(0)
            b = 1/number_stack.pop(-1)
        except ZeroDivisionError:
            return None
        else:
            r = a**b
    if int(r)==r:
        r = int(r)
    return r

def currency_ratio(original_unit, i, goal_unit):
    amount = 0
    exchange_rates={"$": 1.0, "£": 0.7497, "c$": 1.266, "€": 0.8790} #how many foreign currencies to exchange one dollar.
    original_unit = original_unit.lower() # lowering the inputs
    goal_unit = goal_unit.lower() # lowering the inputs
    if "dollar" in original_unit or original_unit == "usd" or original_unit == "$":
        if goal_unit=="£" or ("pound" in goal_unit) or "gbp" in goal_unit:
            goal_unit = "£"
            amount = i*exchange_rates["£"]
        elif goal_unit =="c$" or goal_unit=="canadian dollar" or goal_unit =="cad":
            goal_unit = "c$"
            amount = i*exchange_rates["c$"]
        elif goal_unit == "€" or ("euro" in goal_unit):
            goal_unit = "€"
            amount = i*exchange_rates["€"]
        else:
            return None
    elif "pound" in original_unit or original_unit=="gbp" or original_unit =="£":
        if goal_unit=="$" or goal_unit=="dollar":
            goal_unit = "$"
            amount = i/exchange_rates["£"]
        elif goal_unit =="c$" or goal_unit=="canadian dollar" or goal_unit =="cad":
            goal_unit = "C$"
            amount = i*exchange_rates["c$"]/exchange_rates["£"]
        elif goal_unit == "€" or "euro" in goal_unit:
            goal_unit = "€"
            amount = i*exchange_rates["€"]/exchange_rates["£"]
        else:
            return None
    elif "canadian dollar" in original_unit or original_unit=="cad" or original_unit=="c$":
        if goal_unit=="$" or goal_unit=="dollar":
            goal_unit = "$"
            amount = i/exchange_rates["c$"]
        elif goal_unit=="£" or "pound" in goal_unit or "gbp" in goal_unit:
            goal_unit = "£"
            amount = i*exchange_rates["£"]/exchange_rates["c$"]
        elif goal_unit == "€" or ("Euro"in goal_unit):
            goal_unit = "€"
            amount = i*exchange_rates["€"]/exchange_rates["c$"]
        else:
            return None
    elif original_unit=="€" or original_unit=="euro":
        if goal_unit=="$" or goal_unit=="dollar":
            goal_unit = "$"
            amount = i/exchange_rates["€"]
        elif goal_unit=="£" or ("pound" in goal_unit) or "gbp" in goal_unit:
            goal_unit = "£"
            amount = i*exchange_rates["£"]/exchange_rates["€"]
        elif goal_unit =="c$" or goal_unit=="canadian dollar" or goal_unit =="cad":
            goal_unit = "C$"
            amount = i*exchange_rates["c$"]/exchange_rates["€"]
        else:
            return None
    else:
        print("Exchange is not available")
        return None
    amount = str("{:.2f}".format(amount))
    final_value = goal_unit+ amount
    write_1 = open('report_currency.txt', 'w')
    final_report = write_1.write("Original amount " + str(original_unit) + str(i) + " is exchanged to " + final_value)
    return final_report

class quadratic_equation():
    def __init__(self, x_a, x_b, x_c):
        self.x_a = x_a
        self.x_b = x_b
        self.x_c = x_c
    def __solution__(self, x_a, x_b, x_c):
        self.x1 = (-self.x_b + ((self.x_b**2)-4*self.x_a*self.x_c)**(1/2))/(2*self.x_a)
        self.x2 = (-self.x_b - ((self.x_b**2)-4*self.x_a*self.x_c)**(1/2))/(2*self.x_a)
        if self.x1==self.x2:
            return "x = " + str(self.x1)
        else:
            return "x1 = " + str(self.x1) + " x2 = " + str(self.x2)


choice = input("Please enter the choice of function. '1' for calculation, '2' for currency calculation, '3' for quadratic-equation: ")
if choice=='1':
    result = calculation()
    print(result)
elif choice=='2':
    exchange_unit = input("What is the currency unit exchange: ")
    exchange_amt = float(input("What is the amount to exchange: "))
    expected_unit = input("What currency do you want change to?")
    result_2 = currency_ratio(exchange_unit, exchange_amt, expected_unit)
elif choice=='3':
    a_c, b_c, c_c = float(input("a = ")), float(input("b = ")), float(input("c = "))
    eq_e = quadratic_equation(a_c, b_c, c_c) #equation evaluation class
    print(eq_e.__solution__(a_c, b_c, c_c))


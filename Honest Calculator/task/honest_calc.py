msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"


def check_number(number):
    try:
        float(number)
        return True
    except ValueError:
        print(msg_1)
        return False


def check_operator(operator):
    if operator in ('+', '-', '*', '/'):
        return True
    else:
        print(msg_2)
        return False


while True:
    calc = input(f'{msg_0}\n')
    try:
        x, oper, y = calc.split()
        if check_number(x) and check_number(y) and check_operator(oper):
            break
    except ValueError:
        continue

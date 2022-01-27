msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

memory = 0.0


def check_memory(number):
    if number == 'M':
        return memory
    return number


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


def evaluation_result(first_number, operator, second_number):
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number
    else:
        return first_number / second_number


def saving_to_memory(number):
    global memory
    valid_answer = False
    while not valid_answer:
        answer = input(f'{msg_4}\n')
        if answer in ('y', 'n'):
            valid_answer = True
            if answer == 'y':
                memory = number


def continue_evaluation():
    valid_answer = False
    continue_result = False
    while not valid_answer:
        answer = input(f'{msg_5}\n')
        if answer in ('y', 'n'):
            valid_answer = True
            if answer == 'y':
                continue_result = True
    return continue_result


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if 1 in (v1, v2) and v3 == '*':
        msg += msg_7
    if 0 in (v1, v2) and v3 != '/':
        msg += msg_8
    if msg != '':
        print(msg_9 + msg)


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    return False


while True:
    calc = input(f'{msg_0}\n')
    try:
        x, oper, y = calc.split()
        x = check_memory(x)
        y = check_memory(y)
        if check_number(x) and check_number(y) and check_operator(oper):
            check(float(x), float(y), oper)
            if oper == '/' and 0.0 in (float(x), float(y)):
                print(msg_3)
            else:
                result = evaluation_result(float(x), oper, float(y))
                print(result)
                saving_to_memory(result)
                if not continue_evaluation():
                    break
    except ValueError:
        continue

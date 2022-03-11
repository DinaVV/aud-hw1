# TASK1
def name_age(name, age):
    print("Hello {0}. Your age is: {1}".format(name, age));
    return name + str(age)


# TASK2
def swap_integers(num1, num2):
    temp1 = num1
    num1 = num2
    num2 = temp1
    return str(num1) + str(num2)


# TASK3
def check_numbers(num1, num2):
    if (num1 % 6 == 0 or num2 % 6 == 0) and (num1 % 10 == 0 and num2 % 10 == 0):
        return True
    else:
        return False


# TASK4
def sum_up(num1, num2):
    if num2 > num1:
        if num1 > 0 and num2 > 0:
            sum_var = 0
            for i in range(num1, num2 + 1):
                sum_var = sum_var + i
            return sum_var
        else:
            return 0
    else:
        return 0


# TASK5
def circle_area(r1, r2, r3):
    if not (isinstance(r1, int)) or not (isinstance(r2, int)) or not (isinstance(r3, int)):
        return "no integers passed as arguments"
    else:
        pi = 3.141
        a1 = pi * (r1 ** 2)
        a2 = pi * (r2 ** 2)
        a3 = pi * (r3 ** 2)
        return a1 + a2 + a3


# TASK6
def check_string(text):
    if text.upper().startswith('A') or text.upper().endswith('A'):
        return True
    else:
        return False


# TASK7
def triangle(rows):
    for i in range(1, rows + 1):
        #print('*' * i)
        stringtoprint = ''
        for j in range(1,i+1):
            stringtoprint = stringtoprint+'*'
        print(stringtoprint)


# Press the green button in the gutter to run the script
if __name__ == '__main__':
    # TASK1
    print('###TASK1###')
    var1 = input("Enter your name:")  # read the user-input to variable var1
    var2 = input("Enter your age:")  # read the user-input to variable var2
    returnValue = name_age(var1, var2)  # pass the user-input into the function name_age
    print(returnValue)

    # TASK2
    print('###TASK2###')
    x = 10
    y = 20
    returnValue2 = swap_integers(x, y)
    print(returnValue2)

    # TASK3
    print('###TASK3###')
    number1 = 6
    number2 = 10
    returnValue3 = check_numbers(number1, number2)
    print(returnValue3)

    # TASK4
    print('###TASK4###')
    number1 = 3
    number2 = 9
    returnValue4 = sum_up(number1, number2)
    print(returnValue4)

    # TASK5
    print('###TASK5###')
    r1 = 2
    r2 = 4
    r3 = 5
    returnValue5 = circle_area(r1, r2, r3)
    print(returnValue5)

    # TASK6
    print('###TASK6###')
    example_text = 'Apollo moon fall'
    returnValue6 = check_string(example_text)
    print(returnValue6)

    #  TASK7
    print('###TASK7###')
    triangle(7)

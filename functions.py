def value_input():
    number = 1337
    print('Function: Value_Input', number)
    return number


def value_output(value):
    print('Function: Value_Output', value)


def main():
    number = value_input()
    value_output(number)


main()
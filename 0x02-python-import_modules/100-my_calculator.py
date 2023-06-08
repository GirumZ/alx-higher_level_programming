#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    number = len(sys.argv)

    if number != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = sys.argv[1]
    b = sys.argv[3]
    oper = sys.argv[2]
    if oper != '+' and oper != '-' and oper != '*' and oper != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if oper == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif oper == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif oper == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))

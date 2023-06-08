#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv)
    if number == 2:
        text = 'argument'
    else:
        text = 'arguments'
    print("{} {}:".format(number - 1, text))
    for i in range(1, number):
        print("{}: {}".format(i, sys.argv[i]))

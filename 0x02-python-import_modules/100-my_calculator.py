#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    lent = int(len(sys.argv))
    if lent != 4:
        sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    
    if op == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        sys.exit(0)
    elif op == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        sys.exit(0)
    elif op == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        sys.exit(0)
    elif op == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        sys.exit(0)
    else:
        ops = ['+', '-', '*', '/']
        for i in ops:
            if i != op:
                sys.stderr.write("Unknown operator. Available operators: +, -, * and /\n")
                sys.exit(1)

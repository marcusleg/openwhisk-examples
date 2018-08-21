#!/bin/python3

def fizzbuzz(n):
    if n % 15 == 0:
        return "fizzbuzz"
    if n % 5 == 0:
        return "buzz"
    if n % 3 == 0:
        return "fizz"
    return n

def main(args):
    n = int(args.get("n", 0))
    return {"result": fizzbuzz(n)}

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        sys.exit('Syntax is: ' + sys.argv[0] + ' <integer>')
    n = int(sys.argv[1])
    result = main({'n': n})
    print(result)

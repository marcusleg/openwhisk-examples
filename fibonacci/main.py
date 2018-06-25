#!/bin/python3
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def main(args):
    n = int(args.get("n", 0))
    return {"result": fib(n)}

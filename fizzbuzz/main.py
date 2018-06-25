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

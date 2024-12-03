import re

def compute_mul(input):
    number = 0
    pattern = re.compile(r"mul\((\d+),(\d+)\)")

    if str(type(input)) == "<class '_io.TextIOWrapper'>" :
        matches = pattern.findall(input.read())
    else:
        matches = pattern.findall(input)

    for match in matches:
        number += int(match[0]) * int(match[1])
    
    return number

def compute_mul_new(input):
    number = 0
    do_multiplication = True

    for line in input:
        tokens = re.split(r'(do\(\)|don\'t\(\))', line)

        for token in tokens:
            if token == "do()":
                do_multiplication = True
            elif token == "don't()":
                do_multiplication = False
            elif do_multiplication:
                number += compute_mul(token)

    return number


with open("day3/input.txt", "r") as input:
    print(compute_mul(input)) # 1
    input.seek(0)
    print(compute_mul_new(input)) # 2
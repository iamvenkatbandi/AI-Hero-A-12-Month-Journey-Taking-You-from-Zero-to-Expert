# Core Calculator Functions
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: Division by Zero"

print(add(2,4))
print(sub(6,4))
print(sub(2,8))
print(mul(2,6))
print(div(4,2))
print(div(2,4))
print(div(2,0))
print(div(0,4))

# Input Parsing with Error Handling
def parse_number(text):
    try:
        return float(text)
    except ValueError:
        raise ValueError(f"{text!r} is not a number")

def calculate(a_text, op, b_text):
    try:
        a = parse_number(a_text)
        b = parse_number(b_text)

        if op == "+":
            return add(a, b)
        elif op == "-":
            return sub(a, b)
        elif op == "*":
            return mul(a, b)
        elif op == "/":
            return div(a,b)
    except ValueError as e:
        return f"Input error: {e}"
    except ValueError as e:
        return "Error: Unknown Operator (use + - * /)"

print(calculate("4","+","6"))
print(calculate("2","-","4"))
print(calculate("4","-","2"))
print(calculate("2","*","4"))
print(calculate("8","/","4"))
print(calculate("4","/","0"))
print(calculate("0","/","4"))
print(calculate("4","%","2"))

# Interactive Loop
def repl():
    print("Simple Calculator — type 'q' to quit")
    while True:
        a = input("Enter first number (or 'q'): ").strip()
        if a.lower() == 'q':
            print("Goodbye!")
            break
        op = input("Operator (+ - * /): ").strip()
        b = input("Enter second number: ").strip()
        result = calculate(a, op, b)
        print("Result:", result)

repl()

# Quick self‑tests with assert
assert add(1,2) == 3
assert sub(5,3) == 2
assert mul(2,4) == 8
assert div(9,3) == 3
assert div(1,0), "Error: division by zero"
assert calculate("2","/","0"), "Error: division by zero"
assert "Not a number", calculate("x","+","1")
assert "unknown operator", calculate("1","^","2")
print("All quick tests passed ✅")
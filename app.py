import sys
import math

history = []

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Error: Divide by zero"
def power(a, b): return a ** b
def sqrt(a): return math.sqrt(a) if a >= 0 else "Error: Negative sqrt"
def factorial(a):
    if not a.is_integer() or a < 0:
        return "Error: Factorial requires non-negative integer"
    return math.factorial(int(a))

def clear_history():
    global history
    history = []
    print("History cleared.")

def print_help():
    print("Usage:")
    print(" python calc.py [add|sub|mul|div|pow|sqrt|fact|clear|history|help] num1 num2")
    print(" sqrt/fact only require num1 (num2 ignored)")
    print(" clear - clears history")
    print(" history - shows last 5 results")
    print(" help - this message")

ops = {
    'add': add,
    'sub': sub,
    'mul': mul,
    'div': div,
    'pow': power,
    'sqrt': sqrt,
    'fact': factorial
}

def main():
    if len(sys.argv) < 2:
        print_help()
        return

    cmd = sys.argv[1]

    if cmd == "help":
        print_help()
        return

    if cmd == "clear":
        clear_history()
        return

    if cmd == "history":
        for item in history[-5:]:
            print(item)
        return

    if cmd not in ops:
        print(f"Unknown command: {cmd}")
        print_help()
        return

    try:
        a = float(sys.argv[2])
        b = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
    except (IndexError, ValueError):
        print("Please provide valid numbers.")
        return

    if cmd in ['sqrt', 'fact']:
        result = ops[cmd](a)
        result_str = f"{cmd}({a}) = {result}"
    else:
        result = ops[cmd](a, b)
        result_str = f"{cmd}({a}, {b}) = {result}"

    history.append(result_str)
    print(result_str)

if __name__ == "__main__":
    main()


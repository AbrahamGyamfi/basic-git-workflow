import sys

history = []  # List to store results as formatted strings

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Error: Divide by zero"

ops = {'add': add, 'sub': sub, 'mul': mul, 'div': div}

def main():
    if len(sys.argv) < 2:
        print("Usage: python calc.py [add|sub|mul|div] num1 num2 | history")
        return
    
    cmd = sys.argv[1]
    if cmd == 'history':
        for item in history[-5:]:
            print(item)
        return
    
    if len(sys.argv) != 4 or cmd not in ops:
        print("Invalid command!")
        return
    
    try:
        a, b = float(sys.argv[2]), float(sys.argv[3])
        result = ops[cmd](a, b)
        result_str = f"{cmd}({a}, {b}) = {result}"
        history.append(result_str)
        print(result_str)
    except ValueError:
        print("Invalid numbers!")

if __name__ == "__main__":
    main()

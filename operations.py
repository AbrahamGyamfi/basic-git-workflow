# operations.py
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
    return "History cleared."


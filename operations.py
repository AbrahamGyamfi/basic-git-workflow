# operations.py
import math
import memory

history = []

def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

def mul(a, b): 
    return a * b

def div(a, b): 
    return a / b if b != 0 else "Error: Divide by zero"

def power(a, b): 
    return a ** b

def sqrt(a): 
    return math.sqrt(a) if a >= 0 else "Error: Negative sqrt"

def factorial(a):
    if not a.is_integer() or a < 0:
        return "Error: Factorial requires non-negative integer"
    return math.factorial(int(a))

def store_result(result):
    """Store last result in persistent memory."""
    return memory.store_memory(result)

def recall_from_memory():
    """Recall from persistent memory."""
    return memory.recall_memory()

def clear_persistent_memory():
    """Clear persistent memory."""
    return memory.clear_memory()


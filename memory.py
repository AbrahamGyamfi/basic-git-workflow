# memory.py
import json
import os

MEMORY_FILE = 'calc_memory.json'

def store_memory(value):
    """Store a value in persistent memory."""
    data = {'memory': float(value)}
    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f)
    return f"Memory stored: {value}"

def recall_memory():
    """Recall value from persistent memory."""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            data = json.load(f)
        return data['memory']
    return "No memory stored"

def clear_memory():
    """Clear persistent memory."""
    if os.path.exists(MEMORY_FILE):
        os.remove(MEMORY_FILE)
    return "Memory cleared"


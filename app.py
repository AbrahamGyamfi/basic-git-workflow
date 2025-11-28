# Add these to the cmd checks in main():
if cmd == "store":
    if 'result' in locals():
        print(operations.store_result(result))
    else:
        print("No result to store")
    return

if cmd == "recall":
    mem_value = operations.recall_from_memory()
    print(f"Memory: {mem_value}")
    return

if cmd == "clearmem":
    print(operations.clear_persistent_memory())
    return


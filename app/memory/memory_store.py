import json
import os

MEMORY_FILE = "outputs/memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(entry):
    memory = load_memory()
    memory.append(entry)

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)
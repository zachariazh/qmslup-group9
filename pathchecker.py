import os
import time

def pathchecker(filepath):
    if os.path.exists(filepath):
        return True
    else:
        print("\nWarning: Input filepath not found!\n")
        time.sleep(1.5)
        return False
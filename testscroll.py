import sys
import time

words = "You step into a forest and see whatever"
for char in words:
    time.sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
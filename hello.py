# Author: Brad Montgomery
# blah blah blah.

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
        print(f"Hello {name}!")
    else:
        print("hello world")

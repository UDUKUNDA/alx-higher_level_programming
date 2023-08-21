#!/usr/bin/python3
y = 0
for d in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(d - y)), end="")
    y = 32 if y == 0 else 0

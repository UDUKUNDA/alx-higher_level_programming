#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    length = 0
    try:
        for a in range(x):
            print(my_list[i], end =' ')
            length += 1
    except IndexError:
        print("\nTrying to access invalid index")
    print()
    return length


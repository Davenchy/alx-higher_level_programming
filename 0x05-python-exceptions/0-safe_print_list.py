#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for val in my_list:
            if counter >= x:
                break
            print(val, end="")
            counter += 1
    except Exception:
        pass
    finally:
        print()
    return counter

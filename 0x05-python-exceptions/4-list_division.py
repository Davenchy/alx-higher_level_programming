#!/usr/bin/python3

def list_division(my_list1, my_list2, list_length):
    results = list()
    for i in range(list_length):
        result = 0
        try:
            result = my_list1[i] / my_list2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            results.append(result)
    return results

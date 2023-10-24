#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
        Divide a list by list
    """
    div_list = []
    for i in range(list_length):
        try:
            div_list.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            div_list.append(0)
            print("wrong type")
        except ZeroDivisionError:
            div_list.append(0)
            print("division by zero")
        except IndexError:
            div_list.append(0)
            print("out of range")
        finally:
            pass
    return div_list

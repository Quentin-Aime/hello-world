# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import, print_function


variable_name_list = ["a", "b", "c", "d", "e", "f"]

def create_generator():
    while True:    # infinite loop used to come back at the beginning of the list if your number of iteration is higher than the list's len
        for variable in variable_name_list:
            yield variable

variable_list = create_generator()

print(next(variable_list)) # this will print the next value of the list, iterate AND save the iteration with the yield, just like a static variable in cpp

#!/usr/bin/python3
def to_subtract(list_num):
    """This function is good"""
    to_subs = 0
    max_lists = max(list_num)

    for o in list_num:
        if max_lists > o:
            to_subs += o

    return (max_lists - to_subs)

def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    lists_keys = list(rom_n.keys())

    nums = 0
    lasts_rom = 0
    list_num = [0]

    for cd in roman_string:
        for r_num in lists_keys:
            if r_num == cd:
                if rom_n.get(cd) <= lasts_rom:
                    nums += to_subtract(list_num)
                    list_num = [rom_n.get(cd)]
                else:
                    list_num.append(rom_n.get(cd))

                lasts_rom = rom_n.get(cd)

    nums += to_subtract(list_num)

    return (nums)

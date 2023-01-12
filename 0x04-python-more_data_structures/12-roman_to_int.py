#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    rom_val = dict(I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000)
    roman_string = roman_string.upper()
    subs = 0
    adds = 0
    used = 0
    if len(roman_string) == 1:
        return rom_val[roman_string[0]]
    st_list = [rom_val[l] for l in roman_string]
    for i in range(len(st_list)):
        if used == 1:
            used = 0
            st_list[i] = 0
            continue
        if i != len(st_list) - 1:
            if st_list[i] < st_list[i + 1]:
                subs += (st_list[i + 1] - st_list[i])
                st_list[i] = 0
                used = 1
    for n in st_list:
        adds += n
    num = adds + subs
    return num

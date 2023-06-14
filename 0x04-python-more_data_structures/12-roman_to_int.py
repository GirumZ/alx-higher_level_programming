#!/usr/bin/python3
def roman_to_int(roman_string):
    r = roman_string
    if r is None:
        return (0)
    if not isinstance(r, str):
        return (0)
    roman_conversion = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    r = r.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX")
    r = r.replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
    num = sum(map(lambda x: roman_conversion[x], r))
    return (num)

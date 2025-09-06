def roman(strs):
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    prev=roman_to_int[strs[0]]
    total=roman_to_int[strs[0]]
    for i in range(1, len(strs)):
        current= roman_to_int[strs[i]]
        if prev < current and prev >0:
            total=total+current-2*prev
        else:
            total+=current
        prev=current
    return total
print(roman('IV'))

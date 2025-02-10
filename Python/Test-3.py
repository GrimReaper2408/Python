str1 = input("Enter string: ")
char_count = {}
first_non_repeating = None
for char in str1:
    if char in char_count:
        char_count[char] += 1
        if first_non_repeating == char:
            first_non_repeating = None  
    else:
        char_count[char] = 1
        if first_non_repeating is None:
            first_non_repeating = char

    if first_non_repeating is None:
        for key, value in char_count.items():
            if value == 1:
                first_non_repeating = key
                break
if first_non_repeating:
    print(first_non_repeating)
else:
    print("-1")

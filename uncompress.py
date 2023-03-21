'''
Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:

<number><char>

for example, '2c' or '3a'.

The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.
'''

# def uncompress(s):
#     char = []
#     num = []

#     for ele in s:
#         if ele.isdigit():
#             num.append(ele)
#         else:
#             multiplier = ''.join(num)
#             char.append(ele*int(multiplier))
#             num.clear()

#     return ''.join(char)

# print(uncompress("2c3a1t"))
# print(uncompress("2p1o5p"))
# print(uncompress("3n12e2z"))
# print(uncompress("127y"))


## Two Pointer Stratigy
## two variables tracks indexies j find the end of number sequance i point the start of number portion

def uncompress(s):
    j = 0
    i = 0
    numbers = '0123456789'
    result = []

    while j < len(s):
        if s[j] in numbers:
            j += 1
        else:
            num = int(s[i:j])
            result.append(s[j]* num)
            j += 1
            i = j
    return ''.join(result)


print(uncompress("2c3a1t"))
print(uncompress("2p1o5p"))
print(uncompress("3n12e2z"))
print(uncompress("127y"))


## Complexity
## n = # of groups
## m = max number for any groups
## time = O(nm)
## space = O(nm)
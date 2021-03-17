'''
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"


'''

class Solution:
    def toHex(self, num: int) -> str:
        if not num:
            return '0'
        if num < 0:
            num += 2 ** 32
        s = '0123456789abcdef'
        res = ''
        while num:
            n = s[num & 15]
            res += n           #time complexity O(1) to append at the and, better than O(n) to append left in front of string
            num >>= 4
        return res[::-1]

    def toHex(self, num: int) -> str:
        s, res, num = '0123456789abcdef', '', num & 0xFFFFFFFF
        while num:
            res += s[num % 16]
            num >>= 4
        return res[::-1] or '0'
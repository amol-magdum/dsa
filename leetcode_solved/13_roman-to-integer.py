# Roman to Integer

# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in reversed(s):
            value = roman_numerals[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        
        return total
    
# time complexity: O(n) where n is length of string s
# space complexity: O(1) since the dictionary size is constant

# test cases
print(Solution().romanToInt("III"))      # 3        
print(Solution().romanToInt("IV"))       # 4
print(Solution().romanToInt("IX"))       # 9
print(Solution().romanToInt("LVIII"))    # 58
print(Solution().romanToInt("MCMXCIV"))  # 1994
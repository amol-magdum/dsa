class Solution:
    def romanToInt(self, s):
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        totalInInt = 0
        prev_value = 0
        for char in reversed(s):
            value = roman_numerals[char]
            if value < prev_value:
                totalInInt -= value
            else:
                totalInInt += value
            prev_value = value
        return totalInInt 

print(Solution().romanToInt("III"))      # 3        
print(Solution().romanToInt("IV"))       # 4
print(Solution().romanToInt("IX"))       # 9
print(Solution().romanToInt("LVIIIV"))    # 59
print(Solution().romanToInt("MCMXCIV"))  # 1994
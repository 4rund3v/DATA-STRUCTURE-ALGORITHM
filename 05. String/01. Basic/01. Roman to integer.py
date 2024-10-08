"""
Problem Statement: Given a roman numeral, convert it to an integer.
"""



class Solution:
    def romanToInt(self, s: str) -> int:
        val = {
                        "I":1,
                        "V":5,
                        "X":10,
                        "L":50,
                        "C":100,
                        "D":500,
                        "M":1000,
                        "IV": 4,
                        "IX": 9,
                        "XL": 40,
                        "XC": 90,
                        "CD": 400,
                        "CM": 900,
        }
        amount = 0 
        i = 0 
        while i < len(s):
            # check for len -1 as we are checking 2 nums 
            if i < len(s)-1 and s[i:i+2] in val :
                amount += val[s[i:i+2 ]]
                i+=2
            else:
                amount += val[s[i]]
                i+=1 
        return amount 
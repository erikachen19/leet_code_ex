#13. Roman to Integer
#Easy
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000
#For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, 
#which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
#Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
#Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
#The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.
#Given a roman numeral, convert it to an integer.
#
#Example 1:
#Input: s = "III"
#Output: 3
#
#Example 2:
#Input: s = "IV"
#Output: 4
#
#Example 3:
#Input: s = "IX"
#Output: 9
#
#Example 4:
#Input: s = "LVIII"
#Output: 58
#Explanation: L = 50, V= 5, III = 3.
#
#Example 5:
#Input: s = "MCMXCIV"
#Output: 1994
#Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# 
#
#Constraints:
#1 <= s.length <= 15
#s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
#It is guaranteed that s is a valid roman numeral in the range [1, 3999].
###############################################################################################
class Solution:
    def romanToInt(self, s: str) -> int:
        dictlist = {'I':1,'V':5,'X':10,
                   'L':50,
                   'C':100,
                   'D':500,
                   'M':1000}
        res = []
        for i in range(0,len(s)):
            print(i)
            #compre s[n-1]'s value  and s[n]'s value 
            if i !=0 and (dictlist[s[i]]>dictlist[s[i-1]]):
                #like "IV", (s[0] = I dictlist['I'] =1 , s[1] = V, dictlist['V'] =5), so s[0]<s[1], 
                #so s[0]'s value = s[0]'s value * -1 and s[1]=dictlist[s[1]] 
                nu = dictlist[s[i]]
                print('s[i-1]+s[i]')
                print(s[i-1]+s[i])
                res.append(nu)
                res[i-1]=res[i-1]*(-1)
                print(res)
            else:
                #like "IVI", (s[1] = V dictlist['V'] =5 , s[2] = I, dictlist['I'] =1), so s[1]>s[2], 
                #so s[2]'s value =dictlist[s[2]]               
                print('s[i]')
                print(s[i])
                nu = dictlist[s[i]]
                print('else')
                res.append(nu)                
                print(res)
                         
        return sum(res)            
###############################################################################################


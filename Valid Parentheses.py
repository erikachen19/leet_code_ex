#EASY
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
# 
#Example 1:
#Input: s = "()"
#Output: true
#
#Example 2:
#Input: s = "()[]{}"
#Output: true
#
#Example 3:
#Input: s = "(]"
#Output: false
#
#Example 4:
#Input: s = "([)]"
#Output: false
#
#Example 5:
#Input: s = "{[]}"
#Output: true
# 
#
#Constraints:
#1 <= s.length <= 104
#s consists of parentheses only '()[]{}'.
#####################################################
#SOLUTION
class Solution:
    def isValid(self, s: str) -> bool:
        key_dict = {"[":"]", "(":")","{":"}"}
        print(key_dict)
        b = []
        for i in s:
            if i in list(key_dict.keys()):
                b.append(i)                            # example 1: [{()}]: b = [ "[","{","(" ]
            elif len(b)>0 and key_dict[b[-1]]==i:      #if the next ")" -> b = [ "[","{" ],  "{"-> b = ["["], LIFO last in first out  
                b.pop()                                #example 2: {}()[]: b = ["{"]   the next "}" -> b = [] 
            else:                                      #example 3: ([)] : b = ["(", "["] the next needs to be "[" -> False
                return False
        if len(b)==0:
            return True
            
        

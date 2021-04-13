#3. Longest Substring Without Repeating Characters
#Medium
#Share
#Given a string s, find the length of the longest substring without repeating characters.
#Example 1:
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

#Example 2:
#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.

#Example 3:
#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

#Example 4:
#Input: s = ""
#Output: 0
#Constraints:
#0 <= s.length <= 5 * 104
#s consists of English letters, digits, symbols and spaces.

##########################################################################
#linguagem: Python3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = []
        max_len = 0
        for i in s:
            if i in ss:
                ss = ss[ss.index(i)+1:]
            # getting one substring at a time without repeating characters by order like "abcbcacc"-> 1"abc" 2"cb" 3"bca" 4"ac"5"c" 
            ss.append(i)
            #get aways the max length 
            max_len = max(max_len, len(ss))
        return max_len
 ##########################################################################
 

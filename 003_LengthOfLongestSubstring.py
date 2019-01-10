"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
	输入: "abcabcbb"输出: 3 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
	输入: "bbbbb"输出: 1解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
	输入: "pwwkew"输出: 3解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。     
	请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""

 class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 测试用例：dvdf 、 ohomm 、''、' '
        if s:
            maxStr = s[0]
            maxLen = 1
            resultLen = 0
            for t in s[1:]:
                if t in maxStr:
                    tempLen = len(maxStr)
                    if tempLen>maxLen:
                        maxLen = tempLen
                    maxStr += t
                    maxStr = maxStr[maxStr.index(t)+1:]
                else:
                    maxStr += t
                    resultLen = len(maxStr)
            return max(maxLen, resultLen)        
            
        else:
            return 0




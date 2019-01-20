# -*- coding:utf-8 -*-
"""
问题：
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
输入: 123
输出: 321
示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""
# 解答：
# 方法一：
# 时间复杂度：O（log（x））

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 符号位
        if x>0:
            TF=0
        else:
            TF=1
                 
        # 反转
        xNum=0; x=abs(x)
        while(x>0):
            xNum = xNum*10 + x%10
            x //= 10
                
        # 判断大小
        if (xNum>pow(2,31)-1) or (xNum<-pow(2,31)):
            return 0
        elif TF==1:
            return xNum*-1
        else:
            return xNum

# 方法二：
# 时间复杂度：O（n）

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        xStr = str(x)
        if xStr[0]!='-':
            xStr=xStr[::-1]
            return( int(xStr) if int(xStr)<2**31-1 else 0 )
        else:
            xStr=xStr[::-1][:-1]
            return( -int(xStr) if int(xStr)<2**31 else 0 )


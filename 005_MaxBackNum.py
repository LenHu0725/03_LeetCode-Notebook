 def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        max_length = 0
        palindromic = ''
        for i in range(l):
            x = 1
            while (i - x) >= 0 and (i + x) < l:
                if s[i + x] == s[i - x]:
                    x += 1
                else:
                    break
            x -= 1
            if 2 * x + 1 > max_length:
                max_length = 2 * x + 1
                palindromic = s[i - x:i + x + 1]
            x = 0
            if (i + 1) < l:
                while (i - x) >= 0 and (i + 1 + x) < l:
                    if s[i + 1 + x] == s[i - x]:
                        x += 1
                    else:
                        break
            x -= 1
            if 2 * x + 2 > max_length:
                max_length = 2 * x + 2
                palindromic = s[i - x:i + x + 2]
        if palindromic == '':
            palindromic = s
        return palindromic


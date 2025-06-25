# Longest
# Substring
# Without
# Repeating
# Characters
# Medium
# Topics
# premium
# lock
# icon
# Companies
# Hint
# Given
# a
# string
# s, find
# the
# length
# of
# the
# longest
# substring
# without
# duplicate
# characters.
#
# Example
# 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The
# answer is "abc",
# with the length of 3.
# Example
# 2:
#
# Input: s = "bbbbb"
# Output: 1
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        charset = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[right])
            max_length = max(max_length, right-left+ 1)
        return max_length

if __name__ == "__main__":
    sol = Solution()
    len =sol.lengthOfLongestSubstring('abcabcbb')
    print(len)




#  Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.



# Approach: Dynamic Programming
# The problem can be solved using dynamic programming because it involves breaking the string into smaller subproblems and checking if each prefix can be segmented. Here’s the intuition:
#
# Define a DP array dp[i] where dp[i] is True if the substring s[0:i] (prefix of length i) can be segmented into words from wordDict.
# For each position i in s, check all possible substrings s[j:i] (where j < i) to see if:
# s[j:i] is a word in wordDict, and
# dp[j] is True (the prefix before j can be segmented).
# If both conditions hold, set dp[i] = True.
# The final answer is dp[len(s)], indicating whether the entire string can be segmented.
# To optimize lookups, convert wordDict to a set

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Convert wordDict to set for O(1) lookups
        word_set = set(wordDict)

        # dp[i] represents whether s[0:i] can be segmented
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Empty string is always valid

        # Iterate over each position i in s
        for i in range(1, len(s) + 1):
            # Check all possible starting positions j for substring s[j:i]
            for j in range(i):
                # If s[0:j] is valid and s[j:i] is in wordDict, mark s[0:i] as valid
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        # if the last one is true then the whole string can be derived form work dict
        return dp[len(s)]

if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    sol = Solution()
    sol.wordBreak(s, wordDict)
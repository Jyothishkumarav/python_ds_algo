class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i):
                if s[j:i] in wordSet and dp[j]:
                    dp[i] = True
                    break
        return dp[len(s)]

if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    sol = Solution()
    print(sol.wordBreak(s, wordDict))



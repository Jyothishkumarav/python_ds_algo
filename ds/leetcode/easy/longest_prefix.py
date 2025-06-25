# Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string ""

class Solution:
    def longestCommonPrefix(self, strs: list[str]):
        if not strs :
            return ""
        if len(strs) == 1:
            return strs[0]
        min_length = min(len(s) for s in strs)
        for i in range(min_length):
            char = strs[0][i]
            for text in strs:
                if text[i] != char:
                    return strs[0][:i]

        return strs[0][:min_length]


if __name__ == '__main__':
    sol = Solution()
    pref = sol.longestCommonPrefix(["flower","flow","flight"])
    print(pref)

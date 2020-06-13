class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0 or len(wordDict) == 0:
            return False

        wordDict = set(wordDict)
        n = len(s)
        dp = [0] * (n + 1)  # dp[i] = 1 if substring [0:i) can be divided into words
        dp[0] = 1  # empty string '' can be divided forever

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] == 1 and (s[j:i] in wordDict):
                    dp[i] = 1

        return dp[n]
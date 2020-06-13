class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if len(s) == 0 or len(wordDict) == 0:
            return

        # judge if s can be divided by DP
        wordDict = set(wordDict)
        n = len(s)
        dp = [0] * (n + 1)  # dp[i] = 1 if substring [0:i) can be divided
        dp[0] = 1  # empty string '' can be divided forever
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] == 1 and s[j:i] in wordDict:
                    dp[i] = 1

        # recursively find results
        res = []
        path = []

        def dfs(s):
            if len(s) == 0:
                res.append(' '.join(path))

            for i in range(len(s)):
                word = s[:i + 1]  # be careful about boundary
                if word in wordDict:
                    path.append(word)
                    dfs(s[i + 1:])
                    path.pop()

        if dp[n] == 1:  # if s can be divided, dfs
            dfs(s)

        return res
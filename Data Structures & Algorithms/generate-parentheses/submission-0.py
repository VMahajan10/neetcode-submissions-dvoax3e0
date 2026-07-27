class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sublevel = []


        def backtrack(nOpen, nClosed):
            if nOpen == nClosed == n:
                res.append("".join(sublevel))
                return 

            if nOpen < n:
                sublevel.append("(")
                backtrack(nOpen + 1, nClosed)
                sublevel.pop()

            if nClosed < nOpen:
                sublevel.append(")")
                backtrack(nOpen, nClosed + 1)
                sublevel.pop()

        backtrack(0, 0)
        return res

            
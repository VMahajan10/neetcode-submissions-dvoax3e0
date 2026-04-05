class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        res = []

        for i in tokens:
            if i == "+":
                res.append(res.pop() + res.pop())

            elif i == "-":
                a = res.pop()
                b = res.pop()
                res.append(b - a)

            elif i == "*":
                res.append(res.pop() * res.pop())

            elif i == "/":
                a = res.pop()
                b = res.pop()
                res.append(int(float(b)/a))
            else:
                res.append(int(i))
        
        return res[0]

        
        
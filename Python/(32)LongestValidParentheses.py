class Solution:
    def longestValidParentheses(self, s: str) -> int:
    #time complexity: O(N)
    #space complexity: O(N)

        stack = [-1]
        max_length = 0

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                stack.pop()

                if stack:
                    max_length = max(max_length, i - stack[-1])
                else:
                    stack.append(i)

        return max_length
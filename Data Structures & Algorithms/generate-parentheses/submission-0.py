"""
input:
    int - n
output:
    list of every possible valid unique string that can be created with n pairs of parentheses

each valid string would be len of 2n

1 pair only 1 valid string possible
["()"]

2 pairs 2 valid
()()
(())

3 pairs 5 valid 
()()()
((()))
(()) ()
() (())
(()())

so always can have n pairs side by side
and then n pairs nested

when you have n pairs, you can nest n - 1 pairs inside 

so what are our decisions that we can make

3 pairs to use

so on every open, we can pair with a close or pair with another open 

we should skip when adding the open or close will create an invalid prefix so we're only creating valid states

    when close count + 1 > open count and open count + 1 > n
        skip
(()())( still invalid


backtrack(array)
    if len(array) == 2n
        add it to valid
    
    for i in range(2n):
        when open count + 1 > n
            skip
        add (
        recurse on new state
        undo
        when close count + 1 > open count
            skip
        add )
        recurse on new state
        undo
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = []
        path = []

        def backtrack(open_count, close_count):
            if len(path) == 2 * n:
                parentheses.append("".join(path))
                return
            
            if open_count < n:
                path.append('(')
                backtrack(open_count + 1, close_count)
                path.pop()
            
            if close_count + 1 <= open_count:
                path.append(')')
                backtrack(open_count, close_count + 1)
                path.pop()
            
        backtrack(0, 0)
        return parentheses
        
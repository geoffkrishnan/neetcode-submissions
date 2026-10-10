class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s_g = sorted(g)
        s_s = sorted(s)
        print(s_g)
        print(s_s)
        max_content = 0
        i, j = 0, 0
        while i < len(s_g) and j < len(s_s):
            if s_g[i] <= s_s[j]:
                max_content += 1
                i += 1
                j += 1
            else:
                j += 1
                
        
            
        return max_content

        
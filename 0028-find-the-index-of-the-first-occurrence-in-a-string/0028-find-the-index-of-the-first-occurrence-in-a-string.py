class Solution:
    def strStr(self, haystack, needle):
        h_len, n_len = len(haystack), len(needle)
        
        if n_len == 0:
            return 0
        
  
        for i in range(h_len - n_len + 1):
            
            if haystack[i:i + n_len] == needle:
                return i
        
        return -1


param_1 = "sadbutsad"
param_2 = "sad"
solution = Solution()  
ret = solution.strStr(param_1, param_2)  
print(ret)  

param_1 = "leetcode"
param_2 = "leeto"
ret = solution.strStr(param_1, param_2)
print(ret) 
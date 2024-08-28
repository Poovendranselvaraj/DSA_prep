
strs = ["flower","flow","flight"]
class Solution(object):
    def longestCommonPrefix(self, strs):
         
     if not strs:
       return ""
    
     else:
      min(strs)[0:next((i for i, c in enumerate(zip(*strs)) 
    if len(set(c)) > 1), len(min(strs)))]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ''
        stop = False

        for i in range(len(strs[0])):

            if stop:
                return commonPrefix

            for j in strs:

                if i >= len(j):
                    stop = True
                    break
                
                if strs[0][i] != j[i]:
                    stop = True
                    break
            
            if not stop:
                commonPrefix += strs[0][i]
        
        return commonPrefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ''
        for chars in zip(*strs):
            if len(set(chars))==1:
                commonPrefix += chars[0]
            else:
                break
        return commonPrefix

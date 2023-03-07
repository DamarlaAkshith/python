class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        res=[]
        def helper(ind,str):
            if ind==len(digits):
                res.append(str)
            else:
                for i in phone[digits[ind]]:
                    helper(ind+1,str+i)
        helper(0,'')
        return res




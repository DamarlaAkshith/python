class Solution:
    def intToRoman(self, num: int) -> str:
        values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        romans = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
        ans = ""
        for roman, value in zip(romans, values):
            if num >= value:
                count, num = divmod(num, value)
                ans += count * roman
        return ans

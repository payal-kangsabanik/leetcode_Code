class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        y=words[::-1]
        return ' '.join(y)
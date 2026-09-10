class Solution:

    def shortestCompletingWord(self, license_plate: str, words: List[str]) -> str:
        letters = Counter(ltr.lower() for ltr in license_plate if ltr.isalpha())
        return min((word for word in words if not letters - Counter(word)), key=len)
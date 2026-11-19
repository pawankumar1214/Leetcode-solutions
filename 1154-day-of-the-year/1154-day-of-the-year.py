class Solution:
    def dayOfYear(self, date: str) -> int:
        
        year, month, day = map(int, date.split("-"))

        days_in_month = [
            31,
            28,
            31,
            30,
            31,
            30,
            31,
            31,
            30,
            31,
            30,
            31
        ]

        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            days_in_month[1] = 29
        
        total = 0
        for i in range(month - 1):
            total += days_in_month[i]
        
        total += day
        return total
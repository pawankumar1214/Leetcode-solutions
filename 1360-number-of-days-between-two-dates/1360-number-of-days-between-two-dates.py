class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def is_leap(year):
            if year % 400 == 0:
                return True
            if year % 100 == 0:
                return False
            return year % 4 == 0
    
        def days_until(date):
            year, month, day = map(int, date.split("-"))

            month_days = [31, 28, 31, 30, 31, 30, 31 ,31, 30, 31, 30, 31]

            total_days = 0

            for y in range(1971, year):
                if is_leap(y):
                    total_days += 366
                else:
                    total_days += 365
            
            for m in range(1, month):
                total_days += month_days[m-1]
                if m == 2 and is_leap(year):
                    total_days += 1
            
            total_days += day
            return total_days
    
        days1 = days_until(date1)
        days2 = days_until(date2)

        return abs(days1 - days2)
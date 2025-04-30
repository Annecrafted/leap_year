from calendar import month, day_abbr


class DateCalculator:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

        if self.month in[1,2]:
           self.month+=12
           self.year-=1

    def calculate_day_of_week(self):
         Y=self.year
         m = self.month
         q = self.day
         K=Y%100
         J=Y//100

         h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 + (5 * J)) % 7

         weekdays=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
         return weekdays[h]

print(DateCalculator(2013, 7, 200).calculate_day_of_week())





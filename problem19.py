# Problem 19 - counting sundays
#You are given the following information, but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from datetime import date
from datetime import timedelta
startdate = date(1901,1,1)
enddate = date(2000,12,31)

daysbetween = enddate - startdate


# loop over alle dage mellem de to datoer og tjek om det er en søndag d.1
sum = 0
for date in range(0, daysbetween.days):
    currentdate = startdate + timedelta(days=date)
    if(currentdate.weekday() == 6 and currentdate.day == 1):
        sum += 1

print(sum)

# You are given the following information, but you may prefer to do some
# research for yourself.
#     * 1 Jan 1900 was a Monday.
#     * Thirty days has September,
#       April, June and November.
#       All the rest have thirty-one,
#       Saving February alone,
#       Which has twenty-eight, rain or shine.
#       And on leap years, twenty-nine.
#     * A leap year occurs on any year evenly divisible by 4, but not on
#       a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?

from datetime import date

begin_date = date(1901,1,6) # first Sunday of 20th century
end_date = date(2000,12,31)

sunday_first_of_month_count = 0

current = begin_date
while current <= end_date:
    if current.weekday() == 6 and current.day == 1:
        sunday_first_of_month_count += 1

    current = date.fromordinal(current.toordinal() + 7)

print sunday_first_of_month_count

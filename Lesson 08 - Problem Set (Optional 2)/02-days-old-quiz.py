# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#


'''
def days(month1, month2)
    
    daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_months = 0
    delta_months = abs(month2 - month1)
    
    while delta_months > 0:
        if month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7,
        or month1 == 8 or month1 == 10 or month1 == 12:
            days_in_months = 31
        elif month1 == 4 or month1 == 6 or month1 == 9 or month1 == 11:
            days_in_months = 30
        else:
            days_in_months = 28
        ...
        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    leap_day = 0
    leap_year = year1
    delta_years = year2 - year1
    while delta_years > 0:
        if leap_year % 4 == 0 and (leap_year % 100 != 0 or leap_year % 400 == 0):
            leap_day = leap_day + 1
            leap_year = leap_year + 1
            delta_years = delta_years - 1
        else:
            leap_year = leap_year + 1
            delta_years = delta_years - 1
        return leap_day
    
    daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_years = (year2 - year1)
    total_days_in_months = sum(daysOfMonths[month1-1:month2-1])
    
    total_days = total_years * 365 + total_days_in_months + abs(day2 - day1) + leap_day
    
    return total_days
'''


def days_in_month(n):
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][n-1]


def leap_days(month, day, year):
    days = 365
    # Now need to do if it is leap year
    if (year % 4 == 0) and (year % 100 != 0) and (month > 2):
        days = days + 1
    return days


def days_since_0(month, day, year):
    days = year * 365 + day
    for n in range(1, month):
        days = days + days_in_month(n)
    return days + leap_days(month, day, year)


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    return days_since_0(month2, day2, year2) - days_since_0(month1, day1, year1)


# Test routine
def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


test()

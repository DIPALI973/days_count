# First, we will create a class for dates  
class date_n:  
    def __init__(self, day, month, year):  
        self.day = day  
        self.month = month  
        self.year = year  
   
   
# For storng number of days in all months from  
# January to December.  
month_Days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
   
# This function will count the number of leap years from 00/00/0000 to the #given date  
   
   
def count_Leap_Years(day):  
   
    years = day.year  
   
    # Now, it will check if the current year should be considered for the count          # of leap years or not.  
    if (day.month <= 2):  
        years -= 1  
   
    # The condition for an year is a leap year: if te year is a multiple of 4, and a            # multiple of 400 but not a multiple of 100.  
    return int(years / 4) - int(years / 100) + int(years / 400)  
   
   
# This function will return number of days between two given dates  
def get_difference(date_1, date_2):  
   
    # Now, it will count total number of days before first date "date_1"  
   
    # Then, it will initialize the count by using years and day  
    n_1 = date_1.year * 365 + date_1.day  
   
    # then, it will add days for months in the given date  
    for K in range(0, date_1.month - 1):  
        n_1 += month_Days[K]  
   
    # As every leap year is of 366 days, we will add   
    # a day for every leap year  
    n_1 += count_Leap_Years(date_1)  
   
    # SIMILARLY, it will count total number of days before second date "date_2"  
   
    n_2 = date_2.year * 365 + date_2.day  
    for K in range(0, date_2.month - 1):  
        n_2 += month_Days[K]  
    n_2 += count_Leap_Years(date_2)  
   
    # Then, it will return the difference between two counts  
    return (n_2 - n_1)  
   
   
# Driver program  
date_1 = date_n(12, 10, 2021)  
date_2 = date_n(30, 8, 2022)  
   
print ("Number of Days between the given Dates are: ", get_difference(date_1, date_2), "days")  
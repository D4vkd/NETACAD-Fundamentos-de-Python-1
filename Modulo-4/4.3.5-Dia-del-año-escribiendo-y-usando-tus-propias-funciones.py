def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if is_year_leap(year) == True and month == 2: 
        return 29 
    else:
        return month_list [month - 1]

def day_of_year(year, month, day):
    total_days = 0
    for i in range(month - 1): 
        total_days = total_days + days_in_month(year, i + 1)
    if day > days_in_month(year, month) or day <= 0: 
        return None
    else: 
        return total_days + day 

print(day_of_year(2000, 12, 31))
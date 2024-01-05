def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year:int , month:int) -> int:
    """This Function is used to take year and month as number and return days of that month."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    check_year = is_leap(year)
    if check_year:
        if month == 2:
            return month_days[month -1] + 1
    return month_days[month - 1]
          
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

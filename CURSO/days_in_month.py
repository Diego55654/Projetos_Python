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
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

test_years = [1900, 2000, 2016, 1987, 2026]
test_months = [2, 2, 1, 11, 1]
test_results = [28, 29, 31, 30, 31]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "-> ", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


"""

Output:

1900 2 -> OK
2000 2 -> OK
2016 1 -> OK
1987 11 -> OK
2026 1 -> OK

"""
# Extra tests (not included list)
print(f"1300 year in 10th month: {days_in_month(1300, 10)}")   # None
print(f"2026 year in the first month: {days_in_month(2026, 1)}")    # 31
print(f"1900 year in the second month: {days_in_month(1900, 2)}")    # 28

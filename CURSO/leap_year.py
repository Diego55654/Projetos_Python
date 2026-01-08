"""
Check if each element in the test_data list corresponds to a leap year, returning a boolean value 
and comparing it to the expected result from the list.def is_year_leap(year):
"""
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

print(is_year_leap(1900))  # False, expected
print(is_year_leap(2000))  # True, expected
print(is_year_leap(1980))  # True, expected

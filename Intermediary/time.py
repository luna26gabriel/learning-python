import time
# print(time.ctime(1620651500))
# print(time.time())
# print(time.ctime(time.time()))
# time_object = time.localtime()

# # print(time_object)
# local_time = time.strftime("%A %d %Y %H:%m:%S", time_object)
# print(local_time)


# %a-Locale’s abbreviated weekday name.
# %A-Locale’s full weekday name.
# %b-Locale’s abbreviated month name.
# %B-Locale’s full month name.
# %c-Locale’s appropriate date and time representation.
# %d-Day of the month as a decimal number [01,31].
# %H-Hour (24-hour clock) as a decimal number [00,23].
# %I-Hour (12-hour clock) as a decimal number [01,12].
# %j-Day of the year as a decimal number [001,366].
# %m-Month as a decimal number [01,12].
# %M-Minute as a decimal number [00,59].
# %p-Locale’s equivalent of either AM or PM.(1)
# %S-Second as a decimal number [00,61].(2)
# %U-Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.(3)
# %w-Weekday as a decimal number [0(Sunday),6].
# %W-Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.(3)
# %x-Locale’s appropriate date representation.
# %X-Locale’s appropriate time representation.
# %y-Year without century as a decimal number [00,99].
# %Y-Year with century as a decimal number.
# %z-Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM, where H represents decimal hour digits and M represents decimal minute digits [-23:59, +23:59].
# %Z-Time zone name (no characters if no time zone exists).
# %%-A literal '%' character.




# time_string = "10 May, 2021"
# time_object = time.strptime(time_string, "%d %B, %Y")
# print(time_object)



time_tuple = (2021, 5, 10, 4, 20, 0, 2, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

time_tuple = (2021, 5, 10, 4, 20, 0, 2, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)
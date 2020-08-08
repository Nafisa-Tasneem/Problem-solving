year = int(input().strip())

def dayOfProgrammer(year):

    if year == 1918:
        day = 256 - (31 + 15 + 31 + 30 + 31 + 30 + 31 + 31)

    else:
        isLeap = False  # not leap year

        if year in range(1700,1918): # julian calender
            if year % 4 == 0:
                isLeap = True # leap year

        else:
            if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):

                isLeap = True

        if isLeap == False :
            day = 256 - (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31)

        else:
            day = 256 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31)

    date = ('%r.09.%r' % (day, year))

    return date

result = dayOfProgrammer(year)
print(result)
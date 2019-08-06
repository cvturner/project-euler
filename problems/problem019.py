'''
Catherine Turner
8/5/19
https://projecteuler.net/ Problem 19
'''

daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Given the first day of a certain year, returns a list including the first day of the week of every month of the
# years in that range (inclusive)
def firstDayOfMonths(firstDay, firstYear, lastYear):

    firstDays = []
    monthsOfYear = daysOfMonth
    year = firstYear
    currentDay = firstDay

    while year <= lastYear:
        currentIndex = daysOfWeek.index(currentDay)
        firstDays.append(currentDay)

        if (year % 4 == 0) and (year % 100 != 0):
            monthsOfYear[1] = 29
        elif (year % 400 == 0):
            monthsOfYear[1] = 29
        else:
            monthsOfYear[1] = 28

        monthCount = 0

        while monthCount < 11:
            firstDays.append(daysOfWeek[(currentIndex + monthsOfYear[monthCount]) % 7])
            currentIndex = (currentIndex + monthsOfYear[monthCount]) % 7
            monthCount += 1

        if monthCount == 11:
            currentDay = daysOfWeek[(currentIndex + monthsOfYear[11]) % 7]

        year += 1

    return firstDays

# Count occurrences of "Sunday" in the returned list
print((firstDayOfMonths("Tuesday", 1901, 2000)).count("Sunday"))

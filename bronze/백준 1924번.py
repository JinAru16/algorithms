import calendar
x, y = map(int, input().split())
dayList = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

def findDay(x, y):
    theDay = calendar.weekday(2007, x, y)
    return dayList[theDay]



print(findDay(x, y))
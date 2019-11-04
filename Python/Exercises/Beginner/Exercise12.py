''' formatmonth(theyear, themonth, w=0,l=0)
 Returns a month's calendar in multi-line string. 
 
 If w is provided, it specifies the width of the date columns, which are centered. 
 
 If l is given, it specifies the number of lines that each week will use. Depends on the first weekday as specified in the constructor or set by the setfirstweekday() method.
'''
import calendar

cal = calendar.TextCalendar(firstweekday=0)
year = 2019
month = 10
width = 6
lines = 2

print(cal.formatmonth(year, month, width, lines))

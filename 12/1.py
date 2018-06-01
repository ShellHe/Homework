import calendar

cal = calendar.TextCalendar()

cal.pryear(2012)



cal = calendar.TextCalendar(3)

cal.pryear(2018)


cal = calendar.TextCalendar(6)

cal.prmonth(2018, 8)


d = calendar.LocalTextCalendar(6,"CHINESE")

d.pryear(2012)


print(calendar.isleap(8))


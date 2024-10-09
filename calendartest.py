import calendar

def display_calendar(year,month=None):
    if month:
        print(calendar.month(year,month))
    else:
        print(calendar.calendar(year))

year = int(input('年を入力してください：'))
month = input('（必須はない）月を入力してください：')
if month:
    display_calendar(year,int(month))
else:
    display_calendar(year)
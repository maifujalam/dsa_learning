import calendar,sys
#print(calendar.TextCalendar().formatyear(2020))

sys.stdin=open('input.txt')

def get_day(dd,mm,yyyy):
    print((calendar.day_name[calendar.weekday(yyyy,mm,dd)]).upper())

if __name__ == "__main__":
    mm,dd,yyyy=map(int,input().split())
    get_day(dd,mm,yyyy) 
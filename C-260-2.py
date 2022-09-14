import datetime
today=datetime.date.today()
yesterday=today-datetime.timedelta(days=1)
tommorrow=today+datetime.timedelta(days=1)
print("today's date : ",today)
print("yesterday's date : ",yesterday)
print("Tommorrow's Date : ",tommorrow)
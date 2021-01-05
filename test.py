import datetime
s = '06142018123721'

print( datetime.datetime.strptime(s, "%m%d%Y%H%M%S").strftime("%m/%d/%Y %H:%M:%S"))

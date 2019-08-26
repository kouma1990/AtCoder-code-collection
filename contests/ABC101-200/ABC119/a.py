import datetime
a = input().split("/")

date1 = datetime.datetime(int(a[0]), int(a[1]), int(a[2]))
date2 = datetime.datetime(2019, 4, 30)

if date1 > date2:
    print("TBD")
else:
    print("Heisei")
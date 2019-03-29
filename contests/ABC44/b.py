s = input()
import collections

c = collections.Counter(s)

if len(list(filter(lambda x:x%2==1,c.values()))) > 0:
    print("No")
else:
    print("Yes")
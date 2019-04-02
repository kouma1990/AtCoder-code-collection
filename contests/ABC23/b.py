n = int(input())
s = input()

now = "b"
cnt = 0

def check():
    if s==now:
        print(cnt)
        exit()

    if len(s) < len(now):
        print(-1)
        exit()

while True:
    check()
    now = "a"+now+"c"
    cnt+=1
    check()
    now = "c"+now+"a"
    cnt+=1
    check()
    now = "b"+now+"b"
    cnt+=1 


from queue import Queue

R,C = (int(i) for i in input().split())
sy,sx = (int(i)-1 for i in input().split())
gy,gx = (int(i)-1 for i in input().split())
c = [input() for i in range(R)]

q = Queue()
done = [[-1 for i in range(C)] for j in range(R)]

q.put((sy,sx))
done[sy][sx]=0

while True:
    if q.empty():
        break

    else:
        y,x = q.get()
        cnt = done[y][x]+1

        if x!=0 and done[y][x-1]==-1 and c[y][x-1]==".":
            q.put((y,x-1))
            done[y][x-1]=cnt
        
        if y!=0 and done[y-1][x]==-1 and c[y-1][x]==".":
            q.put((y-1,x))
            done[y-1][x]=cnt
        
        if x!=C-1 and done[y][x+1]==-1 and c[y][x+1]==".":
            q.put((y,x+1))
            done[y][x+1]=cnt

        if y!=R-1 and done[y+1][x]==-1 and c[y+1][x]==".":
            q.put((y+1,x))
            done[y+1][x]=cnt

print(done[gy][gx])
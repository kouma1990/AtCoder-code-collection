deg, dis = input().split()
dir_moji = ['NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
wind_list = [0.2,1.5,3.3,5.4,7.9,10.7,13.8,17.1,20.7,24.4,28.4,32.6,2000]
def custom_round(number, ndigits=0):
    if type(number) == int:
        return number
    d_point = len(str(number).split('.')[1])
    if ndigits >= d_point:
        return number
    c = (10 ** d_point) * 2
    return round((number * c + 1) / c, ndigits)
 
dirs = 'N'
con = 3600/16
for i in range(len(dir_moji)):
    if 112.5 + con * i <= int(deg) < 337.5 + con * i:
        dirs = dir_moji[i]
        break
 
dis_s = float(dis)/60.0
for i in range(len(wind_list)):
    if custom_round(dis_s, 1) <= wind_list[i]:
        deg = i
        if i == 0:
            dirs = 'C'
        break
 
print(dirs, deg)
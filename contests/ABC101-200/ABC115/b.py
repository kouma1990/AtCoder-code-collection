n = int(input()) 
prices = [int(input()) for i in range(n)] 

max_price = 0
sum_price = 0
for price in prices:
    sum_price += price
    if price > max_price:
        max_price = price

sum_price -= max_price/2

print(int(sum_price))
a, b = (int(i) for i in input().split())  

def f(a, b):
    num_len = b-a+1

    if num_len == 1:
        return b

    one_check = num_len if a % 2 == 0 else num_len-1

    x = (one_check // 2) % 2
    y = b if one_check % 2 == 1 else 0
    z = 0 if a % 2 == 0 else a
    return x^y^z

print(f(a,b))

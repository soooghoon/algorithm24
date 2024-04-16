def sub(n):
    global a
    if n <= 1:return n 
    a += 2  
    return sub(n-1) + sub(n-2)

a = 1 
sub(3)
print("sub() 함수가 호출된 총 횟수:", a)
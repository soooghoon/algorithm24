def unique_elements(A):
    n = len(A)
    for i in range(n-1):
        for j in range(i+1, n):
            if A[i] == A[j]:
                return False
    return True


A = [32, 14, 5, 17, 23, 9, 11,14,26,29]
B = [13, 6, 8, 7, 12, 25]

print(f"A: {A}, Unique Elements: {unique_elements(A)}")
print(f"B: {B}, Unique Elements: {unique_elements(B)}")
def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b
print(climbStairs(2))  
print(climbStairs(3))  
print(climbStairs(4))  
print(climbStairs(5))

#2
#3
#5
#8

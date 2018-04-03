# FIND THE SUM OF ALL MULTIPLES OF 3 AND 5 LESS THAN 1000
ans = 0;
for x in range(0, 1000):
    if x%3==0:
        ans += x
    elif x%5==0:
        ans += x
print(ans)

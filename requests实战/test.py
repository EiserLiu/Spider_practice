
p = 0
for i in range(200):
    if i % 3 and i % 5 and i % 7 == 0:
        p = p + i
print(p)

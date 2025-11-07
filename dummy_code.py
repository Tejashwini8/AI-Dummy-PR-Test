# inefficient code example
data = [i for i in range(10000)]
result = []
for i in data:
    if i % 2 == 0:
        result.append(i * 2)
print(sum(result))

# inefficient code example
# optimized version with generator expression
data = range(10000)
result = (i * 2 for i in data if i % 2 == 0)
print(sum(result))



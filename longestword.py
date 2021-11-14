words = open('data/sowpods.txt')
max = 0
max_count = 0
for line in words:
    l = len(line.strip())
    if l == max:
      print(line)
      max_count = max_count + 1
    if l > max:
      print(line)
      max = l
      max_count = 0

print("max: ", max)
print("max_count: ",max_count)

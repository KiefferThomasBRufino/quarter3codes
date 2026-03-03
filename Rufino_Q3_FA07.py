steps = [
  [4500, 5200, 4800, 5000, 5300],  
  [4000, 4100, 3900, 4200, 4600],  
  [6000, 5800, 5900, 6100, 6200]  
]

for i in range(len(steps)):
  total = sum(steps[i])
  print("Total of Row", i + 1, ":", total)


for i in range(len(steps)):
  total = sum(steps[i])
  print("Total of Row", i + 1, ":", total)

for i in range(len(steps)):
  total = sum(steps[i])
  average = total / len(steps[i])
  print("Average of Row", i + 1, ":", average)

maximum = steps[0][0]

for row in steps:
  for value in row:
    if value > maximum:
      maximum = value

print("Maximum value in dataset:", maximum)

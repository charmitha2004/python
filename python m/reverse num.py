def sumsquare(l):
  odd_sum = 0
  even_sum = 0
  for num in 1:
    if num%2 == 0:
       even_sum +=num**2
    else:
       odd_sum +=num**2
  return[odd_sum,even_sum]
n = int(input("enter the number of elements:"))
l = []
for i in range(n):
  l.append(int(input("enter the elements:")))
output = sumsquare(l)
print(output)

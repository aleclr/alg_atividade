a = 15000
b = 45000
c = 65000*1.025
anos = 0

while a <= b:
  a = a*1.10
  b = b*1.05
  anos = anos+1
print('A ultrapassará ou igualará com B em: ',anos,' anos')
while a < c*1.23:
  c = c*1.23
  anos = anos+1
print('A ultrapassará C em 23% em: ',anos, 'anos')
  
  
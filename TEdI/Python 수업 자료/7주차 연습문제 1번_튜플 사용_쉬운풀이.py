max, min = 0, 50
mm, nn = 'a', 'b'
weather =  [('9월', 26), ('10월', 20), ('11월', 12), ('12월', 4)]

for x, y in weather:
  if(max < y):
    mm, max = x, y
  if(y < min):
    nn,min = x, y
print("최고 온도 : %s %d도"%(mm,max))
print("최저 온도 : %s %d도"%(nn,min))
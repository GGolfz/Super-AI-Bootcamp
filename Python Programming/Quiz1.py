#  22p21c0568-วิศรุต
nameList = ['winn','thanarak','somchai','ricky','tao','wanida','peerapol']
def countnamewithalphabet(nameList,alphabet):
  count = 0
  for name in nameList:
    count += 1 if alphabet in name else 0
  return count
print(countnamewithalphabet(nameList,'n'))
print(countnamewithalphabet(nameList,'a'))
print(countnamewithalphabet(nameList,'r'))


#二分法
import random
import math


for i in range(0,101):
  ans = i
  print("答案: "+str(ans))
  max = 100
  min = 0
  counter = 1
  c1guess = 50
  while(True): 
    if(c1guess<=max and c1guess>=min):
      if(c1guess>ans): #猜太大
        max = c1guess
        c1guess = round((c1guess+min)/2)

        counter+=1
      elif(c1guess<ans): #猜太小
        min = c1guess
        c1guess = round((max+c1guess)/2)

        counter+=1
      elif(c1guess == ans):
        print("我猜了" + str(counter)+"次")
        break

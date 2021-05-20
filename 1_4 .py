#1/4
import random
import math

#ans = random.randint(0,100)# 秘密數字
c1guess = 25
counter = 1

#print("我猜: "+str(c1guess))

for i in range(0,101):
  ans = i
  max = 100
  min = 0
  counter = 1
  c1guess = 25
  
  print(str(ans))
  
  while(True): 
    if(c1guess<=max and c1guess>=min):
      if(c1guess>ans): #猜太大
        counter+=1
        if(counter % 2 == 1): 
          max = c1guess
          c1guess = round((c1guess+3*min)/4)
        

        elif(counter % 2 == 0):
          max = c1guess
          c1guess = round((3*c1guess+min)/4)


      elif(c1guess<ans): #猜太小
          counter+=1
          if(counter % 2 ==1):
            min = c1guess
            c1guess =round((3*c1guess+max)/4)


          elif(counter % 2 == 0):
            min = c1guess
            c1guess =round((c1guess+max*3)/4)
           



      elif(c1guess == ans):
        print("我猜了" + str(counter)+"次")
        break

#瞎猜法
import random
import math


for i in range(0,101):
  ans = i
  c1guess = random.randint(0,100) 
  print("答案: "+str(ans))
  counter = 1
  max = 100
  min = 0
  guessed=[]
  while(True ): 
    if(c1guess<=max and c1guess>=min):
      if(c1guess>ans): #猜太大
        max = c1guess
        c1guess = random.randint(min, max)
        while c1guess in guessed:
          c1guess = random.randint(min, max)
        guessed.append(c1guess)
        counter+=1
      elif(c1guess<ans): #猜太小
        min = c1guess
        c1guess = random.randint(min, max)
        while c1guess in guessed:
          c1guess = random.randint(min, max)
        guessed.append(c1guess)
        counter+=1
      elif(c1guess == ans):
        print("我猜了" + str(counter)+"次")
        break

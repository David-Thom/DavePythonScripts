
import random
import math
 

def p(x):
    
    lets = []
    
    nums = []
    
    count = 0
    
    for i in range(len(x)):
        
        for j in range(len(x)):
            
            if(x[i] == x[j]):
            
                count = count + 1
                     
        if(not(x[i] in lets)):
            
            lets.append(x[i])
            
            count = math.factorial(count)
            
            nums.append(count)
            
        count = 0
        
    words = list(x)
    
    newCount = 1
    
    big = 1
    
    for k in range(len(nums)):
        
        big = big * nums[k]
        
    for l in range(len(x)):
        
        newCount = newCount * (len(x) - l) 
        
    rea = newCount//big
     
    me = []
     
    strf = ""
         
    be = False
     
    while(be == False ):
        
        random.shuffle(words)
        
        y = []
        
        for m in range(len(words)):
            
            y.append(words[m])
            
        if (not(y in me)):
            
            me.append(y)
             
            y = "".join(y)
             
            print(y)
            
        if(len(me) == rea):
             
            break


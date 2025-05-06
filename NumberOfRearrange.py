import random
 
def p(x):
     
    count = 1
     
    x = list(x)
     
    me = []
     
    strf = ""
     
    i = 0
     
    for k in range(len(x)):
        
        count = count * (len(x) - k) 
                 
    print(count)
         
         
    be = False 
     
    while(be == False ):
        
        random.shuffle(x)
        
        y = []
        
        for j in range(len(x)):
            
            y.append(x[j])
            
        if (not(y in me)):
            
            me.append(y)
             
            y = "".join(y)
             
            print(y)
            
        if(len(me) == count):
             
            break
        
p("hay")

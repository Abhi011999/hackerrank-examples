def jumpingOnClouds(c):
    jump = 0
    i = 0
    while i < len(c)-1:
        if c[i] == 0:
            i+=1
        jump+=1
        i+=1
            
    return jump
    
print(jumpingOnClouds([0,0,0,1,0,1,0]))
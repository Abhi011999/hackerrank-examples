def countingValleys(n , s):
    sl = 0
    v = 0
    for i in range(n):
        if s[i] == 'U':
            sl+=1
            if sl == 0:
                v+=1
        elif s[i] == 'D':
            sl-=1
    return v

print(countingValleys(26, ['U','U','U','D','D','U','U','D','D','D','D','D','D','U','U','U','D','D','U','U','U','U','D','D','D','U']))
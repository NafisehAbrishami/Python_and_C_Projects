min = None
max = None

while True :
    inp = int(input())
    if inp == -1 :
        break
    try:
        num = float(inp)
    except:
        print ("invalid input")
        continue

    if min is None or num < min :
        min = num
    if max is None or num > max:
        max = num
print( int(max))

    
    
    

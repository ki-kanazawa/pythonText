def capforword(caps):
    start =  forward = backward = 0
    intervals = []
    for i in range(1,len(caps)):
        if caps[start] != caps[i]:
            if caps[start] == 'F' or caps[start] =='B':
                intervals.append((start , i -1, caps[start]))
            if caps[start] == 'F':
                forward += 1
            elif caps[start] == 'B':
                backward += 1
            else:
                continue
            start = i
 
    if start !=0:
        if caps[start] == 'F' or caps[start] =='B':
            intervals.append((start , len(caps)-1 ,caps[start]))
        print(intervals)
        if caps[start] == 'F':
            forward +=1 
        elif caps[start] == 'B':
            backward += 1
            
        if forward < backward:
            flip = 'F'
        else :
            flip = 'B'
        for t in intervals :
            if t[2] == flip:
                if t[0]==t[1]:
                    print(f'people inposition  {t[0]}  flip your caps!')
                else:
                    print(f'people inposition  {t[0]} through {t[1]} flip your caps!')
                print(t)
    else:
        print('No caps!')
    
            
caps = ['F','F','B','B','B','F','B','B','B','F','F','B','F']

caps1 = []
 
caps2 = ['F','F','B','H','B','B','F','B','B','B','F','H','F','B','F']
capforword(caps2)
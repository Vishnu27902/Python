def minStepToReachTarget(KnightPos, TargetPos, N):
    x,y=TargetPos;
    sample=[(-1,-2),(-2,-1),(1,-2),(2,-1),(1,2),(2,1),(-1,2),(-2,1)]
    visited=set()
    reach=[(0,tuple(KnightPos))]
    while(len(reach)!=0):
        mov,cor=reach.pop(0)
        if(cor[0]==x and cor[1]==y):
            return mov
        for i in sample:
            nextcor=(cor[0]+i[0],cor[1]+i[1])
            if(0<=nextcor[0]<N and 0<=nextcor[1]<N):
                continue
            if nextcor not in visited:
                reach.append((mov+1,nextcor))
                visited.add(nextcor)
    return -1
print(minStepToReachTarget((4,5),(1,1),6))
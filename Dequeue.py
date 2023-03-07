from collections import deque

def minPossibleMoves(cor,size):
    initial=cor[:2]
    final=cor[2:]
    ls=[(1,-2),(-1,-2),(-2,-1),(2,-1),(-1,2),(1,2),(2,1),(-2,1)]
    seen=set()
    ordinates=[(0,initial)]
    while(len(ordinates)!=0):
        moves,corr=ordinates.pop(0)
        if(corr[0]==final[0] and corr[1]==final[1]):
            return moves
        for i in ls:
            nextcor=(corr[0]+i[0],corr[1]+i[1])
            if not(1<=nextcor[0]<=size and 1<=nextcor[1]<=size):
                continue
            if nextcor not in seen:
                ordinates.append((moves+1,nextcor))
                seen.add(nextcor)
    return -1
print(minPossibleMoves([2,8,3,4],13))
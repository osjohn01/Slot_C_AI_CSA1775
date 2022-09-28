def max(self):
    maxv=-2
    px=None
    py=None
    result=self.is_end()
    if result=='X':
        return(-1,0,0)
    elif result=='O':
        return(1,0,0)
    if result=='.':
        return(0,0,0)
    for i in range(3):
        for j in range(3):
            if self.current_state[i][i]==".":
                self.current_State[i][j]='O'
                (m, min_i, min_j)=self.min()
                if m>maxv:
                    maxv=m;
                    px=i;
                    py=j
                self.current_state[i][j]="."
        return(maxv, px, py)
max()

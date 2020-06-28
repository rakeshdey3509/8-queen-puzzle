def nqueens(n):
    Q = [None] * n
    dfs(0, Q)
    print ('ans =', Q)
    return Q


def dfs(r, Q):
    cand_pos, stk = gen_pos(r, Q), []
    stk += cand_pos
    while stk:
        pos = stk.pop()
        if is_soln(pos, Q):
            return True
        elif is_valid(pos, Q):
            emplaceQ(pos, Q)
            xplore = dfs(r + 1, Q)
            if xplore:
                return True
            else:
                removeQ(pos, Q)
    return False


def gen_pos(r, Q):
    n, res = len(Q), []
    for i in range(n):
        res += [(r, i)]
    return res


def emplaceQ(pos, Q):
    Q[pos[0]] = pos[1]


def removeQ(pos, Q):
    Q[pos[0]] = None


def is_valid(pos, Q):
    row, col = pos[0], pos[1]
    for i in range(row):
        if col == Q[i] or (row - col) == (i - Q[i]) or\
           (row + col) == (i + Q[i]):
                return False
    return True


def is_soln(pos, Q):
    row, n = pos[0], len(Q)
    if (row == n - 1) and is_valid(pos, Q):
        emplaceQ(pos, Q)
        return True
    return False
    
if __name__=='__main__':
    nqueens(8)

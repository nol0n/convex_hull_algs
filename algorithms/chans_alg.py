import algorithms.graham_scan as gs

# дальше ли точка1, чем точка2 от стартовой точки
def longer(start_pnt: list, pnt1:list, pnt2: list):
    x1, y1 = pnt1[0] - start_pnt[0], pnt1[1] - start_pnt[1]
    x2, y2 = pnt2[0] - start_pnt[0], pnt2[1] - start_pnt[1]
    if x1**2 + y1**2 > x2**2 + y2**2:
        return True
    else:
        return False

# от точки1 к точке2 поворот против часовой стрелки    
def ccw(start_pnt: list, pnt1:list, pnt2: list):
    x1, y1 = pnt1[0] - start_pnt[0], pnt1[1] - start_pnt[1]
    x2, y2 = pnt2[0] - start_pnt[0], pnt2[1] - start_pnt[1]
    if x1 * y2 - x2 * y1 > 0 or (x2 == 0 and y2 == 0):
        return True
    else:
        return False

# проверка лежат ли точки на одной прямой
def collinear(start_pnt: list, pnt1:list, pnt2: list):
    x1, y1 = pnt1[0] - start_pnt[0], pnt1[1] - start_pnt[1]
    x2, y2 = pnt2[0] - start_pnt[0], pnt2[1] - start_pnt[1]
    if x1 * y2 - x2 * y1 == 0:
        return True
    else:
        return False

# точка 1 расположена правее точки 2 или дальше,
# если они коллинеарны 
def pnt_greater(start_pnt: list, pnt1: list, pnt2: list):
    return ccw(start_pnt, pnt1, pnt2) or ( collinear(start_pnt, pnt1, pnt2) and longer(start_pnt, pnt1, pnt2) )

def find_tangent(pnt: list, hull: list):
    if len(hull) == 1:
        return hull[0]
    
    a, b = 0, len(hull)
    curr = (a + b) // 2 
    
    while not (
               ( 
                (pnt_greater(pnt, hull[curr % len(hull)], hull[(curr + 1) % len(hull)])) and 
                (pnt_greater(pnt, hull[curr % len(hull)], hull[(curr - 1)  % len(hull)])) 
               ) or
               (b - a == 1)
              ):
        # a + 1 > a
        if ccw(pnt, hull[(a + 1)  % len(hull)], hull[a % len(hull)]):
            # c > c + 1
            if ccw(pnt, hull[curr % len(hull)], hull[(curr + 1) % len(hull)]):
                b = curr
            # c + 1 > c
            else:
                # c > a
                if ccw(pnt, hull[curr % len(hull)], hull[a % len(hull)]):
                    a = curr
                # a > c
                else:
                    b = curr
        # a > a + 1
        else:
            # c + 1 > c
            if ccw(pnt, hull[(curr + 1) % len(hull)], hull[curr % len(hull)]):
                a = curr
            # c > c + 1
            else:
                # c > a
                if ccw(pnt, hull[curr % len(hull)], hull[a % len(hull)]):
                    b = curr
                # a > c
                else:
                    a = curr
        curr = (a + b) // 2  
        
    if b - a == 1:
        if pnt_greater(pnt, hull[a % len(hull)], hull[b % len(hull)]):
            return hull[a % len(hull)]
        else:
            return hull[b % len(hull)]
    
    return hull[curr % len(hull)]

def chans_alg(pnts: list, hull_size: int):
    hulls_count = (len(pnts) - 1) // hull_size + 1
    sub_hulls = [gs.graham_scan(pnts[i * hull_size : (i + 1) * hull_size]) for i in range(hulls_count)]
    
    ans = [min(pnts, key=lambda pnt: (pnt[0], pnt[1]))]
    for v in range(hull_size):
        new_pnt = None
        for h in range(hulls_count):
            tmp_pnt = find_tangent(ans[-1], sub_hulls[h])
            if new_pnt == None:
                new_pnt = tmp_pnt
            elif pnt_greater(ans[-1], tmp_pnt, new_pnt):
                new_pnt = tmp_pnt
        if (new_pnt == ans[0]):
            return ans
        if len(ans) > 1 and collinear(ans[-2], ans[-1], new_pnt) and longer(ans[-2], new_pnt, ans[-1]):
            ans[-1] = new_pnt
        else:
            ans.append(new_pnt)
    return None

def chans_hull(pnts: list):
    pnts_amount, hull_size_c, answer = len(pnts), 1, None
    while answer == None:
        answer = chans_alg(pnts, min((1 << (1 << hull_size_c)), pnts_amount))
        hull_size_c += 1
    return answer
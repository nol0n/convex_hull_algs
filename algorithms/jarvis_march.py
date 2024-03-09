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
    if x1 * y2 - x2 * y1 > 0:
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

def jarvis_march(pnts: list):
    ans = [min(pnts, key=lambda pnt: (pnt[0], pnt[1]))]

    while True:
        ans.append(None)
        for i in range(len(pnts)):
            if ans[-1] == None or ccw(ans[-2], pnts[i], ans[-1]) or (collinear(ans[-2], pnts[i], ans[-1]) and longer(ans[-2], pnts[i], ans[-1])):
                ans[-1] = pnts[i]
            
        if (ans[-1] == ans[0]):
            return ans[:-1]
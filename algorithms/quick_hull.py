# длинее ли вектор с конечной точкой1, чем вектор с конечной точкой2
# нахождение определитля составленного из двух векторов
def det(start_pnt: list, end_pnt: list, pnt: list):
    x, y = end_pnt[0] - start_pnt[0], end_pnt[1] - start_pnt[1]
    x1, y1 = pnt[0] - start_pnt[0], pnt[1] - start_pnt[1]
    return x * y1 - x1 * y

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

def find_points(pnts: list, start_pnt: list, end_pnt: list, ans: list):
    upper_pnts = [pnt for pnt in pnts if ccw(start_pnt, end_pnt, pnt)]
    
    index = ans.index(min([start_pnt, end_pnt], key=lambda pnt: pnt[0]))
    if (start_pnt[0] >= end_pnt[0]): index += 1
    
    if (len(upper_pnts) > 0):
        ans.insert(index, None)
        for pnt in upper_pnts:
            if (ans[index] == None or det(start_pnt, end_pnt, pnt) > det(start_pnt, end_pnt, ans[index]) or
            (det(start_pnt, end_pnt, pnt) == det(start_pnt, end_pnt, ans[index]) and longer(end_pnt, pnt, ans[index]))):
                ans[index] = pnt
        
        if ans[index] is not None:
            pnt = ans[index]
            find_points(upper_pnts, start_pnt, pnt, ans)
            find_points(upper_pnts, pnt, end_pnt, ans)

def quick_hull(pnts: list):
    min_pnt = min(pnts, key=lambda coord: (coord[0], coord[1])) 
    max_pnt = max(pnts, key=lambda coord: (coord[0], coord[1]))
    
    upper_part = [max_pnt, min_pnt]
    find_points(pnts, min_pnt, max_pnt, upper_part)
    
    lower_part = [min_pnt, max_pnt]
    find_points(pnts, max_pnt, min_pnt, lower_part)
    
    ans = [min_pnt] + lower_part[1:-1] + [max_pnt] + upper_part[1:-1]
    
    return ans
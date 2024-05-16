import math

def orientation(p,q,r):
    return (q[1]-p[1]) * (r[0]-q[0]) - (r[1]-q[1]) * (q[0]-p[0])

def sort_points_acc_polar_angle(pivot,points):
    points.sort(key = lambda p:(math.atan2(p[1]-pivot[1], p[0]-pivot[0]), (p[1]-pivot[1])**2+(p[0]-pivot[0])**2))

def graham_scan(points):

    if len(points) < 3:
        return points

    points.sort(key = lambda p:(p[1],p[0]))
    pivot = points.pop(0)

    sort_points_acc_polar_angle(pivot,points)
    print(points)

    hull = [pivot,points[0]]

    for point in points[1:]:
        while len(hull)>1 and orientation(hull[-2],hull[-1],point) >= 0:
            hull.pop()
        hull.append(point)

    if len(hull)>1 and hull[0]!=hull[-1]:
        hull.append(hull[0])
    
    return hull

points = [(-7,8), (-4,6), (2,6), (6,4), (8,6), (7,-2), (4,-6), (8,-7),(0,0), (3,-2),(6,-10),(0,-6),(-9,-5),(-8,-2),(-8,0),(-10,3),(-2,2),(-10,4)]

hull = graham_scan(points)
print(hull)
import math  # Import the math module for mathematical functions

def orientation(p, q, r):
    """
    Function to find the orientation of triplet (p, q, r).
    Returns:
    0 -> Collinear
    1 -> Clockwise
    2 -> Counterclockwise
    """
    # Calculate the orientation using the cross product formula
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or Counterclockwise

def graham_scan(points):
    # Sort points based on y coordinates
    points = sorted(points, key=lambda point: (point[1], point[0]))
    
    # Find the lowest point (point with the lowest y coordinate)
    lowest = points[0]
    
    # Sort the points by polar angle with respect to the lowest point
    points = sorted(points, key=lambda point: (math.atan2(point[1] - lowest[1], point[0] - lowest[0])))
    
    # Initialize the stack for the convex hull
    stack = []
    stack.append(points[0])  # Add the first point to the stack
    stack.append(points[1])  # Add the second point to the stack
    
    # Perform the Graham scan to construct the convex hull
    for i in range(2, len(points)):
        # Keep removing points from the stack while the orientation is not counterclockwise
        while len(stack) > 1 and orientation(stack[-2], stack[-1], points[i]) != 2:
            stack.pop()
        stack.append(points[i])  # Add the current point to the stack
    
    return stack  # Return the points on the convex hull in counterclockwise order

# Example usage:
points = [(0, 3), (1, 1), (2, 5), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
convex_hull = graham_scan(points)
print("Convex Hull:", convex_hull)

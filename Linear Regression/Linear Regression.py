# Linear Regression is when you have a group of points on a graph, and you find a line that approximately resembles that group of points.
# A good Linear Regression algorithm minimizes the error, or the distance from each point to the line. A line with the least error is the line that fits the data the best.
# We call this a line of best fit.
# We will use loops, lists, and arithmetic to create a function that will find a line of best fit when given a set of data.

# Line Function

def get_y(m, b, x):
  y = m*x + b
  return y


# Testing the Line Function

print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)


# calculate_error() Function

def calculate_error(m , b, point):
    x_point, y_point = point
    y = m*x_point + b
    distance = abs(y- y_point)
    return distance


# Testing the Calculate Error Function:

print(calculate_error(1, 0, (3, 3)))
print(calculate_error(1, 0, (3, 4)))
print(calculate_error(1, -1, (3, 3)))
print(calculate_error(-1, 1, (3, 3)))

# Sample Datapoints

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]


# As we try to fit a line to this data, we will need a function called calculate_all_error, which takes m and b that describe a line, and points, a set of data like the example above.
# Cumulative error (calculate_all_error) Function here:

def calculate_all_error(m,b,points):
    total_error = 0
    for point in points:
        error_of_point = calculate_error(m , b, point)
        total_error += error_of_point
    return total_error


#Testing the Cumulative error (calculate_all_error) Function:

datapoints1 = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints1))

datapoints2 = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints2))

datapoints3 = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints3))

datapoints4 = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints4))


# The Linear Regression:

possible_ms = [m * 0.1 for m in range(-100,100)]
possible_bs = [b * 0.1 for b in range(-200,200)]


smallest_error = float("inf")
best_m = 0
best_b = 0

for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m,b,datapoints)
        if error < smallest_error:
            smallest_error = error
            best_m = m
            best_b = b
            
print(best_m, best_b, smallest_error)


# Model Prediction
# best_m, best_b, x = 6

print(get_y(0.3,1.7,6))
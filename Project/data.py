#The data will consist of 
#
# [0]Distance from middle of pipes -> negative = above, positive = below -> y-axis
# [1]Length from pipes -> x-axis
# [2]Distance from bottom -> can imply distance from top with this -> y-axis
# [3]Input given 1 = jump, -1 = no jump
# if data[0] and data[3] > 0 || if data[0] and data[3] < 0 -> ignore this data
#
data = []

#
# each value will correspond to the values with same index in data[]
# -1 -> input resulted in a fail, 1 -> input resulted in passing
#
result = []
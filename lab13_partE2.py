from lab13_partC import mat_mul
 
R = [[0, -1],
     [1,  0]]            # 90-degree counter-clockwise rotation
P = [[0, 2, 1],
     [0, 0, 2]]          # each COLUMN is a vertex: (0,0), (2,0), (1,2)
t = (5, 5)
 
rotated = mat_mul(R, P)
moved = [[rotated[0][j] + t[0] for j in range(3)],
         [rotated[1][j] + t[1] for j in range(3)]]
print(rotated)
print(moved)

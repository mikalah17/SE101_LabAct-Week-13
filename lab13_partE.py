from lab13_partD import vec_add, vec_scale, magnitude
 
start = [2, 1]
m1, m2 = [3, 4], [-1, 2]
speed = 2.0
 
pos1 = vec_add(start, m1)
pos2 = vec_add(pos1, m2)
# TODO: displacement = pos2 - start   (hint: vec_add with vec_scale(-1, start))
# TODO: print the magnitude of the displacement
# TODO: path_length = magnitude(m1) + magnitude(m2);  print(path_length / speed)
print(pos1, pos2)

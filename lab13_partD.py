import math


def check_same_length(u, v):
    if len(u) != len(v):
        raise ValueError("Vectors must have the same number of components")


def vec_add(u, v):
    check_same_length(u, v)
    return [u[i] + v[i] for i in range(len(u))]


def vec_scale(k, v):
    return [k * x for x in v]


def magnitude(v):
    return math.sqrt(sum(x * x for x in v))


def dot(u, v):
    check_same_length(u, v)
    return sum(u[i] * v[i] for i in range(len(u)))


def angle_degrees(u, v):
    """Extension: angle between u and v, using cos(theta) = (u . v) / (|u| |v|)."""
    cos_theta = dot(u, v) / (magnitude(u) * magnitude(v))
    return math.degrees(math.acos(cos_theta))


if __name__ == "__main__":
    print(vec_add([3, -2], [-1, 5]))      # expect [2, 3]
    print(vec_scale(2, [3, -2]))          # expect [6, -4]
    print(magnitude([3, 4]))              # expect 5.0
    print(dot([4, 3], [-3, 4]))           # expect 0
    print(dot([2, -1, 4], [1, 3, -2]))    # expect -9
    try:
        vec_add([1, 2, 3], [4, 5])
    except ValueError as e:
        print("Caught:", e)

    # Extension: angle between (1, 0) and (1, 1)
    angle = angle_degrees([1, 0], [1, 1])
    print(angle)                          # about 45
    print(angle == 45)                    # False, because of floating-point error
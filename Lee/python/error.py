from lin_arg import bogan, lsm

try:
    result = bogan(3, [(1, 3), (2, -2), (3, -5), (4, 0)])
    print("계수:", result)
except ValueError as e:
    print("오류:", e)
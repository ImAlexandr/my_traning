from fake_math import divide as divide_fake
from true_math import divide as divide_true

print(divide_fake(12,4))
print(divide_true(14,8))

print(divide_fake(12,0))
print(divide_true(14,0))
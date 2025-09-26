import operations
result=operations.add(12,13)
print(result)
import operations as op
result=op.mul(12,13)
print(result)
from operations import *
print(add(1,2))
print(sub(18,5))
from operations import sub
print(sub(12,13))
from operations import mul as mult
print(mult(12,13))
from keyword import *
print(kwlist)




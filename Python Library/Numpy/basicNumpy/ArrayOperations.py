import numpy as np
# Array Operation
a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(3,4)
print(a2)
#Scaler Operation
print(a1 ** a2)

#relational operator
print(a2>5)
#vector operator
print(a1+a2) # as both of thenm as same shape so add them item wise
#similarly
print(a1**a2)
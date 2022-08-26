import numpy as np
import pandas as pd

array_unid = np.array([1,2,3,4,5])

array_bidim = np.array([[1,2,3],
                        [4,5,6]])

array_tri = np.array([[1,2,3],
                        [4,5,6],
                        [7,8,9],
                        [10,11,12]])


# print(array_unid.shape, array_unid.ndim, array_unid.dtype, array_unid.size, type(array_unid))
# print(array_bidim.shape, array_bidim.ndim, array_bidim.dtype, array_bidim.size, type(array_bidim))
# print(array_tri.shape, array_tri.ndim, array_tri.dtype, array_tri.size, type(array_tri))

datos = pd.DataFrame(array_bidim)
# print(datos)

unos = np.ones((4,3))
# print(unos)

ceros = np.zeros((4,3,3))
# print(ceros)

array_1 = np.arange(0,101,5)
# print(array_1)

array_ran = np.random.randint(0,10, (2,5))
# print(array_ran)

array_ran_float = np.random.random((2,3))
print(array_ran_float)
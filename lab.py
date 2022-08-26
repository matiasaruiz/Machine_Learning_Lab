import numpy as np
import pandas as pd

##### NUMPY TESTS #####

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
# print(array_ran_float)

##### PANDAS TESTS #####

numeros = pd.Series([1,2,3,5,67,35,235,62])
# print(numeros.mean)
# print(numeros.sum())


colores = pd.Series(['rojo', 'negro', 'verde'])
tipos_autos = pd.Series(['sedan', 'cupe', 'pickup'])

tabla_autos = pd.DataFrame({'Tipo de auto':tipos_autos,'Color':colores})
# print(tabla_autos      )

# tabla_autos.to_csv("prueba_export.csv")

venta_de_autos = pd.read_csv("ventas-autos.csv")
print(venta_de_autos.dtypes)
print("\n")
print(venta_de_autos.describe())
print("\n")
print(venta_de_autos.info)
print("\n")
print(venta_de_autos.columns)
print("\n")
print(venta_de_autos.head())
print("\n")
print(venta_de_autos.tail())
print("\n")
print(venta_de_autos.loc[2])
print("\n")
print(venta_de_autos.iloc[[2, 3, 5]])
print("\n")
print(venta_de_autos['Kilometraje'].mean())
print("\n")
print(venta_de_autos[venta_de_autos["Kilometraje"] > 10000])
print("\n")
print(pd.crosstab(venta_de_autos['Fabricante'],venta_de_autos['Puertas']))
print("\n")
print(venta_de_autos.groupby(["Fabricante"]).mean())
print("\n")
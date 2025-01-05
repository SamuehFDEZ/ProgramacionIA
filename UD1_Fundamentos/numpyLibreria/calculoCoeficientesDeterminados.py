import numpy as np
import sklearn.metrics as mt
y_real = np.array([3, -0.5, 2, 7, 4.2])
y_predicho = np.array([2.5, 0.0, 2, 8, 4.1])

def r2Score(yReal, yPredict):
    r2 = 1 - (np.sum((yReal - yPredict)** 2) / np.sum((yReal - np.mean(yReal))** 2)) 
    return r2

funcion = r2Score(yReal=y_real,yPredict=y_predicho)

print(f'R²: {funcion:.2f}')

funcionSk = mt.r2_score(y_real, y_predicho)

print(f'R² con libreria: {funcionSk:.2f}')
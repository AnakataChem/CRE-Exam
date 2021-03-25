import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import tikzplotlib

pA = 150e-3 #Pa
Ha = 3.89e-6 #mol/(L*Pa)

cBfl = 1e-3*np.array([25, 150, 600, 1200, 4000, 6000]) # mol/L
r = 1e-6*1/60*np.array([27220, 94970, 151550, 168250, 182310, 184520]) #mol/(L*s)

# Creating a 2 dimensional numpy array
data = np.array([cBfl, r])

# Creating pandas dataframe from numpy array
dataset = pd.DataFrame({'cB': data[0, :], 'r': data[1, :]})

X = dataset.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
Y = dataset.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows,

linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(1/X, 1/Y)         # perform linear regression
Y_pred = linear_regressor.predict(1/X) # make predictions

intercept = linear_regressor.intercept_[0]
slope = linear_regressor.coef_[0,0]

k = 1/(slope*Ha*pA)
aBetaL = 1/(intercept*Ha*pA)

plt.scatter(1/X, 1/Y, color='blue')
plt.plot(1/X, Y_pred, color='red', label='$y={:.2f}x+{:.2f}$'.format(slope,intercept))
plt.xlabel(r'$c_{B,fl}^{-1}\: / \: \si{\liter\per\mole}$')
plt.ylabel(r'$r^{-1}\: / \: \si{\liter\second\per\mole}$')
plt.legend(fontsize=12)
tikzplotlib.save("plot_rate.tex", axis_height="9cm", axis_width="11cm")
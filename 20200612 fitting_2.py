from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
f = np.loadtxt("Mn3.dat")
x=f[::,0]
y=f[::,1]
f2 = np.loadtxt("book1.dat")
S1=f2[::,0]
S2=f2[::,1]
S3=f2[::,2]
S12=f2[::,3]
ST=f2[::,4]
num1=len(x)
num2=len(S1)

J1=18
J2=-9
g=2.1
def test_func(x,J1,J2,g):
    k=0.695
    up=0
    down=0
    for i2 in range(num2):
        E1=(-J1*(ST[i2]*(ST[i2]+1)-S12[i2]*(S12[i2]+1)-S3[i2]*(S3[i2]+1)))-(J2*(S12[i2]*(S12[i2]+1)-S1[i2]*(S1[i2]+1)-S2[i2]*(S2[i2]+1)))
        E2=np.exp(-E1/(k*x))
        up=up+ST[i2]*(ST[i2]+1)*(2*ST[i2]+1)*E2
        down=down+(2*ST[i2]+1)*E2
    return 0.125*g**2*(up/down)
params, params_covariance = optimize.curve_fit(test_func, x, y,p0=[18, -9,2.1])
#popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))
print(params)
plt.scatter(x, y, label='Data')
plt.plot(x, test_func(x, params[0], params[1],params[2]),label='Fitted function',color='red')
plt.legend(loc='best')

plt.show()
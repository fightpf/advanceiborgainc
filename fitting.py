from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
f = np.loadtxt("20200502 fit reralxtion.txt")
x=f[::,0]
y=f[::,1]
fitx=1/x[::-2]
fity=1/np.exp(y[::-2])
k=0.695
def test_func(T,C,n,tau0,Ueff):
    return C*T**n+1/tau0*np.exp(-Ueff/k/T)
params, params_covariance = optimize.curve_fit(test_func,fitx ,fity ,maxfev=100000,p0=[0.01,3,0.0,0],bounds=([0.01,3,0.0,0],[0.09,10,0.000001,np.inf]))
ydata=np.log(1/test_func(1/x, params[0], params[1],params[2],params[3]))        #bestfit maxfev=100000,p0=[0.01,3,0.0,0],bounds=([0.01,3,0.0,0],[1,10,0.000001,np.inf]))
print(params)                                                       ##出現x0錯誤為起始值比Low bound低
plt.scatter(x, y, label='Data')                                             
plt.plot(x,ydata,label='Fitted function',color='red')
plt.legend(loc='best')
plt.show()


with open('fitting_result.txt','w') as fit_out:
    fit_out.write("C\tn\ttau0\tUeff\n")
    fit_out.write(str(params[0])+"\t"+str(params[1])+"\t"+str(params[2])+"\t"+str(params[3])+"\n")
    for i in range(len(ydata)):
        fit_out.write(str(x[i])+" "+str(ydata[i])+"\n")


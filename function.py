import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider
from matplotlib import cm
import matplotlib.animation as animation
from scipy.special import sph_harm, genlaguerre
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def Rp(Z, r, n, l, a1=1.0):
    # Z: 原子序数
    # r：距离原子核的距离
    # n：主量子数
    # l：角量子数
    # a1：第一玻尔半径
    tmp = 2 * Z * r / (n * a1)
    L = genlaguerre(n-l-1, 2*l+1)(tmp) # 调用scipy.special的genlaguerre计算
    return  np.exp(tmp/(-2)) * tmp**l * L
    # return - ((2 * Z / (n * a1))**3 * math.factorial(n - l - 1) / (2 * n * math.factorial(n + l)**3))**(1/2) * np.exp(tmp/(-2)) * tmp**l * L
def Yp(m, l, phi, theta):
    return sph_harm(m, l, phi, theta).real
def psi(Z, n, l, m, r, phi, theta):
    Rpro = Rp(Z, r, n, l, a1=1.0)
    Ypro = Yp(m, l, phi, theta)
    psi = Rpro * Ypro
    return psi

def Rp2(Z, r, n, l, a1=1.0):#为了进行杂化，轨道的相对大小必须正确，因此必须包含归一化系数。
    rho = 2 * Z * r / (n * a1)
    L = genlaguerre(n - l - 1, 2 * l + 1)(rho)
    
    prefactor = np.sqrt((2 * Z / (n * a1))**3 * math.factorial(n - l - 1) / (2 * n * math.factorial(n + l)))
    
    return prefactor * np.exp(-rho / 2) * (rho ** l) * L

def psi2(Z, n, l, m, r, phi, theta):
    # 获取径向部分
    R = Rp2(Z, r, n, l)
    # 获取角向部分 (这里为了简化，我们下面直接手动组合px, py, pz)
    Y = Yp(m, l, phi, theta) 
    return R * Y
#用于杂化轨道的归一化后的函数

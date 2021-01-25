# author:cycsir  time:2021/1/25
# 导入模块
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score


plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

# =================================================pip============================
# 指数函数拟合
# =============================================================================
def func(x, a, b ):
    return a*np.exp(-b * x)+1/150

# =============================================================================
# 幂指数函数拟合
# =============================================================================
def func2(x, a, b ):
    return x**a +b


# =============================================================================
# 多项式函数拟合
# =============================================================================
def func3(x, a, b, c ):
    return a*x**2+ b*x +c


if __name__ == '__main__':
    data = pd.read_excel('.\\微博数据\\工作簿1.xls')
    a = np.array(data['点赞数2'])
    b = np.array(data['点赞数3'])
    xdata = []
    ydata = []
    for i in range(0, 7):
        xdata.append(a[i])
        ydata.append(b[i])

    # 画出真实数据
    plt.plot(xdata, ydata, 'b-')

    # 指数函数拟合
    popt, pcov = curve_fit(func, xdata, ydata)  # popt数组中，三个值分别是待求参数a,b,c
    # 预测值
    y_pred = [func(i, popt[0], popt[1]) for i in xdata]
    # 画图
    plt.plot(xdata, y_pred, 'r--')
    print(popt)

    # 输出R方


    r2 = r2_score(ydata, y_pred)
    print('指数函数拟合R方为:', r2)

    # 幂指数函数拟合
    popt, pcov = curve_fit(func2, xdata, ydata)  # popt数组中，三个值分别是待求参数a,b,c
    y_pred2 = [func2(i, popt[0], popt[1]) for i in xdata]
    # 画图
    plt.plot(xdata, y_pred2, 'g--')
    print(popt)
    # 输出R方
    from sklearn.metrics import r2_score

    r2 = r2_score(ydata, y_pred2)
    print('幂指数函数拟合:', r2)

    # 多项式拟合
    popt, pcov = curve_fit(func3, xdata, ydata)  # popt数组中，三个值分别是待求参数a,b,c
    y_pred3 = [func3(i, popt[0], popt[1], popt[2]) for i in xdata]
    # 画图
    plt.plot(xdata, y_pred3, 'y-')
    print(popt)
    # 输出R方
    from sklearn.metrics import r2_score

    r2 = r2_score(ydata, y_pred3)
    print('多项式拟合R方为:', r2)

    # 添加图例
    plt.legend(['原始数据', '指数函数拟合', '幂指数函数拟合', '多项式拟合'])



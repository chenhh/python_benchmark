# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def plt_plot():
    x = np.linspace(0, 2, 100)

    plt.plot(x, x, label='linear')
    plt.plot(x, x**2, label='quadratic')
    plt.plot(x, x**3, label='cubic')

    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title("Simple Plot")
    plt.legend()
    plt.show()

def plt_axes():
    # 將 figure 例項化到 fig 的變數上，並設定寬與高（此處為預設值）
    fig = plt.figure(figsize=(6, 4))

    # 將 axe 新增到例項化後 2×2 的 figure 上，並指定第 1,2,3 個
    ax_1 = fig.add_subplot(2, 2, 1)
    ax_2 = fig.add_subplot(2, 2, 2)
    ax_3 = fig.add_subplot(2, 2, 3)
    plt.show()

def plt_subplot():
    plt.figure(figsize=(8, 6))

    plt.title("This is a title", fontsize=22, color='blue',
              fontstyle='italic', fontweight="heavy", family="cursive",
              bbox=dict(ec='pink', fc='w'), verticalalignment='bottom')

    plt.show()
if __name__ == '__main__':
    # plt_plot()
    # plt_axes()
    plt_subplot()

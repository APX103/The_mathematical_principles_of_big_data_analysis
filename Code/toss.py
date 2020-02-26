#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author: Jaylin

import numpy as np
from scipy.stats import norm


def simple_gen(num=10000, count=200):
    """
    样本生成
    0 为 T， 1 为 H
    返回'HHH'与'HHHH'的概率

    @param num:样本数，默认为10000
    @param count:掷硬币次数，默认为200
    """
    simples = []
    for k in range(num):
        simple_cell = [0, 0]  # 初始化样本单元，[三连出现的次数， 四连出现的次数]
        toss = np.random.choice([0, 1], count)  # 投掷200次
        # print(toss)  # Debug code
        for i in range(len(toss)):
            if i < len(toss) - 3:
                sum_4H = toss[i] + toss[i + 1] + toss[i + 2] + toss[i + 3]
                if sum_4H == 4:
                    simple_cell[1] = simple_cell[1] + 1
            if i < len(toss) - 2:
                sum_3H = toss[i] + toss[i + 1] + toss[i + 2]
                if sum_3H == 3:
                    simple_cell[0] = simple_cell[0] + 1
        # print(simple_cell)  # Debug code
        simples.append(simple_cell)
    _simples = [[], []]
    for i in simples:
        _simples[0].append(i[0] / 200)
        _simples[1].append(i[1] / 200)
        # _simples[0].append(i[0])
        # _simples[1].append(i[1])
    # simples为[[a, b], [a, b], [a, b]]
    # _simples为[[a, a, a], [b, b, b]]
    # 取你喜欢的一个return
    return _simples


def calculate(simple):
    """
    计算样本的平均值，方差，标准差，标准误差
    @param simple: 待求解的数字数组
    """
    mean = np.mean(simple)
    var = np.var(simple)
    std = np.std(simple)
    std_err = np.sqrt(std / len(simple))

    return [mean, var, std, std_err]


def DoC_3(_mean, _std):
    """
    计算3个'HHH'的置信值
    @param _mean: 样本空间标均值
    @param _std: 样本空间标准差
    """
    print((3 / 200 - _mean) / _std)
    return 1 - 2 * norm.cdf((3 / 200 - _mean) / _std)


def DoC_0(_mean, _std):
    """
    计算0个'HHHH'的置信值
    @param _mean: 样本空间标均值
    @param _std: 样本空间标准差
    """
    print((- _mean) / _std)
    return 1 - 2*norm.cdf((1 / 200 - _mean) / _std)


if __name__ == '__main__':
    simples = simple_gen(10000, 200)  # 样本空间
    [H_3, H_4] = [calculate(simples[0]), calculate(simples[1])]  # 得到计算结果
    # print(simples)
    # print(H_3, H_4)
    E1 = DoC_3(H_3[0], H_3[2])
    E2 = DoC_0(H_4[0], H_4[2])
    # print(H_3[0] / H_3[2])
    # print(H_4[0] / H_4[2])
    print(3/200)
    print("出现三连H的平均值：", H_3[0])
    print("出现三连H的标准差：", H_3[2])
    print("出现四连H的平均值：", H_4[0])
    print("出现四连H的标准差：", H_4[2])
    print("出现三次三连H的置信值是：", E1)
    print("出现一次四连H的置信值是：", E2)

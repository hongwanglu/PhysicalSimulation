# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Copyright (C) 2026 HongwangLu

import numpy as np
from scipy.integrate import odeint

def gravitational_lensing(x0, y0, rays=36, R0=2, speed=1, k=10):
    """
    计算光线在黑洞引力作用下的轨迹
    :param x0: 初始光线的 x 坐标
    :param y0: 初始光线的 y 坐标
    :param rays: 光线数量
    :param R0: 黑洞的事件视界半径
    :param speed: 光线的初始速度
    :param k: 引力常数
    :return: 光线的轨迹列表（每条光线是一个二维数组）
    """
    def Func(u, t, k):
        x, y, dx, dy = u
        r = np.sqrt(x**2 + y**2)  # 计算距离
        dXdt = -k * x * (1 / r**4)
        dYdt = -k * y * (1 / r**4)
        if r <= R0:  # 当 r < R0 时认为光线进入事件视界，停止计算
            return [0, 0, 0, 0]
        return [dx, dy, dXdt, dYdt]

    # 光线的初始速度角度分布
    trajectories = []
    for j in range(rays):
        alpha = float(j) * np.pi / (rays / 2)
        v0 = [speed * np.cos(alpha), speed * np.sin(alpha)]
        u0 = [x0, y0, v0[0], v0[1]]
        
        t = np.linspace(0, 100, 1000)  # 时间分割
        u = odeint(Func, u0, t, args=(k, ))
        
        # 保存光线的轨迹
        trajectories.append(u)
    
    return trajectories

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


class WaveFunction:
    def __init__(self, a=1, miu=9.10938356e-31, h=6.62607015e-34):
        self.a = a
        self.miu = miu
        self.h = h
        self.hbar = h / (2 * np.pi)
        self.main_quantum_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.coefficient = [1] + [0] * 9  # 默认第一能级为1，其余为0

    def psi(self, n, x, t):
        En = n**2 * self.h**2 / (8 * self.miu * self.a**2)
        return np.sqrt(2 / self.a) * np.sin(n * np.pi * x / self.a) * np.exp(-1j * En * t / self.hbar)

    def desirable_psi(self, x, t):
        wave_ideal = np.zeros_like(x, dtype=complex)
        for n, c in zip(self.main_quantum_number, self.coefficient):
            wave_ideal += c * self.psi(n, x, t)
        norm = np.sqrt(np.trapezoid(np.abs(wave_ideal) ** 2, x))
        return wave_ideal / norm if norm != 0 else wave_ideal

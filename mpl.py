import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# plt.plot([1, 2, 3 ,4])
# plt.ylabel('jakies liczby')
# plt.show

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
# plt.axis([0, 6, 8, 20])
# plt.show()
#
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
#
# plt.axis([0, 6, 8, 20])
# plt.show()
#
# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()
#
# x = np.linspace(0, 2, 100)
# plt.plot(x, x, label='Postać liniowa')
# plt.plot(x, x**2, label="Postać kwadratowa")
# plt.plot(x, x**3, label='Postać sześcienna')
# plt.xlabel('etykieta x')
# plt.ylabel('etykieta y')
# plt.title('nazwa wykresu')
# plt.legend()
# plt.show()
#
# x = np.arange(0, 10, 0.1)
# s = np.sin(x)
# plt.plot(x, s, label='sin(x)')
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
# plt.show()
#
# x1 = np.arange(0.0, 2.0, 0.02)
# x2 = np.arange(0.0, 2.0, 0.02)
# y1 = np.sin(2*np.pi*x1)
# y2 = np.cos(2*np.pi*x2)
#
# plt.subplot(2, 1, 1)
# plt.plot(x1,y1, '-')
# plt.title('Dwa podwykresy')
# plt.ylabel('sin(x)')
# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, '-')
# plt.ylabel('cos(x)')
# plt.show()
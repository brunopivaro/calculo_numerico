# O Épsilon de Máquina define a precisão. Dado x, o épsilon de máquina é o menor número tal que
# x + ϵ > x
# O valor de épsilon depende da variação de x

# Cancelamento Catastrófico
# Subtraindo números muito próximos, acabamos perdendo a precisão
# Exemplo: y = 1+x−1 / x

# Vamos variar x de 10^-1 até 10^-16

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10^-1, 10^-16)
y = 1 + x - 1

plt.plot(x, y)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

bits = np.random.randint(0,2,1000)
signal = 2*bits - 1

niose = (0.22)*np.random.randn(1000)
receive = signal + niose

rx_bits = (receive > 0 ).astype(int)

errors = np.sum(bits != rx_bits)
ber = errors / len(bits)
print("ber: " , ber)

plt.subplot(1 , 2 , 1)
plt.stem(bits[:20])
plt.title("Transmitted bits")

plt.subplot(1,2,2)
plt.plot(receive[:20])
plt.axhline(0 , color = "black")
plt.title("Received signl")

plt.show()
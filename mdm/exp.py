import matplotlib.pyplot as plt
file_size = [1.05, 2.79, 12.91, 27.56, 51.01]
transfer_time = [6.00, 14.36, 61.17, 130.25, 238.52]
plt.plot(file_size, transfer_time, marker='o')
plt.xlabel("File Size (MB)")
plt.ylabel("Transfer Time (s)")
plt.title("File Size vs Transfer Time")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
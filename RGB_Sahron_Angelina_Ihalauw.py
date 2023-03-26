# Import library untuk menampilkan warna
import matplotlib.pyplot as plt

# Membuat variabel R, G, dan B dengan nilai 0-255
R = 255
G = 0
B = 0

# Menghasilkan warna dengan kombinasi R, G, dan B
color = (R/255, G/255, B/255)

# Menampilkan warna menggunakan library Matplotlib
plt.bar([0], [1], color=color)
plt.show()


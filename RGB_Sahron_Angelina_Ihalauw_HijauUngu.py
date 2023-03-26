# Import library untuk menampilkan warna
import matplotlib.pyplot as plt

# Warna hijau dengan nilai R=0, G=255, B=0
R = 0
G = 255
B = 0
color = (R/255, G/255, B/255)
plt.bar([0], [1], color=color)

# Warna ungu dengan nilai R=128, G=0, B=128
R = 128
G = 0
B = 128
color = (R/255, G/255, B/255)
plt.bar([1], [1], color=color)

# Menampilkan grafik dengan dua bar berwarna hijau dan ungu
plt.show()

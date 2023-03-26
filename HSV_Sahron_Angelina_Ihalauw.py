# Import library untuk menampilkan warna
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# Membuat variabel Hue, Saturation, dan Value dengan nilai 0-360 dan 0-100
H = 120
S = 100
V = 100

# Menghasilkan warna dengan parameter HSV
color = colors.hsv_to_rgb([H/360, S/100, V/100])

# Menampilkan warna menggunakan library Matplotlib
plt.bar([0], [1], color=color)
plt.show()

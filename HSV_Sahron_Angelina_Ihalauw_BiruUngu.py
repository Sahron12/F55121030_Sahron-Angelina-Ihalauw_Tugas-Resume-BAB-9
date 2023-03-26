# Import library untuk menampilkan warna
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# Warna biru dengan nilai Hue=240, Saturation=100, dan Value=100
H = 240
S = 100
V = 100
color = colors.hsv_to_rgb([H/360, S/100, V/100])
plt.bar([0], [1], color=color)

# Warna ungu dengan nilai Hue=300, Saturation=100, dan Value=100
H = 300
S = 100
V = 100
color = colors.hsv_to_rgb([H/360, S/100, V/100])
plt.bar([1], [1], color=color)

# Menampilkan grafik dengan dua bar berwarna biru dan ungu
plt.show()

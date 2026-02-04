import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def draw_cube(ax, vertices, title, color='cyan'):
    # Menentukan sisi-sisi kubus berdasarkan indeks titik
    faces = [[vertices[0], vertices[1], vertices[2], vertices[3]],
             [vertices[4], vertices[5], vertices[6], vertices[7]], 
             [vertices[0], vertices[1], vertices[5], vertices[4]], 
             [vertices[2], vertices[3], vertices[7], vertices[6]], 
             [vertices[0], vertices[3], vertices[7], vertices[4]],
             [vertices[1], vertices[2], vertices[6], vertices[5]]]

    ax.add_collection3d(Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='r', alpha=.25))
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # Mengatur batas tampilan
    ax.set_xlim([-5, 10])
    ax.set_ylim([-5, 10])
    ax.set_zlim([-5, 10])

# 1. Definisi Titik Awal (Kubus 2x2x2)
vertices = np.array([[0, 0, 0], [2, 0, 0], [2, 2, 0], [0, 2, 0],
                     [0, 0, 2], [2, 0, 2], [2, 2, 2], [0, 2, 2]])

fig = plt.figure(figsize=(15, 5))

# --- Subplot 1: Objek Asli ---
ax1 = fig.add_subplot(131, projection='3d')
draw_cube(ax1, vertices, "Objek Asli")

# --- Subplot 2: Translasi (+3 di X dan Y) ---
T = np.array([3, 3, 0])
vertices_translated = vertices + T
ax2 = fig.add_subplot(132, projection='3d')
draw_cube(ax2, vertices_translated, "Translasi (X+3, Y+3)")

# --- Subplot 3: Rotasi 45 Derajat pada sumbu Z ---
theta = np.radians(45)
Rz = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta),  np.cos(theta), 0],
    [0,              0,             1]
])
vertices_rotated = np.dot(vertices_translated, Rz.T)
ax3 = fig.add_subplot(133, projection='3d')
draw_cube(ax3, vertices_rotated, "Rotasi 45° (setelah Translasi)")

plt.tight_layout()
plt.show()
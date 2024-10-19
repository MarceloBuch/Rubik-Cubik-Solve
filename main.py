import cv2
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_cube_face(colors):
    fig, ax = plt.subplots()

    square_size = 1

    for i in range(3):
        for j in range(3):
            x = j * square_size
            y = (2 - i) * square_size
            color = colors[i * 3 + j]
            
            square = patches.Rectangle((x, y), square_size, square_size, facecolor=color, edgecolor='black')
            ax.add_patch(square)

    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.show()

def get_domination_color(image, x, y, w, h):
    region = image[y:y+h, x:x+w]
    avg_color = np.mean(region, axis=(0,1))
    return avg_color

def map_color(color):
    pass
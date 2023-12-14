import colorsys
from colorthief import ColorThief
import matplotlib.pyplot as plt

# Initialize ColorThief with the image file "testing.jpg"
ct = ColorThief("testing.jpg")

# Get the dominant color
dominant_color = ct.get_color(quality=1)

# Display the dominant color using matplotlib
plt.imshow([[dominant_color]])
plt.show()

# Get the color palette with 5 colors
palette = ct.get_palette(color_count=5)

# Display the color palette using matplotlib
plt.imshow([[palette[i] for i in range(5)]])
plt.show()

# Print information about each color in the palette
for color in palette:
    print(color)
    print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")  # HEX representation
    print(colorsys.rgb_to_hsv(*color))  # HSV representation
    print(colorsys.rgb_to_hls(*color))  # HLS representation

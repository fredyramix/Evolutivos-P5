from PIL import Image
import numpy as np
i = Image.open("imagenes/3.jpg")
iar = np.asarray(i)

print iar
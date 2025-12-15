from microfilm import microplot
import matplotlib.pyplot as plt
import os
import numpy as np
import gc
import nd2

path_nd2 = "images" # where are the images?
os.makedirs("output", exist_ok=True) # where should the output go?
file_list = os.listdir(path_nd2) # get all filenames in the folder
for filename in file_list: # loop 
        image_path = path_nd2 + "/" + filename  
        image = nd2.imread(image_path) 
        print(image.shape)
        max_proj = np.max(image, axis = 0)
        microim = microplot.microshow(images=max_proj)
        save_path = os.path.join("output", f"{filename}_max.png")
        microim.savefig(save_path, dpi=600)
        # Clean up the main image after processing
        del image
        gc.collect()
print("Done")
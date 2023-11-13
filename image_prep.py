import h5py
import matplotlib.pyplot as plt
import numpy as np

def convert_h5_to_rgb_png(h5_in, h5_data, out):
    # Load data from the H5 file
    with h5py.File(h5_in, 'r') as h5_file:
        # Assuming the dataset is named 'data'
        data = h5_file[h5_data][:]
    
    # Normalize the data to the range [0, 1] for better visualization
    data_normalized = (data - np.min(data)) / (np.max(data) - np.min(data))

    # Create an RGB image by assigning channels
    red_channel = data_normalized[:, :, 0]  # Assuming the first channel is for the red channel
    green_channel = data_normalized[:, :, 1]  # Assuming the second channel is for the green channel
    blue_channel = data_normalized[:, :, 2]  # Assuming the third channel is for the blue channel
    
    # Stack the channels to form an RGB image
    rgb_image = np.stack([red_channel, green_channel, blue_channel], axis=-1)

    # Display the RGB image
    plt.imshow(rgb_image)
    plt.axis('off')  # Turn off axis labels and ticks

    # Save the RGB image as a PNG file
    plt.savefig(out, bbox_inches='tight', pad_inches=0)
    print(f"Conversion complete. RGB PNG saved at: {out}")
import h5py
import matplotlib.pyplot as plt
import numpy as np

def convert_h5_to_rgb(h5_in, h5_data, out):
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

    # Save the RGB image
    plt.savefig(out, bbox_inches='tight', pad_inches=0)
    print(f"Conversion complete. RGB saved at: {out}")


def convert_h5_to_bw(h5_in, h5_data, out):
    # Load data from the H5 file
    with h5py.File(h5_in, 'r') as h5_file:
        # Assuming the dataset is named 'data'
        data = h5_file[h5_data][:]
    
    if len(data.shape) == 2:
        # If the data is 2D, it's a grayscale image
        bw_image_normalized = (data - np.min(data)) / (np.max(data) - np.min(data))
    elif len(data.shape) == 3 and data.shape[2] == 14:
        # If the data is 3D with 14 channels, collapse them (e.g., by summing)
        bw_image = np.sum(data, axis=2)
        bw_image_normalized = (bw_image - np.min(bw_image)) / (np.max(bw_image) - np.min(bw_image))
    else:
        print("Unsupported data shape.")

    # Display the black and white image
    plt.imshow(bw_image_normalized, cmap='gray')  # 'gray' colormap represents black and white
    plt.axis('off')  # Turn off axis labels and ticks

    # Save the black and white image as a PNG file
    plt.savefig(out, bbox_inches='tight', pad_inches=0)
    print(f"Conversion complete. Black and white PNG saved at: {out}")

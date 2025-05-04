from PIL import Image
import numpy as np

def decode_lsb(image_path):
    """
    Decode a message from an LSB-encoded image (optimized version)
    """
    # Open image and convert to numpy array
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Get LSBs from all pixels at once (vectorized operation)
    lsb_array = (img_array & 1).flatten()
    
    # Convert LSBs to binary string
    binary_msg = ''.join(lsb_array.astype(str))
    
    # Find the delimiter efficiently
    delimiter = '11111110'
    delimiter_pos = binary_msg.find(delimiter)
    
    if delimiter_pos == -1:
        raise ValueError("No message delimiter found")
    
    # Extract only the message bits (before delimiter)
    message_bits = binary_msg[:delimiter_pos]
    
    # Convert 8-bit chunks to characters
    message = ''
    for i in range(0, len(message_bits), 8):
        byte = message_bits[i:i+8]
        if len(byte) < 8:
            break  # Incomplete byte at end
        message += chr(int(byte, 2))
    
    return message
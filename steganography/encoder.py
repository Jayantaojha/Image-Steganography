from PIL import Image
import numpy as np

def encode_lsb(image_path, message, output_path):
    """
    Encode a message into an image using LSB steganography
    """
    # Open the image and convert to numpy array
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Convert message to binary
    binary_msg = ''.join([format(ord(c), '08b') for c in message])
    binary_msg += '1111111111111110'  # Adding delimiter
    
    # Check if message fits in image
    max_bytes = img_array.size // 8
    if len(binary_msg) > max_bytes:
        raise ValueError("Message too large for the image")
    
    # Flatten the image array for easier manipulation
    flat = img_array.flatten()
    
    # Replace LSBs with message bits
    for i in range(len(binary_msg)):
        flat[i] = (flat[i] & 0xFE) | int(binary_msg[i])
    
    # Reshape the array back to original dimensions
    img_array_encoded = flat.reshape(img_array.shape)
    
    # Save the encoded image
    encoded_img = Image.fromarray(img_array_encoded)
    encoded_img.save(output_path)
    return encoded_img
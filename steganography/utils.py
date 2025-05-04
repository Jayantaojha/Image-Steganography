import numpy as np
from PIL import Image
import math

def calculate_psnr(original_path, encoded_path):
    """
    Calculate PSNR between original and encoded image
    """
    original = np.array(Image.open(original_path)).astype(float)
    encoded = np.array(Image.open(encoded_path)).astype(float)
    
    mse = np.mean((original - encoded) ** 2)
    if mse == 0:
        return float('inf')
    
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
    return psnr

def compare_images(original_path, encoded_path):
    """
    Compare original and encoded images
    """
    psnr = calculate_psnr(original_path, encoded_path)
    print(f"PSNR between images: {psnr:.2f} dB")
    
    original_size = Image.open(original_path).size
    encoded_size = Image.open(encoded_path).size
    print(f"Original size: {original_size}, Encoded size: {encoded_size}")
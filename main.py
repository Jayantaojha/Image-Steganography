import argparse
from steganography.encoder import encode_lsb
from steganography.decoder import decode_lsb
from steganography.crypto import encrypt_message, decrypt_message
from steganography.utils import compare_images

def main():
    parser = argparse.ArgumentParser(description="Image Steganography Tool")
    subparsers = parser.add_subparsers(dest='command', required=True)
    
    # Encode command
    encode_parser = subparsers.add_parser('encode', help='Encode a message in an image')
    encode_parser.add_argument('image', help='Input image path')
    encode_parser.add_argument('message', help='Message to hide')
    encode_parser.add_argument('output', help='Output image path')
    encode_parser.add_argument('--encrypt', action='store_true', help='Encrypt the message before hiding')
    
    # Decode command
    decode_parser = subparsers.add_parser('decode', help='Decode a message from an image')
    decode_parser.add_argument('image', help='Encoded image path')
    decode_parser.add_argument('--decrypt', action='store_true', help='Decrypt the extracted message')
    
    # Compare command
    compare_parser = subparsers.add_parser('compare', help='Compare original and encoded images')
    compare_parser.add_argument('original', help='Original image path')
    compare_parser.add_argument('encoded', help='Encoded image path')
    
    args = parser.parse_args()
    
    if args.command == 'encode':
        message = args.message
        if args.encrypt:
            message = encrypt_message(message)
            print("Message encrypted before encoding")
        
        encode_lsb(args.image, message, args.output)
        print(f"Message encoded in {args.output}")
    
    elif args.command == 'decode':
        message = decode_lsb(args.image)
        if args.decrypt:
            message = decrypt_message(message)
            print("Message decrypted after extraction")
        
        print(f"Extracted message: {message}")
        # Add these lines to save to file:
        with open('images/decoded_message.txt', 'w') as f:
            f.write(message)
    
    elif args.command == 'compare':
        compare_images(args.original, args.encoded)

if __name__ == "__main__":
    main()
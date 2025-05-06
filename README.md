# Image Steganography

Image Steganography is the practice of hiding secret messages within image files. This project uses LSB (Least Significant Bit) encoding to subtly embed text data into the pixels of a PNG image.

<br>

## ✨ Features

- Encrypt messages before embedding.
- Hide and extract messages from images using LSB technique.
- Compare original and modified images.
- CLI tool for ease of use and automation.
- Export extracted messages to text files.

<br>

## 🛠️ Technologies Used

- **Python 3.8+**
- **Pillow** - For image manipulation
- **Cryptography** - For AES encryption/decryption
- **argparse** - Command-line interface handling

<br>

---

### Install all dependencies using:
```bash
pip install -r requirements.txt
```

<br>

## How to Use

### 1. Encoding a Message
```bash
python main.py encode images/input.png "Secret Message" images/encoded.png
```

### 2. Decoding a Message
```bash
python main.py decode images/encoded.png
```

### 3. Comparing Images
```bash
python main.py compare images/input.png images/encoded.png
```

<br>

## Visual Results
### Before Encryption
![Original Image](images/input.png)

<br>

### After Encryption
![Encrypted Image](images/encoded.png)


<br> <br>

## Output
Extracted message is saved to:
```bash
images/decoded_message.txt
```


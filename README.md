# Decryption Tool

This repository contains a decryption utility that uses an RSA private key to decrypt data.

## Files

- `My first key` - RSA private key file
- `decrypt.py` - Python script for decrypting data

## Requirements

```bash
pip install -r requirements.txt
```

## Usage

### Decrypt from command line argument

```bash
python decrypt.py <base64_encrypted_data>
```

### Decrypt from file

```bash
python decrypt.py -f <encrypted_file>
```

### Use a custom key file

```bash
python decrypt.py <base64_encrypted_data> <key_file>
python decrypt.py -f <encrypted_file> <key_file>
```

## Example

To decrypt data that was encrypted with the corresponding public key:

```bash
python decrypt.py "YOUR_BASE64_ENCRYPTED_DATA_HERE"
```

The script will output the decrypted message.

## How it works

1. The script loads the RSA private key from the `My first key` file
2. It decodes the base64-encoded encrypted data
3. It decrypts the data using RSA OAEP padding with SHA-256
4. It outputs the decrypted plaintext message

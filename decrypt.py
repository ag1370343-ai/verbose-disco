#!/usr/bin/env python3
"""
Decryption utility using RSA private key.
This script can decrypt data that was encrypted with the corresponding public key.
"""

import sys
import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding


def load_private_key(key_file):
    """Load the RSA private key from a file."""
    with open(key_file, 'r') as f:
        content = f.read()
        # Extract the private key portion (the git URL is on the same line as BEGIN)
        # Find the BEGIN marker and extract from there
        begin_marker = '-----BEGIN PRIVATE KEY-----'
        end_marker = '-----END PRIVATE KEY-----'
        
        start = content.find(begin_marker)
        end = content.find(end_marker)
        
        if start == -1 or end == -1:
            raise ValueError("Could not find private key markers in file")
        
        # Extract just the key portion
        key_pem = content[start:end + len(end_marker)]
        
    private_key = serialization.load_pem_private_key(
        key_pem.encode(),
        password=None
    )
    return private_key


def decrypt_data(private_key, encrypted_data):
    """Decrypt data using the RSA private key."""
    # Decode from base64
    encrypted_bytes = base64.b64decode(encrypted_data)
    
    # Decrypt using OAEP padding
    decrypted = private_key.decrypt(
        encrypted_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode('utf-8')


def main():
    if len(sys.argv) < 2:
        print("Usage: python decrypt.py <encrypted_data_base64> [key_file]")
        print("   or: python decrypt.py -f <encrypted_file> [key_file]")
        print("\nDefault key file: 'My first key'")
        sys.exit(1)
    
    # Determine key file (use default or user-specified)
    key_file = 'My first key'
    
    # Check if key file is specified as the last argument
    if len(sys.argv) > 2 and sys.argv[1] != '-f':
        # Format: decrypt.py <encrypted_data> <key_file>
        key_file = sys.argv[2] if len(sys.argv) > 2 else key_file
    elif len(sys.argv) > 3 and sys.argv[1] == '-f':
        # Format: decrypt.py -f <encrypted_file> <key_file>
        key_file = sys.argv[3]
    
    # Load the private key
    try:
        private_key = load_private_key(key_file)
    except FileNotFoundError:
        print(f"Error: Key file '{key_file}' not found")
        sys.exit(1)
    except ValueError as e:
        print(f"Error loading key: {e}")
        sys.exit(1)
    
    # Get encrypted data
    if sys.argv[1] == '-f' and len(sys.argv) > 2:
        # Read from file
        with open(sys.argv[2], 'r') as f:
            encrypted_data = f.read().strip()
    else:
        # Read from command line argument
        encrypted_data = sys.argv[1]
    
    # Decrypt the data
    try:
        decrypted_message = decrypt_data(private_key, encrypted_data)
        print("Decrypted message:")
        print(decrypted_message)
    except FileNotFoundError:
        print(f"Error: Encrypted file not found")
        sys.exit(1)
    except (ValueError, base64.binascii.Error) as e:
        print(f"Error: Invalid base64 encoding in encrypted data")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Decryption failed. Possible causes: wrong key, corrupted data, or incorrect encryption format")
        print(f"Details: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

# Key Management Directory

This directory contains cryptographic keys and related materials.

## Directory Structure

- **`private/`** - Private keys (NOT committed to Git, protected by .gitignore)
- **`public/`** - Public keys (safe to commit)
- **`templates/`** - Example and template files

## Usage

### Storing Private Keys

All private keys should be stored in the `private/` directory:

```bash
# Move a private key to the secure location
mv my-key.pem private/
chmod 600 private/my-key.pem
```

### Storing Public Keys

Public keys can be safely stored in the `public/` directory:

```bash
# Extract public key from private key
openssl rsa -in private/my-key.pem -pubout -out public/my-key.pub
```

### Using Templates

The `templates/` directory contains example files showing the expected format:

```bash
# Copy a template to create a new key
cp templates/key-info.template private/my-key-info.txt
# Edit the file with your key information
```

## Security Notes

1. **Never commit private keys** - They are automatically excluded by .gitignore
2. **Set proper permissions** - Private keys should be readable only by the owner (chmod 600)
3. **Backup securely** - Keep encrypted backups of private keys in a secure location
4. **Rotate regularly** - Follow your organization's key rotation policy
5. **Document usage** - Keep track of where each key is used

## Key Information Format

When storing keys, maintain a parallel info file with metadata:

```
Key Name: my-first-key
Purpose: SSH authentication for repository access
Algorithm: RSA 4096-bit
Created: 2026-02-09
Expires: 2027-02-09
Used By: GitHub repository ag1370343-ai/verbose-disco
```

Store this info in `private/my-first-key-info.txt` (also gitignored).

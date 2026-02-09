# Public Keys Directory

This directory is for storing public cryptographic keys.

✅ **SAFE TO COMMIT**: Public keys can be safely committed to version control.

## Usage

Store your public keys here:
```bash
# Extract public key from private key
openssl rsa -in ../private/my-key.pem -pubout -out my-key.pub

# Or for SSH keys
ssh-keygen -y -f ../private/id_rsa > id_rsa.pub
```

### Public Keys Are Meant to Be Shared

Unlike private keys, public keys are designed to be shared freely:
- They can be distributed to anyone
- They're used to verify signatures or encrypt data for the private key holder
- They cannot be used to decrypt data or create signatures

### Examples

- SSH public keys for authentication
- GPG/PGP public keys for encryption
- TLS/SSL certificate public keys
- API verification keys

### Naming Convention

Match the public key filename with the corresponding private key:
- Private: `keys/private/github-deploy.pem`
- Public: `keys/public/github-deploy.pub`

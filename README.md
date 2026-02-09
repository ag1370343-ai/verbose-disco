# Verbose Disco - Secure Cryptographic Key Management

This repository demonstrates best practices for managing cryptographic keys and sensitive content.

## Overview

This project provides a secure framework for storing and accessing cryptographic content. **Private keys should NEVER be committed directly to version control.**

## Secure Key Management

### Best Practices

1. **Never commit private keys to Git**
   - Private keys should be stored locally or in secure key management systems
   - Use environment variables or secret management tools (e.g., HashiCorp Vault, AWS Secrets Manager)
   - Add key file patterns to `.gitignore`

2. **Use separate directories for different key types**
   - `keys/private/` - For private keys (gitignored)
   - `keys/public/` - For public keys (can be committed)
   - `keys/templates/` - For example/template files

3. **Encrypt sensitive data**
   - Use encryption for keys at rest
   - Consider using tools like `gpg`, `age`, or `openssl` for encryption
   - Use secure key derivation functions (KDFs)

### Directory Structure

```
verbose-disco/
├── .gitignore              # Prevents accidental commits of sensitive files
├── README.md               # This file
├── keys/
│   ├── README.md          # Key management instructions
│   ├── private/           # Private keys (gitignored)
│   ├── public/            # Public keys
│   └── templates/         # Example key templates
└── My first key           # Placeholder/reference file
```

## How to Store Your Keys

### Option 1: Local Storage (Development)

Store your private keys in the `keys/private/` directory. This directory is automatically excluded from Git via `.gitignore`.

```bash
# Move your private key to the secure location
mv "My first key" keys/private/my-first-key.pem
chmod 600 keys/private/my-first-key.pem
```

### Option 2: Environment Variables

```bash
# Store key content in environment variable
export MY_PRIVATE_KEY=$(cat keys/private/my-first-key.pem)
```

### Option 3: Secret Management System (Production)

For production environments, use a dedicated secret management system:
- **AWS Secrets Manager**
- **HashiCorp Vault**
- **Azure Key Vault**
- **Google Cloud Secret Manager**

## Viewing Your Keys Safely

To view keys without exposing them in version control:

```bash
# View key from private directory
cat keys/private/my-first-key.pem

# View key metadata without content
openssl rsa -in keys/private/my-first-key.pem -text -noout

# Extract public key from private key
openssl rsa -in keys/private/my-first-key.pem -pubout -out keys/public/my-first-key.pub
```

## Security Checklist

- [x] `.gitignore` configured to exclude private keys
- [x] README with security best practices
- [x] Directory structure for organized key management
- [x] Instructions for secure key storage
- [ ] Move any existing private keys to secure location
- [ ] Generate new keys if old ones were compromised
- [ ] Update any systems using the old key location

## Important Notes

⚠️ **If a private key has been committed to Git history, it should be considered compromised!**

If this happens:
1. Generate a new key pair immediately
2. Update all systems/services using the old key
3. Revoke the compromised key
4. Consider using `git-filter-repo` or BFG Repo-Cleaner to remove the key from Git history
5. Rotate all dependent secrets

## Resources

- [GitHub: Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
- [NIST Guidelines on Cryptographic Key Management](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)

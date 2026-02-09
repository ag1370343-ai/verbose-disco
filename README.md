# verbose-disco

This repository contains cryptographic key material.

## Files

### private_rsa_key.pem
- **Type**: RSA Private Key (PKCS#8 format)
- **Purpose**: Authentication/Encryption key
- **Security Level**: CRITICAL - Contains sensitive cryptographic material

## Security Warnings

⚠️ **IMPORTANT**: This repository contains a private RSA key that should be handled with extreme care:

1. **Never share this key** - Private keys should never be shared publicly or committed to public repositories
2. **Rotate immediately** - If this key has been exposed publicly, it should be considered compromised and rotated immediately
3. **Use proper permissions** - In production environments, private keys should have restricted file permissions (e.g., `chmod 600`)
4. **Use secure storage** - Consider using secret management systems (e.g., AWS Secrets Manager, HashiCorp Vault, Azure Key Vault) instead of storing keys in version control
5. **Remove from git history** - If this key was accidentally committed, consider using tools like `git-filter-repo` or BFG Repo-Cleaner to remove it from git history

## Best Practices for Key Management

- Store private keys in secure, encrypted storage systems
- Use environment variables or secret management services in applications
- Implement key rotation policies
- Use separate keys for development, staging, and production environments
- Never commit private keys to version control systems
- Use `.gitignore` to prevent accidental commits of sensitive files

## File Naming Conventions

This repository follows descriptive naming conventions:
- `private_rsa_key.pem` - Clearly indicates this is a private RSA key in PEM format
- Use descriptive names that indicate the file's purpose, type, and sensitivity level

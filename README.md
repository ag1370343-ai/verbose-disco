# verbose-disco

This repository contains cryptographic key material.

## Files

### private_rsa_key.pem
- **Type**: RSA Private Key (PKCS#8 format)
- **Purpose**: Authentication/Encryption key
- **Security Level**: CRITICAL - Contains sensitive cryptographic material

## Security Warnings

⚠️ **CRITICAL SECURITY ISSUE**: This repository contains a private RSA key that has been committed to version control.

**IMMEDIATE ACTIONS REQUIRED:**
1. **Consider this key COMPROMISED** - Any private key committed to version control should be considered exposed
2. **Rotate the key immediately** - Generate a new key pair and update all systems using this key
3. **Remove from repository** - Delete this file and remove it from git history using tools like `git-filter-repo` or BFG Repo-Cleaner
4. **Never commit private keys** - Private keys should never be stored in version control systems

**Best Practices Going Forward:**
1. **Use secure storage** - Use secret management systems (e.g., AWS Secrets Manager, HashiCorp Vault, Azure Key Vault)
2. **Use proper permissions** - In production environments, private keys should have restricted file permissions (e.g., `chmod 600`)
3. **Use .gitignore** - Prevent accidental commits by ignoring key files (*.pem, *.key, etc.)
4. **Audit regularly** - Regularly scan repositories for accidentally committed secrets

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

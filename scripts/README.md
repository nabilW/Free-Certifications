# Maintenance Scripts

This directory contains scripts to help maintain the Free Certifications repository.

## validate.py

A Python script that validates the repository content:

- **Checks for expired entries**: Identifies certifications that have passed their expiration date
- **Validates formatting**: Ensures consistent markdown table formatting
- **Reports issues**: Provides a summary of problems found

### Usage

```bash
python scripts/validate.py
```

Or make it executable and run directly:

```bash
chmod +x scripts/validate.py
./scripts/validate.py
```

### Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Future Scripts

Additional scripts may be added for:
- Link validation (checking if URLs are still valid)
- Automatic sorting of entries
- Expiration date parsing and validation
- Markdown linting

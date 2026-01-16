# Contributing to Free Certifications

Thank you for your interest in contributing to this repository! This document provides guidelines for adding and organizing free certification resources.

## How to Contribute

### Adding a New Certification

1. **Choose the Right Category**
   - **General**: Cloud platforms, programming, DevOps, AI/ML, networking, etc.
   - **Security**: Cybersecurity, ethical hacking, security certifications
   - **Databases**: Database-related certifications (MongoDB, Redis, SQL, etc.)
   - **Project Management**: Scrum, Agile, PMP, Six Sigma, etc.
   - **Marketing**: Digital marketing, social media, SEO, etc.
   - **Miscellaneous**: Other certifications that don't fit the above categories

2. **Format Your Entry**
   
   Use this format for the **General** section:
   ```markdown
   | Technology | Provider | Description | Link | Expiration |
   | --- | --- | --- | --- | --- |
   | [Technology Name] | [Provider Name] | [Brief description] | [Link](URL) | [Date or "Unlimited" or "Unknown"] |
   ```
   
   Use this format for **other sections** (Security, Databases, etc.):
   ```markdown
   | Provider | Description | Link | Expiration |
   | --- | --- | --- | --- |
   | [Provider Name] | [Brief description] | [Link](URL) | [Date or "Unlimited" or "Unknown"] |
   ```

3. **Entry Guidelines**
   - **Technology**: The technology or topic (e.g., "AWS", "Kubernetes", "Python")
   - **Provider**: The company or organization offering the certification
   - **Description**: A brief, clear description (1-2 sentences max)
   - **Link**: Direct link to the certification/course
   - **Expiration**: 
     - Use "Unlimited" if the offer has no expiration
     - Use "Unknown" if expiration is not specified
     - Use date format: "DD-MMM-YYYY" (e.g., "31-Dec-2024")
     - Use "Limited Time" if it's time-limited but no specific date is given

4. **Where to Add**
   - Add new entries at the **bottom** of the appropriate category table
   - Keep entries sorted by provider name (alphabetically) within each category
   - If a certification expires, move it to `Expired-Offers.md` (add to the top of that file)

### Updating Existing Entries

- If you find a broken link, please update it or mark it for removal
- If an expiration date changes, update it
- If a certification becomes expired, move it to `Expired-Offers.md`

### Code of Conduct

- Be respectful and professional
- Only add genuinely free certifications
- Verify links before adding
- Provide accurate information

## File Structure

```
.
├── README.md                    # Main file with all active certifications
├── Expired-Offers.md            # Archive of expired offers
├── CONTRIBUTING.md              # This file
├── ORGANIZATION.md              # Detailed organization guide
├── CODE_OF_CONDUCT.md           # Community code of conduct
├── CHANGELOG.md                 # Change history
└── scripts/                    # Maintenance scripts
    ├── validate.py             # Script to validate entries
    └── README.md               # Script documentation
```

## Quick Start

1. **Fork the repository**
2. **Run validation** (optional but recommended):
   ```bash
   python3 scripts/validate.py
   ```
3. **Make your changes** following the format guidelines
4. **Test your changes**:
   - Verify links work
   - Check formatting is consistent
   - Run validation script again
5. **Submit a pull request** using the PR template

## Pull Request Process

1. Fork the repository
2. Create a branch for your changes
3. Make your changes following the guidelines above
4. Test that your markdown renders correctly
5. Submit a pull request with a clear description

## Questions?

If you have questions, please open an issue for discussion.

Thank you for helping make free certifications more accessible! 🎓

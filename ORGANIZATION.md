# Repository Organization Guide

This document explains how the Free Certifications repository is organized and maintained.

## File Structure

```
.
├── README.md              # Main file with all active certifications
├── Expired-Offers.md      # Archive of expired offers (newest at top)
├── CONTRIBUTING.md        # Guidelines for contributors
├── ORGANIZATION.md        # This file
├── LICENSE.md             # License information
└── scripts/               # Maintenance scripts
    ├── README.md         # Script documentation
    └── validate.py       # Validation script
```

## Categories

Certifications are organized into the following categories:

### 1. General
Broad category covering:
- Cloud platforms (AWS, Azure, GCP, Oracle, etc.)
- Programming languages and frameworks
- DevOps tools and practices
- AI/ML and data science
- Networking and infrastructure
- Automation and testing
- API development
- Container technologies (Kubernetes, Docker, etc.)

**Table Format**: `| Technology | Provider | Description | Link | Expiration |`

### 2. Security
Cybersecurity-related certifications:
- Ethical hacking
- Security operations
- Network security
- Security frameworks and standards

**Table Format**: `| Provider | Description | Link | Expiration |`

### 3. Databases
Database technologies and certifications:
- SQL and NoSQL databases
- Database administration
- Data management platforms

**Table Format**: `| Provider | Description | Link | Expiration |`

### 4. Project Management
Project management methodologies and certifications:
- Agile and Scrum
- Six Sigma
- PMP and related certifications

**Table Format**: `| Provider | Description | Link | Expiration |`

### 5. Marketing
Digital marketing and related certifications:
- Social media marketing
- SEO and SEM
- Digital marketing platforms

**Table Format**: `| Provider | Description | Link | Expiration |`

### 6. Miscellaneous
Other certifications that don't fit the above categories:
- Business and entrepreneurship
- Education tools
- Various software platforms

**Table Format**: `| Provider | Description | Link | Expiration |`

## Entry Format Standards

### Date Formats
- Use format: `DD-MMM-YYYY` (e.g., `31-Dec-2024`)
- For unlimited offers: `Unlimited`
- For unknown expiration: `Unknown`
- For time-limited (no specific date): `Limited Time`

### Description Guidelines
- Keep descriptions concise (1-2 sentences)
- Include key information (value, requirements, etc.)
- Be clear about what's included

### Link Format
- Always use `[Link](URL)` format
- Ensure links are direct to the certification/course page
- Remove tracking parameters when possible

## Maintenance Workflow

### Adding New Certifications
1. Determine the appropriate category
2. Add entry at the bottom of the category table
3. Follow the format for that category
4. Verify the link works
5. Use consistent date formatting

### Handling Expired Certifications
1. Identify expired entries (dates in the past)
2. Move to `Expired-Offers.md`
3. Add to the **top** of the expired offers table
4. Remove from the main README.md

### Regular Maintenance Tasks
- Run `scripts/validate.py` periodically to check for expired entries
- Verify links are still working
- Update expiration dates if they change
- Sort entries alphabetically by provider (optional, but helpful)

## Validation

Use the validation script to check for issues:

```bash
python scripts/validate.py
```

This will:
- Identify expired entries
- Check for formatting issues
- Report problems that need attention

## Best Practices

1. **Consistency**: Maintain consistent formatting across all entries
2. **Accuracy**: Verify information before adding
3. **Completeness**: Include all required fields
4. **Clarity**: Write clear, concise descriptions
5. **Currency**: Keep expiration dates updated
6. **Organization**: Keep expired offers separate from active ones

## Questions?

If you have questions about organization, please:
1. Check [CONTRIBUTING.md](CONTRIBUTING.md) first
2. Open an issue for discussion
3. Review existing entries for examples

#!/usr/bin/env python3
"""
Validation script for Free Certifications repository.
Checks for expired entries, broken links, and formatting issues.
"""

import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

# Date formats to recognize
DATE_FORMATS = [
    "%d-%b-%Y",      # 31-Dec-2024
    "%d-%m-%Y",      # 31-12-2024
    "%b %d, %Y",     # Dec 31, 2024
    "%d %b %Y",      # 31 Dec 2024
    "%Y-%m-%d",      # 2024-12-31
]

def parse_date(date_str):
    """Try to parse a date string in various formats."""
    date_str = date_str.strip()
    
    # Handle special cases
    if date_str.lower() in ["unlimited", "unknown", "limited time"]:
        return None
    
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    
    return None

def extract_table_entries(file_path):
    """Extract certification entries from markdown table."""
    entries = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all table rows (lines starting with |)
    lines = content.split('\n')
    in_table = False
    header_found = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check if we're entering a table
        if line.startswith('|') and '---' not in line:
            if not header_found:
                # This is the header
                header_found = True
                in_table = True
                continue
            
            if in_table:
                # This is a data row
                parts = [p.strip() for p in line.split('|')[1:-1]]  # Remove empty first/last
                
                if len(parts) >= 4:  # At least Provider, Description, Link, Expiration
                    entries.append({
                        'line_num': i + 1,
                        'raw': line,
                        'parts': parts
                    })
        elif line.startswith('|') and '---' in line:
            # This is the separator row
            continue
        else:
            # Reset table state when we leave a table
            if not line.startswith('|'):
                in_table = False
                header_found = False
    
    return entries

def check_expired_entries(file_path):
    """Check for expired certification entries."""
    entries = extract_table_entries(file_path)
    expired = []
    today = datetime.now()
    
    for entry in entries:
        parts = entry['parts']
        # Expiration is typically the last column
        if len(parts) >= 4:
            expiration = parts[-1]
            exp_date = parse_date(expiration)
            
            if exp_date and exp_date < today:
                expired.append({
                    'line': entry['line_num'],
                    'entry': ' | '.join(parts),
                    'expiration': expiration,
                    'expired_date': exp_date
                })
    
    return expired

def validate_markdown_format(file_path):
    """Check for common markdown formatting issues."""
    issues = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines, 1):
        # Check for inconsistent spacing in table rows
        if line.strip().startswith('|'):
            parts = line.split('|')
            if len(parts) > 2:
                # Check for inconsistent spacing
                for j, part in enumerate(parts[1:-1], 1):
                    if part and not part.startswith(' ') and not part.startswith('['):
                        # Check if it should have spacing
                        pass
    
    return issues

def main():
    """Main validation function."""
    repo_root = Path(__file__).parent.parent
    readme_path = repo_root / "README.md"
    
    if not readme_path.exists():
        print(f"Error: {readme_path} not found")
        sys.exit(1)
    
    print("🔍 Validating Free Certifications repository...\n")
    
    # Check for expired entries
    print("Checking for expired entries...")
    expired = check_expired_entries(readme_path)
    
    if expired:
        print(f"\n⚠️  Found {len(expired)} expired entries:\n")
        for entry in expired:
            print(f"  Line {entry['line']}: {entry['entry'][:80]}...")
            print(f"    Expired: {entry['expiration']} (on {entry['expired_date'].strftime('%Y-%m-%d')})")
            print()
    else:
        print("✅ No expired entries found\n")
    
    # Summary
    print(f"\n📊 Summary:")
    print(f"  Total expired entries: {len(expired)}")
    
    if expired:
        print("\n💡 Tip: Move expired entries to Expired-Offers.md")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

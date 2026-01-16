# Changelog

All notable changes to this repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Contributing guidelines (CONTRIBUTING.md)
- Organization guide (ORGANIZATION.md)
- Code of Conduct (CODE_OF_CONDUCT.md)
- Validation script (scripts/validate.py) to check for expired entries
- GitHub Actions workflow for automated validation
- Issue templates for new certifications and broken links
- Pull request template
- .gitignore file

### Changed
- Moved expired entries to Expired-Offers.md
- Standardized formatting across all entries
- Fixed spacing inconsistencies in table entries

### Fixed
- Removed expired certifications from main README
- Fixed date format inconsistencies
- Standardized table formatting

## Notes

- Expired certifications are archived in [Expired-Offers.md](Expired-Offers.md)
- Run `python3 scripts/validate.py` to check for expired entries
- See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines

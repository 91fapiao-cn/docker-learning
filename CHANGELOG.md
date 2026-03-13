# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2026-03-13

### Added
- Minimal Python HTTP service with `/` and `/healthz`
- Dockerfile and local Docker build workflow
- Pytest-based tests
- GitHub Actions CI workflow with Docker smoke test
- Release workflow template for GHCR
- README, roadmap, template notes, release notes template

### Fixed
- CI import path issue for `app.py` on GitHub Actions
- Module startup side effect by guarding server boot with `if __name__ == '__main__'`

### Infrastructure
- Added `.gitignore` and `.gitattributes`
- Initialized git repository and published to GitHub

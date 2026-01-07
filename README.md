# API Bugfix – Data Consistency & Validation

This repository demonstrates a realistic Python REST API bugfix scenario.

## Problem
The API returned inconsistent response types and incorrect HTTP status codes
for certain input values.

Issues included:
- Missing input validation
- Inconsistent response formats
- Business logic mixed with request handling

## Approach
- Reproduced the bug with failing tests
- Introduced explicit validation
- Refactored business logic into a service layer
- Ensured deterministic API responses

## Result
- Consistent response structure
- Clear error handling
- Regression tests preventing recurrence

## Run tests
```bash
pip install -r requirements.txt
pytest

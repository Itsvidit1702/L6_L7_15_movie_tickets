# Lab 6 – Movie Tickets: Code and Branch Coverage Analysis

## Overview
This lab focuses on testing a Movie Tickets application using `pytest` and measuring code and branch coverage using `coverage.py`.

## Application Features
- **Ticket Pricing:** Calculates ticket prices based on seat type, age, show time, and weekend pricing.
- **Group Discounts:** Calculates discounts based on ticket quantity and student group eligibility.
- **Snack Combos:** Calculates snack combo prices based on size and coupon availability.
- **Input Validation:** Handles invalid seat types, show times, and ticket quantities.

## Testing and Coverage
The test cases cover valid inputs, boundary conditions, conditional branches, discounts, coupons, and error handling.

### Tools Used
- Python
- pytest
- coverage.py

### Run the Tests
```bash
python -m pytest
```

### Measure Code Coverage
```bash
python -m coverage run -m pytest CodeCoverageTest_xxxx_application.py
python -m coverage report -m
```

### Measure Branch Coverage
```bash
python -m coverage erase
python -m coverage run --branch -m pytest BranchCoverageTest_xxxx_application.py
python -m coverage report -m
```

## Coverage Target
The lab requirement is at least **90% code coverage and 90% branch coverage**. Refer to the actual coverage reports for the achieved percentages.

## Repository Contents
- `movie_tickets.py` – Application source code
- `test_movie_tickets.py` – Original example tests
- `CodeCoverageTest_xxxx_application.py` – Code coverage test cases
- `BranchCoverageTest_xxxx_application.py` – Branch coverage test cases
- `README.md` – Project documentation

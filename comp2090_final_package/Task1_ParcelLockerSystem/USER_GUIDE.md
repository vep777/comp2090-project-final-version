# Task 1 User Guide

## Requirements
- Python 3.10 or above
- No extra package is required

## How to run
Open a terminal in this folder and enter:

```bash
python main.py
```

## Menu functions
1. Add customer
2. Register parcel and assign locker
3. Pick up parcel
4. Search parcel
5. Show locker status
6. Save data to JSON file
7. Load saved data from JSON file
8. Exit the program

## Notes
- Tracking IDs should begin with `P`, for example `P1005`.
- Phone numbers should contain at least 8 digits.
- Parcel size is decided by weight in this beginner version:
  - up to 1.0 kg -> Small
  - above 1.0 kg and up to 3.0 kg -> Medium
  - above 3.0 kg -> Large
- The program loads one demo parcel when it starts.

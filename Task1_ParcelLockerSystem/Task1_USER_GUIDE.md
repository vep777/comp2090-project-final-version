# User Guide - Task 1 Campus Parcel Locker Management System

## 1. Requirements
- Python 3 installed on your computer
- All Task 1 files stored in the same folder

## 2. Files Needed
Make sure the following files are in the same folder:
- `main.py`
- `system.py`
- `parcel.py`
- `customer.py`
- `locker.py`
- `utils.py`

## 3. How to Run
Open a terminal in the Task 1 folder and run:

```bash
python main.py
```

## 4. Main Menu Functions
After running the program, the menu will display the following options:
1. Add customer
2. Register parcel and assign locker
3. Pick up parcel
4. Search parcel
5. Show locker status
6. Save data
7. Load saved data
8. Exit

## 5. How to Use the Program

### Add customer
Enter:
- customer name
- student ID
- phone number

### Register parcel and assign locker
Enter:
- parcel type (`standard`, `express`, or `fragile`)
- tracking ID
- sender
- recipient
- weight

The system will assign the parcel to a suitable locker and generate a pickup code.

### Pick up parcel
Enter:
- tracking ID
- pickup code
- days stored

The system will verify the parcel and calculate the total fee.

### Search parcel
Enter the tracking ID to view:
- parcel type
- recipient
- status
- locker ID
- pickup code

### Show locker status
Display all lockers and whether they are available or occupied.

### Save data
Save the current system data into `locker_data.json`.

### Load saved data
Load the saved information from `locker_data.json`.

## 6. Navigation During Input
For multi-step input:
- enter `B` to return to the previous step
- enter `M` to return to the main menu

## 7. Notes
- Phone numbers should contain at least 8 digits
- Tracking IDs must start with `P`
- If no suitable locker is available, the program will show an error message

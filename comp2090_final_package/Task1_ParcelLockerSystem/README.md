# Task 1 - Campus Parcel Locker Management System

## Project overview
This project is a beginner-level Python application for managing a campus parcel locker service. The system allows staff to register customers, record incoming parcels, assign parcels to lockers, search parcel records, and release parcels when students pick them up.

## Why this topic
A smart parcel locker system is a realistic campus problem. It is also suitable for demonstrating the Object-Oriented Programming concepts taught in COMP2090SEF.

## OOP concepts demonstrated
- **Encapsulation**: data is stored inside objects such as `Customer`, `Locker`, and `Parcel`.
- **Inheritance**: `StandardParcel`, `ExpressParcel`, and `FragileParcel` inherit from the abstract class `Parcel`.
- **Polymorphism**: each parcel type implements `calculate_fee()` differently.
- **Abstraction**: `Parcel` is an abstract base class.
- **Modular programming**: the project is divided into multiple Python files.
- **Class attributes**: `Parcel.total_parcels`, `Customer.total_customers`, and `Locker.total_lockers`.
- **Class method**: `LockerSystem.create_demo_system()` and `LockerSystem.load_data()`.
- **Static method**: helper functions inside `SystemUtils`.
- **Magic methods**: `__str__`, `__eq__`, and `__add__`.

## Main functions
1. Add customer
2. Register parcel
3. Automatically assign parcel to a suitable locker
4. Search parcel by tracking ID
5. Pick up parcel with pickup code
6. Calculate storage fee
7. Save system data
8. Load saved system data
9. Show locker status

## File structure
- `customer.py` - customer class
- `parcel.py` - abstract parcel class and child classes
- `locker.py` - locker class
- `system.py` - main controller class
- `utils.py` - utility helper methods and fee record class
- `main.py` - menu-based program entry point
- `USER_GUIDE.md` - instructions for running the program
- `test_cases.txt` - simple test list for demonstration

## How to run
```bash
python main.py
```

## Final version improvements from pre-submission
- Added parcel search function
- Added JSON save/load function
- Added simple locker size matching based on parcel weight
- Improved comments, structure, and user guide

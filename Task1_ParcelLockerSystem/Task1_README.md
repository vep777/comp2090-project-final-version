# Task 1 - Campus Parcel Locker Management System

## Overview
This task is a Python-based application for managing a campus smart parcel locker service. It is designed to simulate the basic operations of parcel handling in a simple and structured way.

The system allows staff to:
- add customers
- register parcels
- assign parcels to lockers
- search for stored parcels
- release parcels during pickup
- save and load system data

## OOP Design
This task applies object-oriented programming concepts through multiple classes and modules.

Examples of OOP usage:
- `Parcel` is an abstract base class
- `StandardParcel`, `ExpressParcel`, and `FragileParcel` inherit from `Parcel`
- different parcel types use different fee calculation methods
- `LockerSystem` acts as the main controller of the program
- utility functions are separated into `utils.py`

## File Structure
- `main.py` - program entry point and menu interface
- `system.py` - main system controller
- `parcel.py` - parcel classes
- `customer.py` - customer class
- `locker.py` - locker class
- `utils.py` - helper functions and fee record class

## Main Functions
- Add customer
- Register parcel and assign locker
- Pick up parcel
- Search parcel
- Show locker status
- Save data to JSON
- Load data from JSON

## Notes
- Tracking IDs must start with `P`
- Data is saved in `locker_data.json`
- During multi-step input, users can enter `B` to go back or `M` to return to the main menu

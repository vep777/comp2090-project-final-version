# Task 1 - Campus Parcel Locker Management System

## Overview
This is the final version of the Task 1 project for COMP2090SEF. The system simulates a campus smart parcel locker service. Staff can add customers, register parcels, assign parcels to lockers, search for parcels, release parcels during pickup, and save or load system data.

## Main functions
- Add customer
- Register parcel and assign locker
- Pick up parcel
- Search parcel
- Show locker status
- Save data to JSON
- Load saved data from JSON

## Final improvements
- Added parcel search
- Added save/load data
- Added locker size matching
- Kept `B` for back and `M` for main menu during input

## User Guide
1. Open a terminal in this folder.
2. Run the program with:

```bash
python main.py
```

3. Follow the on-screen menu.
4. During multi-step input:
   - Enter `B` to go back to the previous step
   - Enter `M` to return to the main menu

## Notes
- Tracking IDs must start with `P`.
- Saved data will be stored in `locker_data.json`.

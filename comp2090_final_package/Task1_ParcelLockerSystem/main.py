from customer import Customer
from system import LockerSystem
from utils import SystemUtils


DATA_FILE = "locker_data.json"


def seed_demo_data(system: LockerSystem) -> None:
    parcel = system.register_parcel("express", "P1001", "Campus Bookstore", "Alex Chan", 1.2)
    message = system.assign_to_first_available_locker(parcel)
    print("Demo parcel loaded:")
    print(message)
    print()


def show_menu() -> None:
    print("=" * 55)
    print("COMP2090 Smart Locker Hub")
    print("1. Add customer")
    print("2. Register parcel and assign locker")
    print("3. Pick up parcel")
    print("4. Search parcel")
    print("5. Show locker status")
    print("6. Save data")
    print("7. Load saved data")
    print("8. Exit")


def create_system() -> LockerSystem:
    system = LockerSystem.create_demo_system()
    seed_demo_data(system)
    return system


def menu() -> None:
    system = create_system()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                name = input("Customer name: ")
                student_id = input("Student ID: ")
                phone = input("Phone number: ")

                if not SystemUtils.validate_phone(phone):
                    raise ValueError("Phone number is invalid.")

                system.add_customer(Customer(name, student_id, phone))
                print("Customer added successfully.")

            elif choice == "2":
                parcel_type = input("Parcel type (standard/express/fragile): ")
                tracking_id = input("Tracking ID: ")
                sender = input("Sender: ")
                recipient = input("Recipient: ")
                weight = float(input("Weight (kg): "))

                parcel = system.register_parcel(parcel_type, tracking_id, sender, recipient, weight)
                print(system.assign_to_first_available_locker(parcel))

            elif choice == "3":
                tracking_id = input("Tracking ID: ")
                code = input("Pickup code: ")
                days = int(input("Days stored: "))
                print(system.pickup_parcel(tracking_id, code, days))

            elif choice == "4":
                tracking_id = input("Tracking ID: ")
                print(system.search_parcel(tracking_id))

            elif choice == "5":
                print(system.show_locker_status())

            elif choice == "6":
                print(system.save_data(DATA_FILE))

            elif choice == "7":
                system = LockerSystem.load_data(DATA_FILE)
                print("Saved data loaded successfully.")

            elif choice == "8":
                print("Exiting system. Goodbye.")
                break

            else:
                print("Invalid option. Please choose again.")

        except FileNotFoundError:
            print("No saved file was found yet.")
        except ValueError as error:
            print(f"Error: {error}")

        print()


if __name__ == "__main__":
    menu()

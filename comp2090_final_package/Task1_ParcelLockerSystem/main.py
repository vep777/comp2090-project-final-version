from customer import Customer
from system import LockerSystem
from utils import SystemUtils

BACK = "B"
MAIN = "M"


def seed_demo_data(system: LockerSystem) -> None:
    parcel = system.register_parcel("express", "P1001", "Bookstore", "Alex Chan", 1.2)
    message = system.assign_to_first_available_locker(parcel)
    print("Demo parcel loaded:")
    print(message)
    print()


def show_navigation_tip() -> None:
    print(f"Enter {BACK} to go back to the previous step.")
    print(f"Enter {MAIN} to return to the main menu.")


def get_step_input(prompt: str) -> str:
    return input(prompt).strip()


def add_customer_menu(system: LockerSystem) -> None:
    print("\n--- Add Customer ---")
    show_navigation_tip()

    steps = ["name", "student_id", "phone"]
    data = {"name": "", "student_id": "", "phone": ""}
    index = 0

    while index < len(steps):
        current = steps[index]

        if current == "name":
            value = get_step_input("Customer name: ")
        elif current == "student_id":
            value = get_step_input("Student ID: ")
        else:
            value = get_step_input("Phone number: ")

        upper_value = value.upper()

        if upper_value == MAIN:
            print("Returned to main menu.")
            return

        if upper_value == BACK:
            if index == 0:
                print("Already at the first step.")
            else:
                index -= 1
            continue

        if value == "":
            print("Input cannot be empty.")
            continue

        if current == "phone" and not SystemUtils.validate_phone(value):
            print("Phone number is invalid.")
            continue

        data[current] = value
        index += 1

    system.add_customer(Customer(data["name"], data["student_id"], data["phone"]))
    print("Customer added successfully.")


def register_parcel_menu(system: LockerSystem) -> None:
    print("\n--- Register Parcel and Assign Locker ---")
    show_navigation_tip()

    steps = ["parcel_type", "tracking_id", "sender", "recipient", "weight"]
    data = {
        "parcel_type": "",
        "tracking_id": "",
        "sender": "",
        "recipient": "",
        "weight": ""
    }
    index = 0

    while index < len(steps):
        current = steps[index]

        if current == "parcel_type":
            value = get_step_input("Parcel type (standard/express/fragile): ")
        elif current == "tracking_id":
            value = get_step_input("Tracking ID: ")
        elif current == "sender":
            value = get_step_input("Sender: ")
        elif current == "recipient":
            value = get_step_input("Recipient: ")
        else:
            value = get_step_input("Weight (kg): ")

        upper_value = value.upper()

        if upper_value == MAIN:
            print("Returned to main menu.")
            return

        if upper_value == BACK:
            if index == 0:
                print("Already at the first step.")
            else:
                index -= 1
            continue

        if value == "":
            print("Input cannot be empty.")
            continue

        if current == "weight":
            try:
                weight = float(value)
                if weight <= 0:
                    print("Weight must be greater than 0.")
                    continue
                data[current] = weight
            except ValueError:
                print("Please enter a valid number for weight.")
                continue
        else:
            data[current] = value

        index += 1

    parcel = system.register_parcel(
        data["parcel_type"],
        data["tracking_id"],
        data["sender"],
        data["recipient"],
        data["weight"]
    )
    print(system.assign_to_first_available_locker(parcel))


def pickup_parcel_menu(system: LockerSystem) -> None:
    print("\n--- Pick Up Parcel ---")
    show_navigation_tip()

    steps = ["tracking_id", "code", "days"]
    data = {"tracking_id": "", "code": "", "days": ""}
    index = 0

    while index < len(steps):
        current = steps[index]

        if current == "tracking_id":
            value = get_step_input("Tracking ID: ")
        elif current == "code":
            value = get_step_input("Pickup code: ")
        else:
            value = get_step_input("Days stored: ")

        upper_value = value.upper()

        if upper_value == MAIN:
            print("Returned to main menu.")
            return

        if upper_value == BACK:
            if index == 0:
                print("Already at the first step.")
            else:
                index -= 1
            continue

        if value == "":
            print("Input cannot be empty.")
            continue

        if current == "days":
            try:
                days = int(value)
                if days < 0:
                    print("Days stored cannot be negative.")
                    continue
                data[current] = days
            except ValueError:
                print("Please enter a valid integer for days stored.")
                continue
        else:
            data[current] = value

        index += 1

    print(system.pickup_parcel(data["tracking_id"], data["code"], data["days"]))


def menu() -> None:
    system = LockerSystem.create_demo_system()
    seed_demo_data(system)

    while True:
        print("=" * 50)
        print(system.campus_name)
        print("1. Add customer")
        print("2. Register parcel and assign locker")
        print("3. Pick up parcel")
        print("4. Show locker status")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                add_customer_menu(system)

            elif choice == "2":
                register_parcel_menu(system)

            elif choice == "3":
                pickup_parcel_menu(system)

            elif choice == "4":
                print(system.show_locker_status())

            elif choice == "5":
                print("Exiting system. Goodbye.")
                break

            else:
                print("Invalid option. Please choose again.")

        except ValueError as error:
            print(f"Error: {error}")

        print()


if __name__ == "__main__":
    menu()

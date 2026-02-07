import time

# User inputs number of trains
n = int(input("Enter number of trains to simulate: "))

trains = []
platforms = []

# Collect train names and platform numbers from user
for i in range(n):
    name = input(f"Enter name of train {i+1}: ")
    platform = int(input(f"Enter platform number for {name}: "))
    trains.append(name)
    platforms.append(platform)

while True:
    print("\n--- Train Station Simulation ---")
    print("1. Start Simulation")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        for i in range(len(trains)):
            print(f"\nTrain '{trains[i]}' arriving at Platform {platforms[i]}")

            # Arrival countdown
            for sec in range(5, 0, -1):
                print(f"Arrival in {sec} seconds...", end="\r")
                time.sleep(1)

            print(f"Train '{trains[i]}' has arrived at Platform {platforms[i]}")

            # Departure countdown
            for sec in range(3, 0, -1):
                print(f"Departing in {sec} seconds...", end="\r")
                time.sleep(1)

            print(f"Train '{trains[i]}' has departed from Platform {platforms[i]}")

        print("\n--- Cycle Completed ---\n")

    elif choice == 2:
        print("Thank you for using Train Station Simulator 🚉")
        break

    else:
        print("Invalid choice, please try again.")

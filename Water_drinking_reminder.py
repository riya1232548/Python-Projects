
import time
from plyer import notification


def water_reminder(interval_minutes):
    interval_seconds = interval_minutes * 60

    print("=" * 40)
    print("       💧 WATER DRINKING REMINDER")
    print("=" * 40)
    print(f"Your reminder is set for every {interval_minutes} minutes.")
    print("Stay hydrated and take care of yourself!")
    print("Press Ctrl + C to stop the reminder.\n")

    reminder_count = 0

    try:
        while True:
            time.sleep(interval_seconds)

            reminder_count += 1

            print(f"Reminder #{reminder_count}: Time to drink water!")

            notification.notify(
                title="💧 Time to Drink Water!",
                message="Take a short break and drink some water.",
                timeout=10
            )

    except KeyboardInterrupt:
        print("\nWater reminder stopped. Stay hydrated!")


def main():
    print("Welcome to your Water Reminder App!")

    try:
        interval = int(
            input("How often should I remind you? Enter minutes: ")
        )

        if interval <= 0:
            print("Please enter a number greater than zero.")
            return

        water_reminder(interval)

    except ValueError:
        print("Invalid input! Please enter a whole number, such as 5 or 30.")


if __name__ == "__main__":
    main()

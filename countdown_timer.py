import time

def countdown(seconds):
    while seconds > 0:
        minutes, remaining_seconds = divmod(seconds, 60)

        print(
            f"{minutes:02d}:{remaining_seconds:02d}",
            end="\r"
        )

        time.sleep(1)
        seconds -= 1

    print("Time's up!       ")

def main():
    print("===== COUNTDOWN TIMER =====")

    try:
        seconds = int(input("Enter countdown time in seconds: "))

        if seconds <= 0:
            print("Please enter a positive number.")
            return

        countdown(seconds)

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()

import time
import re
import subprocess
import sys


def parse_duration(duration_str):
    """
    Parse a duration string like '1h5m8s' into total seconds.
    """
    # Match all occurrences of numbers followed by valid time units (h, m, s)
    matches = re.findall(r"(\d+)([hms])", duration_str)
    if not matches:
        raise ValueError("Invalid duration format. Use a combination of 'h', 'm', and 's' (e.g., '1h5m8s').")

    total_seconds = 0
    for value, unit in matches:
        value = int(value)
        if unit == 'h':
            total_seconds += value * 3600
        elif unit == 'm':
            total_seconds += value * 60
        elif unit == 's':
            total_seconds += value
        else:
            raise ValueError("Invalid duration unit. Use 'h', 'm', or 's'.")

    return total_seconds


def timer(timer_name, duration_str):
    """
    Run a timer with the given name and duration.
    """
    try:
        total_duration = parse_duration(duration_str)
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(f"{total_duration} in seconds")

    interval = 1  # Update interval in seconds
    notification_id = None  # Store the ID of the current notification

    for elapsed in range(0, total_duration + 1, interval):
        percentage = int((elapsed / total_duration) * 100)
        message = f"{timer_name}: {percentage}% complete"
        
        # Send or update the notification
        if notification_id is None:
            # First notification, store its ID
            result = subprocess.run(
                ["dunstify", "-p", "-h", f"int:value:{percentage}", message],
                stdout=subprocess.PIPE,
                text=True
            )
            notification_id = result.stdout.strip()  # Capture the notification ID
        else:
            # Update the existing notification
            subprocess.run(
                ["dunstify", "-r", notification_id, "-h", f"int:value:{percentage}", message]
            )

        if elapsed < total_duration:
            time.sleep(interval)

    # Final notification when the timer is complete
    subprocess.run(
        ["dunstify", "-r", notification_id, f"{timer_name} complete!", "-h", "int:value:100"]
    )


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python dunst_timer.py <Timer Name> <Duration>")
        print("Example: python dunst_timer.py 'Break Timer' 5m")
        sys.exit(1)

    timer_name = sys.argv[1]
    duration = sys.argv[2]

    timer(timer_name, duration)

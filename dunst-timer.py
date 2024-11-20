#! /usr/bin/python3

import time
import re
import subprocess
import sys


def parse_duration(duration_str):
    """
    Parse a duration string like '5m' or '10s' into seconds.
    """
    match = re.match(r"(\d+)([sm])", duration_str)
    if not match:
        raise ValueError("Invalid duration format. Use '5m' for minutes or '10s' for seconds.")
    value, unit = match.groups()
    value = int(value)
    if unit == 'm':
        return value * 60
    elif unit == 's':
        return value
    else:
        raise ValueError("Invalid duration unit. Use 'm' for minutes or 's' for seconds.")


def timer(timer_name, duration_str):
    """
    Run a timer with the given name and duration.
    """
    try:
        total_duration = parse_duration(duration_str)
    except ValueError as e:
        print(f"Error: {e}")
        return

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

#!  /usr/bin/env python3

import time
import re
import subprocess
import sys
import argparse

APP_NAME = "Dunst Timer"

def parse_duration(duration_str):
    """
    Parse a duration string like '1h5m8s' or 'HH:MM:SS' into total seconds.
    """
    # Check for HH:MM:SS format
    if re.match(r"^\d{1,2}:\d{2}:\d{2}$", duration_str):
        parts = duration_str.split(":")
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
        return hours * 3600 + minutes * 60 + seconds

    # Match all occurrences of numbers followed by valid time units (h, m, s)
    matches = re.findall(r"(\d+)([hms])", duration_str)
    if not matches:
        raise ValueError("Invalid duration format. Use a combination of 'h', 'm', and 's' (e.g., '1h5m8s') or 'HH:MM:SS'.")

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

def stop_timer(notification_id):
    """
    Close the timer notification with the given ID.
    """
    subprocess.run(["dunstify", "-C", notification_id])

def start_timer(timer_name, duration_str):
    """
    Run a timer with the given name and duration.
    """
    try:
        total_duration = parse_duration(duration_str)
    except ValueError as e:
        print(f"Error: {e}")
        return

    interval = 0.5  # Update interval in seconds (500ms)
    notification_id = None  # Store the ID of the current notification
    start_time = time.time()
    try:
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > total_duration:
                break

            percentage = int((elapsed_time / total_duration) * 100)
            message = f"{timer_name}: {percentage}%"
            
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
                    ["dunstify", "-a", APP_NAME, "-r", notification_id, "-h", f"int:value:{percentage}", message]
                )

            time.sleep(interval)

        # Final notification when the timer is complete
        subprocess.run(
            ["dunstify", "-r", notification_id, f"{timer_name} complete!", "-h", "int:value:100"]
        )
    except KeyboardInterrupt:
        # Handle Ctrl+C to stop the timer
        stop_timer(notification_id)
        print("\nTimer aborted.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a timer with notifications.")
    parser.add_argument("-t", "--title", required=False, help="Title of the timer", default="Timer")
    parser.add_argument("-d", "--duration", required=True, help="Duration of the timer (e.g., '1h5m8s' or 'HH:MM:SS')")
    
    args = parser.parse_args()

    start_timer(args.title, args.duration)

# Dunst Timer

A timer which is displayed as a dunst notification

## Motivation

A few weeks ago a great project appeared on Reddit and other platforms:
[mpris-timer](https://github.com/efogdev/mpris-timer)

A simple timer which uses the MPRIS interface to display a timer as a notification. I really liked the idea and wanted to create a similar application which uses the dunst notification system, because different window managers and desktop environments use different styles of a bar so maybe a media-styled notification would not fit in every environment.

## Features & Usage

![](doc/example1.png)

Emojis are supported too 😍

![](doc/example2.png)

And if you don't want to be stressed by the remaining time you can disable the percentage

![](doc/example3.png)

```bash
python dunst-timer.py -d 10m -t "A 10 minute timer 💼 "
```

or if the application is installed

```bash
dunst-timer -d 10m
```

The timer is blocking, so you can't use the terminal until the timer is finished. If you want to run the timer in the background you can use the `&` operator

```bash
dunst-timer -d 10m &
```

**Full Spec**
```bash
Usage: dunst-timer [-t TITLE] -d DURATION [-p]
Run a timer with notifications.
  -t, --title       Title of the timer (default: 'Timer')
  -d, --duration    Duration of the timer (e.g., '1h5m8s' or 'HH:MM:SS')
  -p, --percentage  Print the percentage of the timer
  -h, --help        Print this help message
```

## Installation & Configuration

### Arch User Repository

The application is available in the AUR as `dunst-timer`

    ```bash
    yay -S dunst-timer
    ```

### Manual Installation

On any other system you can install the application by cloning the repository and copying the script to `/usr/bin` (or any other directory in your `$PATH`)

```bash
    git clone https://github.com/bitSheriff/dunst-timer.git
    cd dunst-timer
    cp dunst-timer.py /usr/bin/dunst-timer
    chmod +x /usr/bin/dunst-timer
```
### Configuration

The script uses the `dunst` notification system, so it will use the default settings of `dunst`. If you want to change the settings you can do this in the `dunstrc` file. The default location is `~/.config/dunst/dunstrc`.

To enable the progress bar, use these (or similar) settings:
```txt
    # Window Confiration
    width = 300
    height = 100
    offset = +5x+10
    origin = top-right

    # Turn on the progess bar
    progress_bar = true

    # Set the progress bar height. This includes the frame, so make sure
    # it's at least twice as big as the frame width.
    progress_bar_height = 10

    # Set the frame width of the progress bar
    progress_bar_frame_width = 1

    # Set the minimum width for the progress bar
    progress_bar_min_width = 150

    # Set the maximum width for the progress bar
    progress_bar_max_width = 300

```

Change the color of the timer:
    
```bash
    [dunst-timer]
    appname = Dunst Timer
    urgency = normal
    frame_color = "#2b18e1"
```

For more information about the configuration of `dunst` see the [dunst documentation](https://dunst-project.org/documentation/)
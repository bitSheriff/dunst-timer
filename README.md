# Dunst Timer

A timer which is displayed as a dunst notification

## Installation

### Arch User Repository

The application is available in the AUR as `dunst-timer`

    ```bash
    yay -S dunst-timer
    ```

### Manual Installation

On any other system you can install the application by cloning the repository and copying the script to `/usr/bin` (or any other directory in your `$PATH`)

`bash
    git clone https://github.com/bitSheriff/dunst-timer.git
    cd dunst-timer
    cp dunst-timer.py /usr/bin/dunst-timer
    chmod +x /usr/bin/dunst-timer
    `

## Usage

    ```bash
    python dunst-timer.py -d 10m
    ```

    or if the application is installed

    ```bash
    dunst-timer -d 10m
    ```

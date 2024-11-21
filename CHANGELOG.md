# Changelog and Release Notes

## [v1.00.07]

### 🚀 Features

- **Handle Keyboard Interrupts** [Issue #6](https://github.com/bitSheriff/dunst-timer/issues/6)
- **Percentage is now optional**: the percentage is only displayed if the `-p` flag is set

### 🛠 Fixes

- **App Name**: now the app name is set for the dunst notification
    - so it can be filtered in the settings more easily
- **Usage**: works now with custom instructions

## [v1.00.04] - [v1.00.06]

### 🛠 Fixes

- released the package on the [AUR](https://aur.archlinux.org/packages/dunst-timer), ran into some problems

## [v1.00.03]

### 🚀 Features

- **Mixed Duration Parsing** ([Issue #2](https://github.com/bitSheriff/dunst-timer/issues/2)): The parse_duration function now supports parsing mixed duration strings like 1h5m8s. It can handle combinations of hours (h), minutes (m), and seconds (s) in a single input string.
  - further the `HH:MM:SS` format is also supported
- **Options** ([Issue #1](https://github.com/bitSheriff/dunst-timer/issues/1)): The script now supports the `-t` for the title and `-d` for the duration option.
  - the `-t` is optional, if not provided the title will be set to "Timer"

### 🛠 Fixes

- use time measurement to calculate the remaining time, not the theoretical time which the process sleeps

## [v1.00.02]

### 🛠 Fixes

- added `dunst` as a dependency

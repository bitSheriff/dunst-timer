# Changelog and Release Notes

## [v1.00.03]

### 🚀 Features

- **Mixed Duration Parsing** ([Issue #2](https://github.com/bitSheriff/dunst-timer/issues/2)): The parse_duration function now supports parsing mixed duration strings like 1h5m8s. It can handle combinations of hours (h), minutes (m), and seconds (s) in a single input string.
    - further the `HH:MM:SS` format is also supported
- **Options** ([Issue #1](https://github.com/bitSheriff/dunst-timer/issues/1)): The script now supports the `-t` for the title and `-d` for the duration option.
    - the `-t` is optional, if not provided the title will be set to "Timer"

## [v1.00.02]

### 🛠 Fixes

- added `dunst` as a dependency

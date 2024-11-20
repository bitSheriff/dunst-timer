# Justfile for release management
set shell := ["bash", "-uc"]

# Default target
default:
    just --choose

# Prompt for the tag version and create a release
release:
    #!/bin/bash

    # Check if currently on branch master
    if [ "$(git rev-parse --abbrev-ref HEAD)" != "master" ]; then
        echo "You must be on the master branch to create a release."
        exit 1
    fi


    echo "Last 5 tags:"
    git tag --sort=-v:refname | head -n 5
    echo "Enter the new release version (e.g., X.YY.ZZ):"
    version=$(gum input --placeholder "X.YY.ZZ")
    echo "$version" | grep -E '^[0-9]+\.[0-9]{2}\.[0-9]{2}$' > /dev/null || { 
        echo "Invalid version format. Please use X.YY.ZZ (e.g., 1.02.03).";
        exit 1; 
    }

    gum confirm --default=false "Commit and Push?" && (
        # Commit and tag the new release
        echo "Committing changes and creating tag..."
        git add -u
        git commit -m "Release v$version"
        git tag -f "v$version"
        echo "Tag v$version created."

        git push -f origin
        git push -f --tags
        echo "Pushed changes and tags to all remotes."
    )
    echo "Done"

# Clean the package
clean:
    # remove all archives
    rm -rf **.tar.gz
    rm -rf build dist pkg src

# Build and install the package
install:
    makepkg -si

# different checks
check:
    # Comming soon
    #

# Install the needed dependencies for the development process
install-dep:
    yay -S pyinstaller

# Build the application to a binary
build:
    #!/bin/bash
    echo "Creat the binary with PyInstaller"
    pyinstaller --clean --onefile ./dunst-timer.py

# Justfile for release management
set shell := ["bash", "-uc"]


# Prompt for the tag version and create a release

release:
    #!/bin/bash
    echo "Last 5 tags:"
    git tag --sort=-v:refname | head -n 5
    echo "Enter the new release version (e.g., X.YY.ZZ):"
    version=$(gum input --placeholder "X.YY.ZZ")
    echo "$version" | grep -E '^[0-9]+\.[0-9]{2}\.[0-9]{2}$' > /dev/null || { 
        echo "Invalid version format. Please use X.YY.ZZ (e.g., 1.02.03).";
        exit 1; 
    }
    git add tag "v$version"
    echo "Tag $version created."
    git push --tags
    echo "Pushed tags to all remotes."

# Clean the package
clean:
    makepkg -C

# Build and install the package
install:
    makepkg -si

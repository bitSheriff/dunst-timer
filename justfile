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

    # Update the version in PKGBUILD
    echo "Updating PKGBUILD version..."
    sed -i "s/pkgver=.*/pkgver=$version/" PKGBUILD
    sed -i "s/pkgrel=.*/pkgrel=1/" PKGBUILD

    # Generate a new source tarball
    echo "Generating source tarball..."
    tar czf "v$version.tar.gz" *

    # Generate and update the SHA256 checksum
    echo "Calculating SHA256 checksum..."
    checksum=$(sha256sum "v$version.tar.gz" | awk '{ print $1 }')
    echo "$checksum"
    sed -i "s/sha256sums=.*/sha256sums=('${checksum}')/" PKGBUILD

    # Regenerate .SRCINFO
    echo "Regenerating .SRCINFO..."
    makepkg --printsrcinfo > .SRCINFO

    gum confirm --default=false "Commit and Push?" && (
        # Commit and tag the new release
        echo "Committing changes and creating tag..."
        git add PKGBUILD .SRCINFO
        git commit -m "Release v$version"
        git tag -f "v$version"

        echo "Tag v$version created."
        git push -f origin
        git push aur
        git push --tags
        echo "Pushed changes and tags to all remotes."
    )
    echo "Done"

# Clean the package
clean:
    # remove all archives
    rm -rf **tar.gz
    makepkg -C

# Build and install the package
install:
    makepkg -si

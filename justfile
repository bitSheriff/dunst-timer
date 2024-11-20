# Justfile for release management

# Prompt for the tag version and create a release
release:
    @echo "Last 5 tags:"
    @git tag --sort=-v:refname | head -n 5
    @echo "Enter the release version (e.g., X.YY.ZZ):"
    @read version && \
    git tag "$$version" && \
    echo "Tag $$version created." && \
    git push --tags && \
    echo "Pushed tags to all remotes."

clean:
    makepkg -C

install:
    makepkg -si

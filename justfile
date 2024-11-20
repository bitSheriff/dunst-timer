# Justfile for release management

# Prompt for the tag version and create a release
release:
    @echo "Enter the release version (e.g., X.YY.ZZ):"
    @read version && \
    git tag "$$version" && \
    echo "Tag $$version created." && \
    git push --tags && \
    echo "Pushed tags to all remotes."


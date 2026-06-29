from documentation.generators.readme import generate_readme


def generate_all_documentation() -> None:
    print("Generating documentation artifacts...")
    print("=" * 60)

    generate_readme()

    print("=" * 60)
    print("Documentation generation completed successfully.")


if __name__ == "__main__":
    generate_all_documentation()

from pathlib import Path
import re


BASE_DIR = Path(__file__).resolve().parent

BASE_PROFILE_FILE = BASE_DIR / "profile.base.txt"
COLORED_PROFILE_FILE = BASE_DIR / "profile.txt"
README_FILE = BASE_DIR / "README.md"


# ANSI escape sequences
RESET = "\033[0m"
BOLD = "\033[1m"

LOGO_COLOR = "\033[97m"    
SECTION_COLOR = "\033[33m"   
LABEL_COLOR = "\033[92m"     
VALUE_COLOR = "\033[97m"     
SEPARATOR_COLOR = "\033[90m" 


# Matches section names such as:
# [ Personal Info ]
# [ Tech Stack ]
SECTION_PATTERN = re.compile(r"\[ [^\]]+ \]")

# Matches labels such as:
# Name:
# Country:
# Email:
# Languages:
# Expertise:
# Databases:
# Frameworks:
# Tools & Others:
LABEL_PATTERN = re.compile(
    r"(Name|Country|Email|Languages|Expertise|Databases|Frameworks|Tools & Others):"
)

# Matches the separator:
# -----------------
SEPARATOR_PATTERN = re.compile(r"-{17}")


def read_base_profile() -> str:
    """Read the plain-text source profile."""
    return BASE_PROFILE_FILE.read_text(encoding="utf-8").rstrip()


def colorize_profile(profile: str) -> str:
    """
    Convert the plain profile into an ANSI-colored profile.

    The original profile is never modified.
    """
    output = []

    for line in profile.splitlines():

        # Preserve empty lines.
        if not line.strip():
            output.append("")
            continue

        # ---------------------------------------------------------
        # Section headers
        # ---------------------------------------------------------
        section_match = SECTION_PATTERN.search(line)

        if section_match:
            start, end = section_match.span()

            prefix = line[:start]
            section = line[start:end]

            output.append(
                f"{BOLD}{LOGO_COLOR}{prefix}{RESET}"
                f"{BOLD}{SECTION_COLOR}{section}{RESET}"
            )

            continue

        # ---------------------------------------------------------
        # Labels + values
        # ---------------------------------------------------------
        label_match = LABEL_PATTERN.search(line)

        if label_match:
            start, end = label_match.span()

            prefix = line[:start]
            label = line[start:end]
            value = line[end:]

            output.append(
                f"{BOLD}{LOGO_COLOR}{prefix}{RESET}"
                f"{BOLD}{LABEL_COLOR}{label}{RESET}"
                f"{VALUE_COLOR}{value}{RESET}"
            )

            continue

        # ---------------------------------------------------------
        # Separator
        # ---------------------------------------------------------
        separator_match = SEPARATOR_PATTERN.search(line)

        if separator_match:
            start, end = separator_match.span()

            prefix = line[:start]
            separator = line[start:end]
            suffix = line[end:]

            output.append(
                f"{LOGO_COLOR}{prefix}{RESET}"
                f"{SEPARATOR_COLOR}{separator}{RESET}"
                f"{LOGO_COLOR}{suffix}{RESET}"
            )

            continue

        # ---------------------------------------------------------
        # Everything else is ASCII art
        # ---------------------------------------------------------
        output.append(
            f"{LOGO_COLOR}{line}{RESET}"
        )

    return "\n".join(output) + '\n'


def generate_readme(profile: str) -> str:
    """
    Generate README.md using the plain profile.

    No ANSI escape sequences are included here.
    """
    return f"""<pre>
<b>zoanig@github.com:~$</b> fastfetch
<code>
{profile}
</code>
</pre>

"""


def write_colored_profile(profile: str) -> None:
    """Write the ANSI-colored profile used by Vercel."""
    colored_profile = colorize_profile(profile)

    COLORED_PROFILE_FILE.write_text(
        colored_profile,
        encoding="utf-8",
    )


def write_readme(profile: str) -> None:
    """Write the clean GitHub README."""
    README_FILE.write_text(
        generate_readme(profile),
        encoding="utf-8",
    )


def main():
    # profile-base.txt is the ONLY source.
    profile = read_base_profile()

    # Generate Vercel's colored response.
    write_colored_profile(profile)

    # Generate GitHub's clean README.
    write_readme(profile)

    print("Profile generated successfully.")
    print(f"  Source : {BASE_PROFILE_FILE.name}")
    print(f"  Vercel : {COLORED_PROFILE_FILE.name}")
    print(f"  GitHub : {README_FILE.name}")


if __name__ == "__main__":
    main()
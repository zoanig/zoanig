import json
import sys
from pathlib import Path
try:
    with open("profile.json", 'r') as file:
        DATA = json.loads(file.read())
except FileNotFoundError:
    print(f"You must have a file named \"profile.json\" in the same directory as {__file__}")
    sys.exit(1)

try:
    with open(DATA['ascii']['file'], 'r') as file:
        ASCII_ART = file.read()
except FileNotFoundError:
    print(f'ASCII file not found: {Path.cwd() / DATA['ascii']['file']}')
    sys.exit(1)


def generate_fetch_layout(config, logo_str, gap=4, color=True, newline=True):
    c_headline = "\033[1;32m" if color else ""
    c_title = "\033[1;34m" if color else ""
    c_key = "\033[1;36m" if color else ""
    c_reset = "\033[0m" if color else ""
    profile = config["profile"]
    logo_lines = [f'{c_key}{line}{c_reset}' for line in logo_str.split("\n") if line.strip() or logo_str.startswith(line)]
    logo_lines.append(f'      ASCII by {c_title}{DATA['ascii']['artist']}{c_reset}')
    max_logo_width = max(len(line) for line in logo_lines) if logo_lines else 0
    all_keys = []
    for section in profile["sections"]:
        all_keys.extend(section["fields"].keys())
    text_lines = []
    
    headline = profile["headline"]
    text_lines.append(f"{c_headline}{headline}{c_reset}")
    text_lines.append("-" * len(headline))
    
    for section in (profile["sections"]):
        if profile["sections"].index(section) > 0:
            text_lines.append("")
        title = f'[ {section['title']} ]'
        text_lines.append(f"{c_title}{title}{c_reset}")
        
        for key, value in section["fields"].items():
            text_lines.append(f"  {c_key}{key}{c_reset} : {value}")
    total_lines = max(len(logo_lines), len(text_lines))
    output_lines = []
    for i in range(total_lines):
        logo_part = logo_lines[i] if i < len(logo_lines) else ""
        logo_padded = logo_part.ljust(max_logo_width)
        text_part = text_lines[i] if i < len(text_lines) else ""
        output_lines.append(f"{logo_padded}{' ' * gap}{text_part}")
        
    return "\n".join(output_lines) + "\n" if newline else ""

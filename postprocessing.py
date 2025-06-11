import re
import sys
from pathlib import Path

def update_marimo_filename(html_file, new_name):
    """Update the marimo-filename tag in the HTML file."""
    html_path = Path(html_file)
    if not html_path.is_file():
        print(f"Error: {html_file} does not exist.")
        return False
    
    content = html_path.read_text()

    updated_content = re.sub(
        r'<marimo-filename hidden>.*?</marimo-filename>',
        f'<marimo-filename hidden>{new_name}</marimo-filename>',
        content,
    )

    html_path.write_text(updated_content)
    print(f"Updated marimo-filename in {html_file} to {new_name}")
    return True

if __name__ == "__main__":
    success = update_marimo_filename("output_dir/index.html", "Savannah Bailey")
    sys.exit(0 if success else 1)
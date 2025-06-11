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

def improve_seo(html_file):
    """Improve SEO by adding a meta description."""
    html_path = Path(html_file)
    if not html_path.is_file():
        print(f"Error: {html_file} does not exist.")
        return False
    
    content = html_path.read_text()

    # Look for the description meta tag
    meta_tag = '<meta name="description" content="a marimo app" />'
    meta_insertion_point = content.find(meta_tag)
    
    if meta_insertion_point == -1:
        print("Could not find meta description tag")
        return False

    # Calculate position after the existing meta tag
    end_of_meta_tag = content.find('>', meta_insertion_point) + 1
    
    # Prepare the updated description and additional SEO tags
    updated_meta = '<meta name="description" content="Savannah Bailey - Python Core Developer working on the JIT, Snowflake, and Jupyter" />'
    seo_tags = """
    <meta name="author" content="Savannah Bailey" />
    <meta name="keywords" content="Python, Core Developer, JIT, Snowflake, Jupyter, Programming" />
    <meta property="og:title" content="Savannah Bailey - Python Core Developer" />
    <meta property="og:description" content="Python Core Developer and Python Developer Experience at Snowflake" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://savannah.dev" />
    <meta name="twitter:card" content="summary" />
    <meta name="twitter:title" content="Savannah Bailey - Python Core Developer" />
    <meta name="twitter:description" content="Python Core Developer working on the JIT, Snowflake, and Jupyter" />
    """
    
    # Replace the old meta tag and add new SEO tags in one operation
    updated_content = content[:meta_insertion_point] + updated_meta + seo_tags + content[end_of_meta_tag:]
    
    # Write the updated content back to the file
    html_path.write_text(updated_content)
    print(f"Updated {html_file} with SEO improvements")
    return True

if __name__ == "__main__":
    success = update_marimo_filename("output_dir/index.html", "Savannah Bailey")
    success &= improve_seo("output_dir/index.html")
    sys.exit(0 if success else 1)
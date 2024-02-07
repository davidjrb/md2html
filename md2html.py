import markdown
import sys

def convert_md_to_html(input_filename, output_filename):
    # Read the Markdown file
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        md_text = input_file.read()

    # Convert the Markdown to HTML
    html_content = markdown.markdown(md_text)

    # Write the HTML content to the output file
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(html_content)

    print(f"Converted {input_filename} to {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python md2html.py test.md test.html")
    else:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
        convert_md_to_html(input_filename, output_filename)

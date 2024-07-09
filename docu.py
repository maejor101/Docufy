import pdfkit
import os
import subprocess

def check_wkhtmltopdf():
    """Check if wkhtmltopdf is installed and in PATH."""
    try:
        subprocess.run(["wkhtmltopdf", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("wkhtmltopdf is installed and accessible.")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("wkhtmltopdf is not installed or not in PATH. Please install it and add to PATH.")
        return False
    return True

def convert_html_to_pdf(html_content, output_pdf_path):
    try:
        pdfkit.from_string(html_content, output_pdf_path)
        print(f"PDF generated successfully at: {output_pdf_path}")
    except OSError as e:
        print(f"Failed to generate PDF. OS error: {e}")
    except Exception as e:
        print(f"Failed to generate PDF: {e}")

if __name__ == "__main__":
    # Check if wkhtmltopdf is installed
    if not check_wkhtmltopdf():
        exit(1)

    # Example HTML file path
    html_file_path = r"C:\Users\vusum\OneDrive\Desktop\Gazette-Prototype\doc.html"

    # Check if the HTML file exists
    if not os.path.exists(html_file_path):
        print(f"HTML file does not exist: {html_file_path}")
    else:
        try:
            # Read HTML content from file
            with open(html_file_path, "r", encoding="utf-8") as file:
                example_html = file.read()

            # CSS styles
            css_styles = """
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    margin: 0;
                    padding: 0;
                }
                h1 {
                    color: red;
                    text-align: center;
                    margin-top: 20%;
                }
            </style>
            """

            # Embed CSS styles within the HTML content
            example_html_with_css = f"{css_styles}{example_html}"

            # Output PDF path
            output_path = "output.pdf"

            # Convert HTML to PDF
            convert_html_to_pdf(example_html_with_css, output_path)
        except Exception as e:
            print(f"Error reading HTML file: {e}")

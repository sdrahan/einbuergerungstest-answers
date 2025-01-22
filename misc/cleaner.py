import sys
from bs4 import BeautifulSoup

def clean_html_file(source_filename):
    # Read the source HTML file
    with open(source_filename, "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all question blocks
    question_blocks = soup.find_all("div", class_="mb-8")

    for question_block in question_blocks:
        # Find all answer list items
        answers = question_block.find_all("li", class_="mb-2")

        for answer in answers:
            # Check if the answer contains the class "bg-green-100"
            if "bg-green-100" not in answer.find("span").get("class", []):
                # Remove incorrect answers
                answer.decompose()

    # Get the modified HTML content
    cleaned_html = soup.prettify()

    # Create the output filename
    output_filename = source_filename.replace(".html", "_cleaned.html")

    # Save the cleaned HTML to a new file
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(cleaned_html)

    print(f"Cleaned file saved as: {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <source_filename>")
    else:
        source_filename = sys.argv[1]
        clean_html_file(source_filename)
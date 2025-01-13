from bs4 import BeautifulSoup

def extract_links(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all <a> tags with an href attribute
    links = [a['href'] for a in soup.find_all('a', href=True)]
    
    return links

if __name__ == "__main__":
    # Load the HTML content (replace with the actual content or file reading)
    html_file = "input.html"
    
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Extract links
    links = extract_links(html_content)
    
    # Print all extracted links
    for link in links:
        print(link)
    
    # Optionally save to a file
    with open('extracted_links.txt', 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(links))

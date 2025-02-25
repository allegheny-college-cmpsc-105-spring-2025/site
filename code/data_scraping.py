import requests
from bs4 import BeautifulSoup

# Example usage
topic = "scikit-image"  # Change this to any topic

url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
response = requests.get(url)

if response.status_code != 200:
    return "Error: Could not retrieve the page."

soup = BeautifulSoup(response.text, "html.parser")
paragraphs = soup.find_all("p")

# for p in paragraphs:
#     if p.text.strip():  # Ensure it's not an empty paragraph
#         p.text.strip()
#       break
    
print(soup)
print(paragraphs)

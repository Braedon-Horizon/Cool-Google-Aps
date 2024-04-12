import requests
from bs4 import BeautifulSoup

def scrape_google_form(url):
    # Send a GET request to the URL and retrieve the HTML content
    response = requests.get(url)
    html_content = response.content

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all the form fields
    form_fields = soup.find_all("div", class_="freebirdFormviewerComponentsQuestionBaseRoot")

    # Create a list to store the form fields
    fields = []

    # Iterate over the form fields and extract the relevant information
    for field in form_fields:
        # Extract the field label
        label = field.find("div", class_="freebirdFormviewerComponentsQuestionBaseTitle").text.strip()
        
        # Extract the field type
        field_type = "text"  # Default to text field
        if field.find("textarea"):
            field_type = "textarea"
        elif field.find("input", type="radio"):
            field_type = "radio"
        elif field.find("input", type="checkbox"):
            field_type = "checkbox"
        
        # Add the field to the list
        fields.append((label, field_type))
    
    return fields
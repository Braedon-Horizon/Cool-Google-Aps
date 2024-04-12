# main.py

from scraper import scrape_google_form
from analyzer import analyze_form_fields
from generator import generate_responses
from submitter import submit_form

def main():
    # The URL of the Google Form
    url = "https://docs.google.com/forms/d/e/1FAIpQLSfMP713OTqoL5iRUBCT3F9iqlZJj5dXINBr3v83E-YuZZ-iPg/viewform?usp=sf_link"

    # Scrape the Google Form
    fields = scrape_google_form(url)

    # Analyze the form fields
    analyzed_fields = analyze_form_fields(fields)

    # Generate responses for the form fields
    responses = generate_responses(analyzed_fields)

    # Submit the form
    submit_form(url, responses)

# Call the main function
if __name__ == "__main__":
    main()
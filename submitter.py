# submitter.py

from selenium import webdriver

def submit_form(url, responses):
    # Create a new instance of the Firefox driver
    driver = webdriver.Chrome()

    # Go to the Google Form
    driver.get(url)

    # Find the form fields and fill them out with the generated responses
    for i, response in enumerate(responses):
        # Find the i-th form field
        field = driver.find_element_by_xpath(f"//input[@name='entry.{i}']")

        # Fill out the form field with the response
        field.send_keys(response)

    # Submit the form
    driver.find_element_by_xpath("//span[contains(text(), 'Submit')]").click()

    # Close the driver
    driver.quit()
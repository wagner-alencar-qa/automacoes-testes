"""
Custom assertion helpers for improved test readability and reliability.
"""


class CustomAssertions:
    """Custom assertions for Selenium test automation."""

    @staticmethod
    def assert_page_loaded(driver, expected_url_part):
        """Assert that the page has loaded with the expected URL."""
        assert expected_url_part in driver.current_url, \
            f"Expected URL to contain '{expected_url_part}', but got '{driver.current_url}'"

    @staticmethod
    def assert_element_visible(element):
        """Assert that an element is visible on the page."""
        assert element.is_displayed(), "Element should be visible"

    @staticmethod
    def assert_element_text_contains(element, expected_text):
        """Assert that element text contains the expected text."""
        actual_text = element.text
        assert expected_text.lower() in actual_text.lower(), \
            f"Expected element text to contain '{expected_text}', but got '{actual_text}'"

    @staticmethod
    def assert_element_text_equals(element, expected_text):
        """Assert that element text exactly matches the expected text."""
        actual_text = element.text.strip()
        assert actual_text == expected_text.strip(), \
            f"Expected element text '{expected_text}', but got '{actual_text}'"

    @staticmethod
    def assert_page_source_contains(driver, expected_text):
        """Assert that the page source contains the expected text."""
        assert expected_text.lower() in driver.page_source.lower(), \
            f"Expected page to contain '{expected_text}'"

    @staticmethod
    def assert_number_of_elements(elements, expected_count):
        """Assert that the number of elements matches the expected count."""
        actual_count = len(elements)
        assert actual_count == expected_count, \
            f"Expected {expected_count} elements, but found {actual_count}"

    @staticmethod
    def assert_element_enabled(element):
        """Assert that an element is enabled."""
        assert element.is_enabled(), "Element should be enabled"

    @staticmethod
    def assert_element_attribute_contains(element, attribute, expected_value):
        """Assert that an element's attribute contains the expected value."""
        actual_value = element.get_attribute(attribute)
        assert expected_value in actual_value, \
            f"Expected attribute '{attribute}' to contain '{expected_value}', but got '{actual_value}'"

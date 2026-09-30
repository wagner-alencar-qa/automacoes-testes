from selenium import webdriver


class Application:
    """Guará Application class for fluent test writing with BDD support."""
    
    def __init__(self, driver=None):
        self.driver = driver or webdriver.Chrome()
        self._result = None

    def given(self, *args, **kwargs):
        """Setup phase for test scenarios."""
        return self

    def when(self, action, *args, **kwargs):
        """Action phase - execute a transaction or action."""
        if isinstance(action, type):
            # If it's a class, instantiate and execute
            action_instance = action(self.driver)
            self._result = action_instance.do(*args, **kwargs)
        else:
            # If it's already an instance, execute its do method
            self._result = action.do(*args, **kwargs)
        return self

    def then(self, assertion, *args, **kwargs):
        """Assertion phase - validate the result."""
        if callable(assertion):
            assertion(self._result, *args, **kwargs)
        return self

    @property
    def result(self):
        """Get the result of the last operation."""
        return self._result


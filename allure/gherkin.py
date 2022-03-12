import allure



from typing import Optional

from .report import step as s


def _step(description: Optional[str] = None):
    def decorated(fn):
        if description:
            fn.__name__ = description.replace(' ', '_')                             # todo: improve (leave it with spaces?)
        return s(fn, display_context=False)()
    return decorated


def given(precondition: Optional[str] = None):
    return _step(precondition)


def when(act: Optional[str] = None):
    return _step(act)


def then(assertion: Optional[str] = None):
    return _step(assertion)


"""
Class wrapper was used to make difference between function wrappers and test steps in report
"""
class Given:

    def __new__(cls):
        cls.given(cls)
        return super(Given, cls).__new__(cls)
    
    @allure.step("GIVEN")
    def given(self):
        pass

class When:

    def __new__(cls):
        cls.when(cls)
        return super(When, cls).__new__(cls)
    
    @allure.step("WHEN")
    def when(self):
        pass

class Then:

    def __new__(cls):
        cls.then(cls)
        return super(Then, cls).__new__(cls)

    @allure.step("THEN")
    def then(self):
        pass


class And:
    
    def __new__(cls):
        cls.and_(cls)
        return super(And, cls).__new__(cls)

    @allure.step("AND")
    def and_(self):
        pass

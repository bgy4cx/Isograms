from behave import *
from isograms import IsItEmpty
from isograms import IsItIsogram

@given('a string')
def given_impl(context):
    pass

@when('got eny empty string')
def when_impl(context):
    assert (IsItEmpty("") is True)

@then('result is true')
def then_impl(context):
    assert (IsItIsogram(str) is True)

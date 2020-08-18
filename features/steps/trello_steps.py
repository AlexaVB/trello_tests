from behave import when
from behaving.web.steps import *

@given('I have created a Trello board with three cards')
def step_impl(context):
    context.execute_steps(f'''
        Given a browser
        When I visit "https://trello.com/login"
        And I fill in "user" with "{os.environ['USER_EMAIL']}"
        And I fill in "password" with "{os.environ['USER_PASSWORD']}"
        And I press "Log in"
    ''')
    assert context.browser.find_by_text('My Trello board')
    context.browser.find_by_css('.board-tile').click()

@then('I can see the three cards on the Trello board')
def step_impl(context):
    assert context.browser.find_by_text('Card 1')
    assert context.browser.find_by_text('Card 2')
    assert context.browser.find_by_text('Card 3')

@when('I edit a Trello card')
def step_impl(context):
    context.add_desc()

@then('I can see the Trello card has been updated')
def step_impl(context):
    context.browser.find_by_css('.list-card').last.click()
    assert context.browser.find_by_text('This is the card description')  

@when('I delete a Trello card')
def step_impl(context):
    context.delete_card()

@then('I can see the Trello card has been deleted')
def step_impl(context):
    assert context.browser.find_by_text('Card 1')
    assert context.browser.find_by_text('Card 2')
    assert not context.browser.find_by_text('Card 3')

@when('I add a comment to a Trello card')
def step_impl(context):
    context.add_comment()

@then('I can see the comment on the Trello card')
def step_impl(context):
    context.browser.find_by_text('Card 3').click()
    assert context.browser.find_by_text('This is the card comment')

@when('I add a comment to a Trello card using the browser')
def step_impl(context):
    context.browser.find_by_css('.list-card').click()
    context.browser.find_by_css('.comment-box-input').fill('This is the browser card comment')
    context.browser.find_by_css('.confirm').click()

@then('I can see the comment has been added to the Trello card')
def step_impl(context):
    assert context.browser.find_by_text('This is the browser card comment')

@when('I set the Trello card to done')
def step_impl(context):
    context.browser.find_by_css('.list-card').click()
    context.browser.find_by_text('Move').click()
    context.browser.find_by_css('.js-select-list').select_by_text('Done')
    context.browser.find_by_css('input.primary:nth-child(4)').click()
    context.browser.find_by_css('.js-close-window').click()

@then('I can see the Trello card is done')
def step_impl(context):
    context.browser.find_by_text('Card 1').click()
    assert context.browser.find_by_text('Done')

@then('I should see there is no account for this username error message')
def step_impl(context):
    assert context.browser.find_by_text('There isn\'t an account for this username')

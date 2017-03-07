import nose

import requests
from behave import when, given, then

from kombu_producer import publish_message


@given('a message is consumed by the system with client id {client_id:d} and gender {gender}')
def consume_message(context, client_id, gender):
    message = {"client_id": client_id, "gender": gender}
    nose.tools.assert_true(publish_message(message))


@when('I ask for the gender of the client id {client_id:d}')
@when('I ask for the gender of the client id {client_id:d} with the {heuristic} heuristic')
def update_list_of_policies(context, client_id, heuristic="default"):
    server_answer = requests.get("{}{}".format(context.address, "/getGender/{}/?heuristic={}".format(
        client_id, heuristic)))
    context.server_answer = server_answer


@then('the response is ok and the gender is {gender}')
def number_policies_ok(context, gender):
    nose.tools.assert_true(context.server_answer.ok)
    nose.tools.assert_equal(context.server_answer.json()["data"]["gender"], gender)


@then('the response is not ok and the error code is {status_code:d}')
def number_policies_ok(context, status_code):
    nose.tools.assert_false(context.server_answer.ok)
    nose.tools.assert_equal(context.server_answer.status_code, status_code)

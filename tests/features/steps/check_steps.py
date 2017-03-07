import nose
import json
import requests
from behave import step, when


@when('the microservice is up and running')
def check_health(context):
    server_answer = requests.get("{}{}".format(context.address, "/_internal_/health"))
    nose.tools.assert_true(server_answer)
    context.server_answer = server_answer


@step('the response of the microservice is "{user_answer}"')
def check_health_response(context, user_answer):
    nose.tools.assert_equal(context.server_answer.json(), json.loads(user_answer))

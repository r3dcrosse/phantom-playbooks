"""
Generate prompt/task approvals
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'DogedogeDogedogeDogedogeDogedogeDogedoge' block
    DogedogeDogedogeDogedogeDogedogeDogedoge(container=container)

    # call 'prompt_2' block
    prompt_2(container=container)

    # call 'prompt_3' block
    prompt_3(container=container)

    # call 'task_1' block
    task_1(container=container)

    return

"""
DogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedoge
"""
def DogedogeDogedogeDogedogeDogedogeDogedoge(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('DogedogeDogedogeDogedogeDogedogeDogedoge() called')
    
    # set user and message variables for phantom.prompt call
    user = "Administrator"
    message = """Prompt for administrator..."""

    phantom.prompt(container=container, user=user, message=message, respond_in_mins=120, name="DogedogeDogedogeDogedogeDogedogeDogedoge")

    return

def prompt_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('prompt_2() called')
    
    # set user and message variables for phantom.prompt call
    user = "admin"
    message = """Prompt for admin..."""

    # response options
    options = {
        "type": "list",
        "choices": [
            "Yes",
            "No",
        ]
    }

    phantom.prompt(container=container, user=user, message=message, respond_in_mins=30, name="prompt_2", options=options)

    return

def prompt_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('prompt_3() called')
    
    # set user and message variables for phantom.prompt call
    user = "Administrator"
    message = """On a scale of 1 to 99, how Doge are you? Administrator answer only..."""

    # response options
    options = {
        "type": "range",
        "min": 1,
        "max": 99,
    }

    phantom.prompt(container=container, user=user, message=message, respond_in_mins=30, name="prompt_3", options=options)

    return

def task_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('task_1() called')
    
    # set user and message variables for phantom.task call
    user = "Administrator"
    message = "DogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedogeDogedoge"

    phantom.task(user=user, message=message, respond_in_mins=1337, name="task_1")

    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    # This function is called after all actions are completed.
    # summary of all the action and/or all detals of actions 
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return
"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'playbook_r3d_GitHub_sleep_1_1' block
    playbook_r3d_GitHub_sleep_1_1(container=container)

    return

def playbook_r3d_GitHub_sleep_1_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('playbook_r3d_GitHub_sleep_1_1() called')
    
    # call playbook "r3d--GitHub/sleep", returns the playbook_run_id
    playbook_run_id = phantom.playbook("r3d--GitHub/sleep", container=container, name="playbook_r3d_GitHub_sleep_1_1", callback=playbook_r3d_GitHub_sleep_2_2)

    return

def playbook_r3d_GitHub_sleep_2_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('playbook_r3d_GitHub_sleep_2_2() called')
    
    # call playbook "r3d--GitHub/sleep", returns the playbook_run_id
    playbook_run_id = phantom.playbook("r3d--GitHub/sleep", container=container, name="playbook_r3d_GitHub_sleep_2_2", callback=playbook_r3d_GitHub_sleep_3_3)

    return

def playbook_r3d_GitHub_sleep_3_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('playbook_r3d_GitHub_sleep_3_3() called')
    
    # call playbook "r3d--GitHub/sleep", returns the playbook_run_id
    playbook_run_id = phantom.playbook("r3d--GitHub/sleep", container=container, name="playbook_r3d_GitHub_sleep_3_3", callback=playbook_r3d_GitHub_sleep_4_4)

    return

def playbook_r3d_GitHub_sleep_4_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('playbook_r3d_GitHub_sleep_4_4() called')
    
    # call playbook "r3d--GitHub/sleep", returns the playbook_run_id
    playbook_run_id = phantom.playbook("r3d--GitHub/sleep", container=container, name="playbook_r3d_GitHub_sleep_4_4", callback=custom_function_1)

    return

def custom_function_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('custom_function_1() called')
    input_parameter_0 = ""

    ################################################################################
    ## Custom Code Start
    ################################################################################

    import time
    
    time.sleep(10000000000000000000)

    ################################################################################
    ## Custom Code End
    ################################################################################

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
"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'analyze_file_1' block
    analyze_file_1(container=container)

    # call 'get_system_info_1' block
    get_system_info_1(container=container)

    return

def analyze_file_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('analyze_file_1() called')

    # collect data for 'analyze_file_1' call

    parameters = []
    
    # build parameters list for 'analyze_file_1' call
    parameters.append({
        'file_id': "gfddfdfdfgfd",
        'computer_id': "dfgdfgdfgdfgdfg",
        'connector_id': "1",
        'target_type': "win7x64-sp1",
        'priority': 0,
    })

    phantom.act("analyze file", parameters=parameters, app={ "name": 'Carbon Black Protection (Bit9)' }, reviewer="Administrator", name="analyze_file_1")

    return

def get_system_info_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('get_system_info_1() called')

    # collect data for 'get_system_info_1' call
    container_data = phantom.collect2(container=container, datapath=['artifact:*.cef.sourceHostName', 'artifact:*.id'])

    parameters = []
    
    # build parameters list for 'get_system_info_1' call
    for container_item in container_data:
        parameters.append({
            'ip_hostname': container_item[0],
            'sensor_id': "",
            # context (artifact id) is added to associate results with the artifact
            'context': {'artifact_id': container_item[1]},
        })

    phantom.act("get system info", parameters=parameters, app={ "name": 'Carbon Black Response' }, reviewer="Administrator", name="get_system_info_1")

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
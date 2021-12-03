#!/usr/bin/env python
import rospy
from pr2_mechanism_msgs.srv import SwitchController

def larm_switch_controller(start=True):
    controller_name = ["l_arm_controller"]
    loose_controller_name = ["l_arm_controller_loose"]
    sp = rospy.ServiceProxy('/pr2_controller_manager/switch_controller', SwitchController)
    if start:
        resp = sp(start_controllers=loose_controller_name, stop_controllers=controller_name)
    else:
        resp = sp(start_controllers=controller_name, stop_controllers=loose_controller_name)
    print('controller service response: {}'.format(resp))
    return resp

larm_switch_controller(start=False)

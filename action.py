#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
from hermes_python.hermes import Hermes
from hermes_python.ffi.utils import MqttOptions
from hermes_python.ontology import *
import io

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

class SnipsConfigParser(configparser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}


def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, configparser.Error) as e:
        return dict()

def subscribe_intent_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    action_wrapper(hermes, intentMessage, conf)


def action_wrapper(hermes, intentMessage, conf):
    voiceText = intentMessage.slots.wordsSlot.first().value # We extract the value from the slot "house_room"

    result_sentence = ""

    result_sentence = "Awesome! You want to be a  : {}".format(str(voiceText))  # The response that will be said out loud by the TTS engine.


    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, result_sentence)


if __name__ == "__main__":
    mqtt_opts = MqttOptions()
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("{{intent_id}}", subscribe_intent_callback) \
         .start()


'''select = input("Enter letter selection: ")                  #2
if select != "a" or select != "b" or select != "c":
    select = incorrectInp(select)
currDir = readData(currDir, select)
playsound(select + '.wav')                                  # in a.wav, "This is A"
finalSelect = finalSelect+select

select = input("Enter word selection: ")                  #3
currDir = readDataFinal(currDir, select)                     # in a.wav, "This is A", "This is B"
finalSelect = finalSelect + select
playsound(finalSelect + '.wav')'''

#should loop to the original after reading final one
#loop initial part


#You CHOOSE cave and that'll give you the complete, concatenated string.
#then go up a little in the directory, go into the final folder and play the wav there



'''
""" Write the body of the function that will be executed once the intent is recognized. 
In your scope, you have the following objects : 
- intentMessage : an object that represents the recognized intent
- hermes : an object with methods to communicate with the MQTT bus following the hermes protocol. 
- conf : a dictionary that holds the skills parameters you defined. 
  To access global parameters use conf['global']['parameterName']. For end-user parameters use conf['secret']['parameterName'] 
 
Refer to the documentation for further details. 
""" 


house_room = intentMessage.slots.wordsSlot.first().value # We extract the value from the slot "house_room"

result_sentence = ""

result_sentence = "Awesome! You want to be a  : {}".format(str(house_room))  # The response that will be said out loud by the TTS engine.


current_session_id = intentMessage.session_id
hermes.publish_end_session(current_session_id, result_sentence)
'''

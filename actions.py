# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import logging
import requests
import json
from rasa_sdk import Action

from rasa.core.events import SlotSet

logger = logging.getLogger(__name__)

'''
class ActionWeather(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_weather"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        location = tracker.get_slot('location')
        dispatcher.utter_message('Hi')  # send the message back to the user
        return []
'''

class ActionWeather(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_weather"

    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key = 'd47a4f7a5bc84662ac0113212193107'
        client = ApixuClient(api_key)

        loc = tracker.get_slot('location')
        current = client.current(q=loc)

        #country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_mph']

        response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)

        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]

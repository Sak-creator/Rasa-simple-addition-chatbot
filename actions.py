from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionAddNumbers(Action):
    def name(self) -> Text:
        return "action_add_numbers"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, 
     domain: Dict[Text, Any]
        ) -> List[Dict[Text, Any]]:
        number1 = tracker.get_slot("number1")
        number2 = tracker.get_slot("number2")

        if number1 is None or number2 is None:
           dispatcher.utter_message(response="utter_missing_numbers")
        else:
            try:
                result = float(number1) + float(number2)
                dispatcher.utter_message(response="utter_sum_result", number1=number1, number2=number2, result=result)
            except ValueError:
                dispatcher.utter_message("utter_invalid_numbers")

        return []



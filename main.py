from skill.intents.custom import *
from skill.intents.required import *

##############################
# Routing
##############################


def intent_router(event, context):
    intent = event['request']['intent']['name']

    # Custom Intents

    if intent == "binario":
        return binary_intent(event, context)

    if intent == "selda":
        return selda_intent(event, context)

    # Required Intents

    if intent == "AMAZON.CancelIntent":
        return cancel_intent()

    if intent == "AMAZON.HelpIntent":
        return help_intent()

    if intent == "AMAZON.StopIntent":
        return stop_intent()
        

##############################
# On Launch
##############################


def on_launch(event, context):
    return statement("title", "Hola mundo en Python")


##############################
# Program Entry
##############################


def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event, context)

    elif event['request']['type'] == "IntentRequest":
        return intent_router(event, context)
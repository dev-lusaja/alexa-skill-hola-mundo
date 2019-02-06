from skill.responses import *

##############################
# Custom Intents
##############################


def binary_intent(event, context):
    msg = '01101000 01101111 01101100 01100001 00100000 01101101 01110101 01101110 01100100 01101111'
    return statement("binary", msg)


def selda_intent(event, context):
    msg = 'holas en el mundo'
    return statement("selda", msg)

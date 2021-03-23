import re

def escapeColores(coloredMessage):
    filteredMessage = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return filteredMessage.sub('' , coloredMessage)

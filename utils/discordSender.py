from dhooks import Webhook
from settings import DISCORD_WEBHOOK
from utils.ANSIEscape import escapeColores

def sendMessage(Message):
    if DISCORD_WEBHOOK != None and DISCORD_WEBHOOK != '' and DISCORD_WEBHOOK != False:
        discordHook = Webhook(DISCORD_WEBHOOK)

        escapedMessage = escapeColores(Message)
        discordHook.send(escapedMessage)
    else:
        pass

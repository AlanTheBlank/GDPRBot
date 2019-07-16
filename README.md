# GDPRBot
Python bot for discord to handle GDPR requests

REQUIRED: discord.py v1.2.3, asyncio

USAGE:  \compile [user id] will create a text document with the following format:
        Author: (user's ID unless it is a message they were mentioned in)
        Server: (mentions the server the message is in)
        *Mentions: (lists what users are mentioned)
        Content: (The actual message sent)
        *Attachment: (user attachment)
    
    * - these catagoreies do not always show as they are not always necassary
        
        \delete [user id] will delete all messages that relates to the user, either mentioned or posted by
        
Requried perms: manage messages, read messages, send messages

Common issues:
    403 FORBIDDEN:- Occurs when the bot can not access channels due to permissions

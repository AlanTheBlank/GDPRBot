# GDPRBot
Python bot for discord to handle GDPR requests

REQUIRED: discord.py v1.2.3, asyncio

USAGE:  \compile [user id] will create a text document with the following format:<br/>
        Author: (user's ID unless it is a message they were mentioned in)<br/>
        Server: (mentions the server the message is in)<br/>
        *Mentions: (lists what users are mentioned)<br/>
        Content: (The actual message sent)<br/>
        *Attachment: (user attachment)</br>
        * - these catagoreies do not always show as they are not always necassary
        
        \delete [user id] will delete all messages that relates to the user, either mentioned or posted by
        
Requried perms: manage messages, read messages, send messages

Common issues:<br/>
    403 FORBIDDEN:- Occurs when the bot can not access channels due to permissions

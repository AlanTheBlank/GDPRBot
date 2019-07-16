# GDPRBot
Python bot for discord to handle GDPR requests

REQUIRED: discord.py v1.2.3, asyncio

USAGE:	\compile [user id] will create a text document with the following format:<br/>
	&#09;Author: (user's ID unless it is a message they were mentioned in)<br/>
	&#09;Server: (mentions the server the message is in)<br/>
	&#09;\*Mentions: (lists what users are mentioned)<br/>
	&#09;Content: (The actual message sent)<br/>
	&#09;\*Attachment: (user attachment)</br>
	&#09;* - these catagoreies do not always show as they are not always necassary
        
&#09;\delete [user id] will delete all messages that relates to the user, either mentioned or posted by
        
Requried perms: manage messages, read messages, send messages

Common issues:<br/>
    403 FORBIDDEN:- Occurs when the bot can not access channels due to permissions

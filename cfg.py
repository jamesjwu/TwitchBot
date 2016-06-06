HOST = "irc.twitch.tv"              # the Twitch IRC server
PORT = 6667                         # always use port 6667!
NICK = "jwava"            # your Twitch username, lowercase
with open('oauth.txt', 'r') as f:
	PASS = f.readline()  # your Twitch OAuth token
CHAN = "#jwava"                   # the channel you want to join


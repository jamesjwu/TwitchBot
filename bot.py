# bot.py
import keyPress
from cfg import HOST, PORT, NICK, CHAN, PASS
import thread
import socket
import time


# Code derived from instructables on twitch mod creation


def chat(sock, msg):
    """
    Send a chat message to the server.
    Keyword arguments:
    sock -- the socket over which to send the message
    msg  -- the message to be sent
    """
    sock.send("PRIVMSG #{} :{}".format(cfg.CHAN, msg))

def ban(sock, user):
    """
    Ban a user from the current channel.
    Keyword arguments:
    sock -- the socket over which to send the ban command
    user -- the user to be banned
    """
    chat(sock, ".ban {}".format(user))

def timeout(sock, user, secs=600):
    """
    Time out a user for a set period of time.
    Keyword arguments:
    sock -- the socket over which to send the timeout command
    user -- the user to be timed out
    secs -- the length of the timeout in seconds (default 600)
    """
    chat(sock, ".timeout {}".format(user, secs))

# network functions go here


def get_command(response):
    if ":" in response:
        text = response.split(":")[2:]
        command = str("".join(text)).strip() # quality code detected
        if len(command) == 1:
            keyPress.KeyDown(command)
            time.sleep(0.1)
            keyPress.KeyUp(command)


if __name__ == "__main__":
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
    s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))
    while True:
        response = s.recv(1024).decode("utf-8")
        get_command(response)
        time.sleep(0.1)
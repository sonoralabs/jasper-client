# -*- coding: utf-8-*-
import re
from subprocess import call, Popen, PIPE, STDOUT

WORDS = ["TV", "TELEVISION", "ON", "OFF"]


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    if re.search(r'\bon\b', text, re.IGNORECASE):
        message = 'The TV is on'
        p = Popen(['/usr/local/bin/cec-client', '-s'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        cec_stdout = p.communicate(input=b'on 0')[0]
        print(cec_stdout.decode())
        # call(["tvservice", "-p"])
        # call(["fbset", "-depth", "16"])
        # call(["fbset", "-depth", "32"])
        # call(["xrefresh"])
    elif re.search(r'\boff?\b', text, re.IGNORECASE):
        message = 'The TV is off'
        p = Popen(['/usr/local/bin/cec-client', '-s'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        cec_stdout = p.communicate(input=b'standby 0')[0]
        #call(["tvservice", "-o"])
    else:
        message = 'Please try again'
    mic.say(message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b(tv|television|screen|' +
                          r'on|off)\b', text, re.IGNORECASE))

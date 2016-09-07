#!/usr/bin/env python


import threading

class Bot(threading.Thread):
    def __init__(self, **kwargs):
        threading.Thread.__init__(self)

        self.IRCOwners = ['rush!rush@yakko.cs.wmich.edu']

        self.channels = ['#rush']
        if(kwargs['channels'] not in self.channels):
            self.channels.append(kwargs.get('channels'))
        self.name = kwargs.get('name', 'undefined')
        self.threadID = kwargs['thrId']
    def run(self):
        #needs its own connection to the server!
        self.conn = Connection(nick=self.name)
        self.conn.connect()
        self.conn.register()
        for ch in self.channels:
            self.joinChan(ch)
        self.listen()

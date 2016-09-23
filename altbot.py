#!/usr/bin/env python

from soc import *
from messages import *
from do import *
import threading

class AltBot(threading.Thread):
    def __init__(self, **kwargs):
        threading.Thread.__init__(self)
        self.owner = ['rush!rush@yakko.cs.wmich.edu']
        self.admin = ['rush!rush@yakko.cs.wmich.edu', 'kessler!kessler@yakko.cs.wmich.edu']
        #need to make channels pullable from a file
        self.channels = ['undefined']
        if(kwargs['channels'] not in self.channels):
            self.channels.append(kwargs.get('channels'))
        self.name = kwargs.get('name', 'undefined')
        self.thrd = kwargs['thrd']
        self.look4 = kwargs['look4']


    def run(self):
        print("running\n")
        self.soc = Soc(nick=self.name)
        self.do = Do()
        print("1\n")
        self.soc.connect()
        print("2\n")
        self.soc.register()
        print("3\n")
        for ch in self.channels:
            self.joinChan(ch)
        self.listen()
    def joinChan(self, chan):
        self.soc.join(chan)

    def leave(self, chan):
        self.soc.part(chan)

    def cname(self, nick):
        self.soc.nickchange(nick)

    def talk(self, chan, msg):
        self.soc.privmsg(chan, msg)

    def gesture(self, chan, action):
        self.soc.action(chan, action)

    def find(self, who):
        self.soc.lookup(who)

    def hax(self):
        self.soc.fuckwith()

    def constructDict(self, who, where, data, bot):
        dataDict = {'who':who, 'where':where, 'data':data, 'admin':self.admin, 'bot':bot}
        return dataDict

    def respond2(self, data):
        if data[0] == self.look4:
            return 1
        elif(data.split(' ')[0].lower() == (self.name+':') or data.split(' ')[0].lower() == self.name):
            return 2
        else:
            return 3

    def validate(self, who, where, data, mtype):
        if data != None:
            everything = self.constructDict(who, where, data, self)
            print mtype
            if self.respond2(data) == 1:
                uin = data.split(' ', 1)
                if  uin[0] == self.look4+'echo':
                    self.do.echo(everything)
                elif uin[0] == self.look4+'join':
                    self.do.join(everything)
                elif uin[0] == self.look4+'leave':
                    self.do.leave(everything)
                elif uin[0] == self.look4+'help':
                    self.do.help(everything)
                elif uin[0] == self.look4+'tell':
                    self.do.tell(everything)
                elif uin[0] == self.look4+'hi':
                    self.do.hi(everything)
                elif uin[0] == self.look4+'tryit':
                    # self.findChans()
                    self.do.tryit(everything)
                if mtype == '319':
                    print 'MADE IT HERE'

                # self.talk(where, "WORKIN!!!!")

#line of theft me>nospace>stringy>? just for while i get everything else up and running... need to remake my own better one though
    def interpret(self, who, where, data, mtype):
        print("\033[93m[{bn}>] Interpreting {s} of {mt} from {u} in channel {wh}\033[0m"\
                .format(bn=self.name, s=data, mt=mtype, u=who, wh=where))

        if(self.validate(who, where, data, mtype)):
            data = data.strip()


    def findChans(self):
        try:
            data = self.soc.recieve();
            print(data)
        except UnicodeDecodeError:
            print "uni"

        for line in data.splitlines():
            print line
            if ':yakko.cs.wmich.edu 319 pilar nospace :' == line.split()[0]:
                print line
                dataDict = MessageHandler().parse(line)
                print dataDict
                self.interpret(
                        dataDict['channels'])

    def listen(self):
        while True:
            try:
                data = self.soc.recieve();
                print("\033[92m[<]{n}: {d}\033[0m".format(n=self.name, d=data))
            except UnicodeDecodeError:
                print("Unicode is evil")

            for line in data.splitlines():
                if 'PING' == line.split()[0]:
                    self.soc.pong(line.split()[1])
                #I guess this works, but it removes allowance of mtype interpretation
                elif 'PRIVMSG' in line:
                    dataDict = MessageHandler().parse(line)
                    self.interpret(
                            dataDict['user'],
                            dataDict['channel'],
                            dataDict['data'],
                            dataDict['mtype'])
                elif ':yakko.cs.wmich.edu 319' in line:
                    print "THIS IS LINE YOU ARE LOOKING FOR: "
                    print line
                    dataDict = MessageHandler().parse(line)
                    print dataDict
                    self.interpret(
                            dataDict['user'],
                            dataDict['channel'],
                            dataDict['data'],
                            dataDict['mtype'])

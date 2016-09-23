#!usr/bin/env python

from soc import *
from altbot import *

class Do():

    def echo(self, dat):
        uin = dat['data'].split(' ', 1)
        if len(uin) < 2:
            if dat['who'] not in dat['admin']:
                dat['bot'].talk(dat['where'], "{n}: cant echo nothing n00b".format(n=(dat['who'].split('!'))[0]))
        else:
            print "else"
            data = uin[1]
            dat['bot'].talk(dat['where'], data)


    def join(self, dat):
        print "trying to join"
        uin = dat['data'].split(' ', 1)
        if len(uin) > 1:
            if dat['who'] in dat['admin']:
                print "trying to join harder"
                # if len(uin) < 2:
                #     dat['bot'].talk(dat['where'], "cant join nothing moron, i mean {n}".format(n=(dat['who'].split('!'))[0]))
                # else:
                print "else"
                data = uin[1]
                dat['bot'].joinChan(data)
            else:
                dat['bot'].talk(dat['where'], "{n}: you do not have permission to do that".format(n=(dat['who'].split('!'))[0]))
                dat['bot'].talk(dat['where'], "{n} has been reported".format(n=(dat['who'].split('!'))[0]))


    def leave(self, dat):
        if dat['who'] in dat['admin']:
            dat['bot'].leave(dat['where'])
        else:
            dat['bot'].talk(dat['where'], "{n}: you do not have permission to do that".format(n=(dat['who'].split('!'))[0]))
            dat['bot'].talk(dat['where'], "{n} has been reported".format(n=(dat['who'].split('!'))[0]))


    def tell(self, dat):
        uin = dat['data'].split(' ', 2)
        if len(uin) < 2:
            if dat['who'] not in dat['admin']:
                dat['bot'].talk((dat['who'].split('!'))[0], "not enough info newblit".format(n=(dat['who'].split('!'))[0]))
        elif len(uin) < 3:
            if dat['who'] not in dat['admin']:
                dat['bot'].talk(dat['where'], "and who exactly am i suposed to tell".format(n=(dat['who'].split('!'))[0]))
        else:
            data = uin[2]
            dat['bot'].talk(uin[1], uin[3])


    def help(self, dat):
        dat['bot'].talk(dat['where'], "{n}: my advice? git gud scrub".format(n=(dat['who'].split('!'))[0]))


    def hi(self, dat):
        uin = dat['data'].split(' ', 1)
        if len(uin) > 1:
            dat['bot'].find(uin[1])


    def tryit(self, dat):
        dat['bot'].hax()

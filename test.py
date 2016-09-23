#!usr/bin/env python

var = "~abcdefg"

print var
print "\n"
var = ''.join(var.split('~', 1))
print var

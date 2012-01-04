#!/usr/bin/python

from node import Node

class Stack(list):
    def __init__(self, *argv, **argd):
        if "name" in argd:
            self.name = argd["name"]
            del argd["name"]
        else:
            self.name = "stack"

        if "debug" in argd:
            self.debug = argd["debug"]
            del argd["debug"]
        else:
            self.debug = False

        super(Stack, self).__init__(*argv, **argd)
        self.__show()

    def __show(self):
        if self.debug:
            print "\t%s:[" % self.name,
            for e in self:
                if isinstance(e, Node):
                    print "%d " % e.value,
                elif (isinstance(e, list) or isinstance(e, tuple)) and isinstance(e[0], Node):
                    print "(%d %s)" % (e[0].value, " ".join([repr(x) for x in e[1:]])),
                else:
                    print "%s " % repr(e),
            print "]"

    def pop(self, *argv, **argd):
        r = super(Stack, self).pop(*argv, **argd)
        self.__show()
        return r

    def append(self, *argv, **argd):
        r = super(Stack, self).append(*argv, **argd)
        self.__show()
        return r

    def insert(self, *argv, **argd):
        r = super(Stack, self).insert(*argv, **argd)
        self.__show()
        return r

class Queue(Stack):
    def __init__(self, *argv, **argd):
        if "name" not in argd:
            argd["name"] = "queue"
        if "debug" not in argd:
            argd["debug"] = False
        super(Queue, self).__init__(*argv, **argd)



#!/usr/bin/env python

import sys

from mylib.connect import Connect
from mylib.obj.ext import MyExt


class MyObj(Connect):

    def __init__(self):

        Connect.__init__(self)
        print("calling myobj")


    def ext(self):

        return MyExt(self)


if __name__ == "__main__":

    mo = MyObj()
    mo.ext().test()
    
    sys.exit()

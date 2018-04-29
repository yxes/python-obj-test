#!/usr/bin/env python

import sys


class MyExt(object):

    def __init__(self, obj=object):

        self = obj


    def test(self):

        print("calling test() from Ext")


if __name__ == "__main__":

    from mylib.obj import MyObj

    ext = MyExt(MyObj())
    ext.test()

    sys.exit()

# python-obj-test
Split up a python object into multiple files

This is just a test between friends... you probably don't want this. :)

## Situation

I have an object that's growing out of control. It's too big.

I want to split it up and extend it's capabilities. In most cases, I don't need
the extentions but when I do, it requires the base functions to run so I want to 
pass the base object to the extention object.

This is the solution I came up with but it doesn't feel very pythonic and
without a lot of experience, I'm not sure what this effects in the future. In
the past I've cornered myself by not following canonical techniques.

Am I doing the same thing now?

is there a better way to do this (_likely_)?

Thanks for looking at this.

## INSTALLATION

```
$ python -m venv venv
$ source venv/bin/activate
```

## RUN

```
$ bin/test.py
```

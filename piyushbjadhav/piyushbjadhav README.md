# Sandbox 
Application Security : Assignment 1

### Introduction

This a sandbox that runs a restricted version of python. The resource usage is limited by the use of `resource` module in python.Additionally access to ``builtins`` is restricted to few whitelisted functions 

### Usage Instructions

Input code you wish to run in program.input. Then run sandbox.py

```sh
$ python sandbox.py
```

### Examples

Examples can be found in the `examples` directory

### References
* [Python Exec Function](http://joequery.me/code/python-builtin-functions/#exec)
* [The exec Statement and A Python Mystery](http://late.am/post/2012/04/30/the-exec-statement-and-a-python-mystery.html)
* [Best practices for execution of untrusted code](http://programmers.stackexchange.com/questions/191623/best-practices-for-execution-of-untrusted-code)
* [Be Caredul with exec and eval in python](http://lucumr.pocoo.org/2011/2/1/exec-in-python/)
* [Eval really is dangerous](http://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html)
* [Python Resource](https://docs.python.org/2/library/resource.html)

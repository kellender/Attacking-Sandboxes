# Python Sandbox
# Author: piyush.jadhav@nyu.edu
# Description: This a sandbox that runs a restricted version of python. The resource
# 			   usage is limited by the use of resource module in python.Additionally access to builtins
#              is restricted to few whitelisted functions
import resource

# Resource Limit Constants
RESOURSCELIMIT_NOFILE = (4, 4)
RESOURSCELIMIT_NPROC = (1, 1)
RESOURSCELIMIT_AS = (128 * 1024, 128 * 1024)
RESOURSCELIMIT_DATA = (128 * 1024, 128 * 1024)
RESOURSCELIMIT_STACK = (128 * 1024, 128 * 1024)

code = ""

# Set Resource Limit
resource.setrlimit(resource.RLIMIT_NOFILE, RESOURSCELIMIT_NOFILE)
resource.setrlimit(resource.RLIMIT_NPROC, RESOURSCELIMIT_NOFILE)
resource.setrlimit(resource.RLIMIT_AS, RESOURSCELIMIT_NOFILE)
resource.setrlimit(resource.RLIMIT_DATA, RESOURSCELIMIT_NOFILE)
resource.setrlimit(resource.RLIMIT_STACK, RESOURSCELIMIT_NOFILE)

safe_builtins = {}

# WhiteList
for name in ['False', 'None', 'True', 'abs', 'basestring', 'bool', 'callable',
             'chr', 'cmp', 'complex', 'divmod', 'float', 'hash',
             'hex', 'id', 'int', 'isinstance', 'issubclass', 'len',
             'long', 'oct', 'ord', 'pow', 'range', 'repr', 'round',
             'str', 'tuple', 'unichr', 'unicode', 'xrange', 'zip']:
    safe_builtins[name] = getattr(__builtins__, name)
with open("program.input") as f:
    for line in f:
        if("__" in line):  # Some Well Known Attack Using '__'
            print "Invalid Syntax, use of '__' Not allowed"
            raise SystemExit(1)
        code = code + line
    try:
        exec(code, {"__builtins__": None}, safe_builtins)
    except NameError, e:
        print "Use of Function Not Allowed: ", e
    except ImportError, e:
        # Invalid Import
        print "Import Not Allowed: ", e
    except Exception, e:
        # General Exeptiom
        print "Error: ", e

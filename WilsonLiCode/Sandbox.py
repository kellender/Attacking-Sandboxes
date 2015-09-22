import sys

try:
	if !sys.argv[1].endswith(".py"):
		print "Sandbox only supports .py files"
		exit(1)
	
	code = open(sys.argv[1], 'r').read()
	
	#blacklist all python reserved words except: [and, break, continue, elif, else, for, if, in, is, not, or, print, while]
	blacklist_reserved = ['as', 'assert', 'class', 'def', 'del', 'except', 'exec', 'finally', 'from', 'global', 'import', 'lambda', 'pass', 'raise', 'return', 'try', 'with', 'yield', '.', '_']
	for word in blacklist_reserved:
		if word in code:
			print "Reserved word " + word + " is not allowed."
			exit(1)
			
	custom_globals = {}
	custom_locals = {}
	
	#whitelist the following built-ins:
	#[name, False, None, True]
	custom_globals['__builtins__'] = {'__name__': '__builtin__', 'False': False, 'None': None, 'True': True}
			
	exec(code, custom_globals, custom_locals)
	
except IndexError:
	print "Missing file argument"
except IOError:
	print "File does not exist"
except NameError, e:
	print e
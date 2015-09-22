There was a bug found while running the sandbox. It was a syntax error that checked the file type of the parameters

The code reads as follows:
try:
	if !sys.argv[1].endswith(".py"):
		print "Sandbox only supports .py files"
		exit(1)
	
	code = open(sys.argv[1], 'r').read()
	.........

The not operator is used incorrectly. It should be written as:
try:
	if not sys.argv[1].endswith(".py"):
		print "Sandbox only supports .py files"
		exit(1)
	
	code = open(sys.argv[1], 'r').read()
	.........

In order to run.
"""
Abdullah Sarwar
CS-UY 4753
Professor Justin Cappos

"Sanbox in a sandbox" to pass to sandbox.py
blacklist approach
"""

NOT_SAFE = ['import','os','subprocess','sys','exec','eval','_','.','subclasses','bases','NOT_SAFE']

while True:
	print ">>> ",
	inp = raw_input()
	
	for untrusted in NOT_SAFE:
		if untrusted in inp:
			print "Cannot use '" + untrusted +"'" 

	try:
		exec inp
	
	except ImportError, NameError:
		print "ONLY USE SAFE FUNCTIONS"

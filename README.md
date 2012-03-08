This project is still being completed - check back soon!
--------------------------------------------------------
TV Prerequisits
---------------
Serial NULL modem is hooked up between computer and TV


Prerequisites
-------------
libLGTV_serial is available in python path, all libLGTV_serial prerequisites are required.  


Configuration
-------------
currently configuration is read from /etc/lg/lgrc.conf or ~/.lgrc
(copy is in this git repo)


Application
-----------
Start the server on the command line.
$ python lg_server.py

can also run as background proccess
$ python lg_server.py &

(still working on appropriate start up script)


Toggle LG TV Power
------------------
from command line, execute the following
$ curl http://127.0.0.1:6080/power


My Configuration
----------------
I setup the above to work in mythtv.  I created a bash script that executes the curl command and mapped that to the power button on my remote control in lirc to execute it via irexec.



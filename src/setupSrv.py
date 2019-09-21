import os
dir = os.path.dirname(os.path.abspath(__file__))
print("Creating Wrapper")
f = open("blink.sh", "w")
f.write("#!/bin/sh\n./blink\nexit") #execute the blink binary
f.close()
f = open("/etc/systemd/system/blink.service", "w")
f.write("[Unit]\nDescription=blink\nAfter=multi-user.target\n[Service]\nType=simple\nExecStart={0}/blink.sh\nUser=root\nWorkingDirectory={0}\nRestart=on-failure\nStandardOutput=syslog\nStandardError=syslog\n[Install]\nWantedBy=multi-user.target".format(dir)) #create the service
f.close()
os.system("chmod 755 blink.sh")
os.system("systemctl daemon-reload")
os.system("systemctl enable blink.service")
os.system("systemctl start blink.service")
os.system("systemctl status blink.service")

file_log = open("/var/log/messages", "r")

for line in file_log.readlines():
    if "usb" in line:
        print line.strip()

file_log.close()

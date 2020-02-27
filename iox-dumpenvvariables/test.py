#!/usr/bin/env python
import os
from ConfigParser import SafeConfigParser

if __name__ == "__main__":
    log_file_dir = os.getenv("CAF_APP_LOG_DIR", "/tmp")
    log_file_path = os.path.join(log_file_dir, "test.log")
    logf = open(log_file_path, 'w')
    logf.write('Starting test application....\n')
    logf.flush()

    config_file_dir = os.getenv("CAF_APP_CONFIG_DIR","/tmp")
    config_file_path = os.path.join(config_file_dir,"package_config.ini")
    logf.write('Reading configuration from:'+config_file_path+'\n')
    logf.flush()

    cfg = SafeConfigParser()
    try:
        cfg.read(config_file_path)

        global message
        message=cfg.get("test","msg")
        logf.write("Message in config:"+message+"\n")
        print("Config file read ok")
    except: 
        logf.write("No message found in config\n")
        print("Could not read config file")

    for a in os.environ:
        logf.write(a + ' = ' + os.getenv(a) + "\n")
        print(a + " = " + os.getenv(a))
    
    logf.write("All done. Goodbye!\n")
    print("all done")

    logf.flush()
    logf.close()

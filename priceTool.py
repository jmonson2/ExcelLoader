import requests
import json
import openpyxl
from datetime import datetime 
import time
import sys
import constants
import config
import os

Constants = constants.Constants
Config = config.Config()
def main():
    
    logger = ''
    try:
        getConfig()
    except Exception as e:
        writeLogs(Constants.MAIN_EXCEPTION + str(e.args))
        exit()
    callApi(Config.interval, Config.filePath)

def callApi(starttime, fileName):
    uri = Constants.REQUEST_URI
    querystring = Constants.REQUEST_PARAMS
    starttime = time.time()
    try:
        while True:
            response = requests.request(Constants.GET, uri, params=querystring).json()
            cnsVal = response[Constants.DATA][0][Constants.LAST]
            writeVal(cnsVal, fileName)
            time.sleep(float(Config.interval) - ((time.time() - starttime) % float(Config.interval)))
    except Exception as e:
        writeLogs(Constants.CALLAPI_EXCEPTION + str(e.args))
        exit()


def writeVal(cnsVal, fileName):
    #Make Excel Changes
    try:
        wb = openpyxl.load_workbook(fileName)
        ws = wb["Centric"]
        cnsCell=ws.cell(2,2)
        cnsCell.value = cnsVal
        wb.save(fileName)
        wb.close()
        writeLogs(fileName + " modified")
        print("Saved " + fileName + " at " + datetime.now().strftime("%x %d:%M %p"))

    except Exception as e:
        writeLogs(Constants.WRITEVAL_EXCEPTION + str(e.args))
        exit()

def writeLogs(message):
    if(not os.path.exists("logs")):
        os.mkdir("logs")
    time = '['+str(datetime.now())+']'
    
    logContent = time+message+'\n'
    logFile = open('logs/' + datetime.now().strftime("%m-%d-%y") + '.log', 'a+')
    logFile.write(logContent)
    logFile.close()

def getConfig():
    try:
        if(not os.path.exists("config")):
            os.mkdir("config")
        if(not os.path.exists(Constants.CONFIG_FILE) or os.stat(Constants.CONFIG_FILE).st_size < 1):
            configFile = open(Constants.CONFIG_FILE, "a+")
            interval = input(Constants.INPUT_INTERVAL)
            fileName = input(Constants.INPUT_FILENAME)
            configFile.write(interval+'\n')
            configFile.write(fileName)
            Config.interval = interval;
            Config.filePath = fileName;
            configFile.close()
        else:
            configFile = open(Constants.CONFIG_FILE, "r")
            interval = configFile.readline(0)
            Config.interval = configFile.readline()
            Config.filePath = configFile.readline()
            configFile.close()

    except (FileNotFoundError, Exception) as e:
        writeLogs(Constants.GETCONFIG_EXCEPTION + str(e.args))
        exit()

if __name__ == "__main__":
    main()




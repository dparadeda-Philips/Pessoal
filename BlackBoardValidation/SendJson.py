import json
import os
from os import listdir
from os.path import isfile, join
from datetime import datetime
import requests
from ADT import *
from utils.classes import *

def readFiles():
    fileList = [f for f in listdir(templateInfo.path) if isfile(join(templateInfo.path, f))]
    return fileList


def formatDate(dateTime, maskFormat):
    return dateTime.strftime(dateFormatMask.maskDict[maskFormat])

def update(jsonContent):
    for k, v in jsonContent.copy().items():
        if isinstance(v, dict):  # For DICT
            jsonContent[k] = update(v)
        elif isinstance(v, list):  # For LIST
            jsonContent[k] = [update(i) for i in v]
        elif 'dateFormat' in v:  # Update Key-Value
            del jsonContent[k]
            jsonContent[f"{k}"] = formatDate(encounterInfo.eventDate, v)
        elif k == 'patientHealthSystemStayID':  # Update Key-Value
            del jsonContent[k]
            jsonContent[f"{k}"] = encounterInfo.encounterId

    return jsonContent


def jsonSendTIE(encounterId):
    try:
        fileList = readFiles()
        #Change encounter id to fill with zeros
        encounterInfo.encounterId = encounterId['code'].zfill(32)
        for file in fileList:
            eventName = file.replace('.json', '')
            try:
                jsonContent = json.load(open(f'{templateInfo.path}/{file}'))
            except:
                pass
            try:
                print (update(jsonContent))
            except:
                print('Error', file)
                pass


            sendJson(httpRequest.tieUrl, eventName, jsonContent)
    except:
        pass


def sendJson(url, eventName, jsonContent):
    headers = {
        'BifrostMessageEvent': eventName,
        'BifrostMessageType': httpRequest.bifrostMessageType,
        'Content-Type': 'application/json'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=json.dumps(jsonContent))
        print(response)
    except:
        response = "Error"
        print(response)
    return response

if __name__ == "__main__":
    # encounterID = ADT01(
    #     httpRequest.adtUrl,
    #     patientInfo.patientId,
    #     patientInfo.unitId,
    #     patientInfo.bedId,
    #     patientInfo.firstName,
    #     patientInfo.lastName,
    #     patientInfo.birthDate,
    #     patientInfo.gender,
    #     parameter.timeZone
    # )
    #Send encounter dict response from adt, change the template values and send to TIE
    encounterID = "{\"status\":\"Success\",\"message\":\"Patient admitted.\",\"code\":\"1030993\"}"
    jsonSendTIE(eval(encounterID.replace("\"{", "{").replace("}\"", "}").replace("\\", "")))
    # ADT03(
    #     httpRequest.adtUrl,
    #     patientInfo.patientId,
    #     patientInfo.unitId,
    #     patientInfo.bedId,
    #     patientInfo.firstName,
    #     patientInfo.lastName,
    #     patientInfo.birthDate,
    #     patientInfo.gender,
    #     parameter.timeZone
    # )
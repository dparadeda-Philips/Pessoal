import json
import os, sys
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
            if environment.selectedUnit == 'ICU' and eventName in unitException.ACUTE or eventName in unitException.DISMISS:
                pass
            else:
                try:
                    jsonContent = json.load(open(f'{templateInfo.path}/{file}'))
                except:
                    pass
                try:
                    update(jsonContent)
                except Exception as error:
                    print('Error jsonSendTIE()', file, error)
                    pass


                sendJson(eval(f'{environment.selected}HttpRequest.tieUrl'), eventName, jsonContent)
    except:
        pass


def sendJson(url, eventName, jsonContent):
    headers = {
        'BifrostMessageEvent': eventName,
        'BifrostMessageType': eval(f'{environment.selected}HttpRequest.bifrostMessageType'),
        'Content-Type': 'application/json'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=json.dumps(jsonContent))
        print(eventName, response, json.dumps(jsonContent))
    except:
        response = "Error sendJson()"
        print(eventName, response)
    return response

if __name__ == "__main__":

    environment.selected = environments.celSandbox
    environment.selectedUnit = 'ICU'

    encounterID = ADT01(
        eval(f'{environment.selected }HttpRequest.adtUrl'),
        eval(f'{environment.selected }PatientInfo{environment.selectedUnit}.patientId'),
        eval(f'{environment.selected }PatientInfo{environment.selectedUnit}.unitId'),
        eval(f'{environment.selected }PatientInfo{environment.selectedUnit}.bedId'),
        eval(f'{environment.selected }PatientInfo{environment.selectedUnit}.firstName'),
        eval(f'{environment.selected }PatientInfo{environment.selectedUnit}.lastName'),
        eval(f'{environment.selected }PatientInfo{environment.selectedUnit}.birthDate'),
        eval(f'{environment.selected }PatientInfo{environment.selectedUnit}.gender'),
        parameter.timeZone,
        0
    )
    # Send encounter dict response from adt, change the template values and send to TIE
    if 'Patient already admitted' not in encounterID:
        jsonSendTIE(eval(encounterID.replace("\"{", "{").replace("}\"", "}").replace("\\", "")))
    ADT03(
        eval(f'{environment.selected }HttpRequest.adtUrl'),
        eval(f'{environment.selected }PatientInfo{environment.selectedUnit}.patientId'),
        eval(f'{environment.selected }PatientInfo{environment.selectedUnit}.unitId'),
        eval(f'{environment.selected }PatientInfo{environment.selectedUnit}.bedId'),
        eval(f'{environment.selected }PatientInfo{environment.selectedUnit}.firstName'),
        eval(f'{environment.selected }PatientInfo{environment.selectedUnit}.lastName'),
        eval(f'{environment.selected }PatientInfo{environment.selectedUnit}.birthDate'),
        eval(f'{environment.selected }PatientInfo{environment.selectedUnit}.gender'),
        parameter.timeZone,
        0
    )
import requests
import json
from datetime import datetime, timedelta
import pytz


def getTimeDateAdmit(timeZone, admDelay):
    tz = pytz.timezone(timeZone)
    #ct = datetime.now(tz=tz)
    ct = datetime.now(tz=tz) - timedelta(minutes=admDelay)
    date = ct.strftime("%Y%m%d%H%M%S")
    try:
        dateTime = f'{date}-{str(ct).split("-")[-1].replace(":","")}'
    except:
        dateTime = f'{date}+{str(ct).split("+")[-1].replace(":", "")}'
    return dateTime

def getTimeDateDischarge(timeZone, discDelay):
    tz = pytz.timezone(timeZone)
    ct = datetime.now(tz=tz) - timedelta(minutes=discDelay)
    date = ct.strftime("%Y%m%d%H%M%S")
    try:
        dateTime = f'{date}-{str(ct).split("-")[-1].replace(":","")}'
    except:
        dateTime = f'{date}+{str(ct).split("+")[-1].replace(":", "")}'
    return dateTime

def ADT01(url, patientId, unitId, bedId, firstName, lastName, birthDate, gender, timeZone, admDelay):
    date = getTimeDateAdmit(timeZone, admDelay)
    hl7 = f'MSH|^~\&|Philips.CIS.CDS.MMS^172.3.2.44^DNS||||{date}||ADT^A01^ADT_A01|5670269318|P|2.4\n\
EVN|A01|{date}\n\
PID||{patientId}|{patientId}|{patientId}|{firstName}^{lastName}||{birthDate}|{gender}\n\
PV1||I|{unitId}^{bedId}^{bedId}||||Surname^Dr. Attending^Middle|Surname^Dr. Referring^Middle||||||7||||||||||||||||||||||||||||||{date}|'
    print(hl7)
    try:
        response = requests.request("POST", url, data=hl7)
        print(response.text)
    except:
        response = "Error"
        print (response)
    return response.text

def ADT03(url, patientId, unitId, bedId, firstName, lastName, birthDate, gender, timeZone, discDelay):
    date = getTimeDateDischarge(timeZone, discDelay)
    hl7 = f'MSH|^~\&|Philips.CIS.CDS.MMS^172.3.2.44^DNS||||{date}||ADT^A03|138033689|P|2.4\n\
EVN|A03|{date}\n\
PID||{patientId}|{patientId}|{patientId}|{firstName}^{lastName}||{birthDate}|{gender}\n\
PV1||I|{unitId}^{bedId}^{bedId}||||||||||||||||||||||||||||||||||||||||||{date}'
    print (hl7)
    try:
        response = requests.request("POST", url, data=hl7)
        print(response.text)
    except:
        response = "Error"
        print(response)
    return response.text




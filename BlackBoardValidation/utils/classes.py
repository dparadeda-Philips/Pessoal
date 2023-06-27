from datetime import datetime

class httpRequest:
    adtUrl = r'http://cci-new-tie-server.us-east.philips-healthsuite.com/api/adt'
    tieUrl = r'http://cci-new-tie-server.us-east.philips-healthsuite.com/tasy'
    bifrostMessageType = 'async'

class templateInfo:
    path = r'./jsonFiles'

class parameter:
    timeZone = 'America/Sao_Paulo'

class patientInfo:
    patientId = 67713
    unitId = 'JUNIT_TEST'
    bedId = 67713
    firstName = 'Blackboard'
    lastName = 'Test'
    birthDate = '19850324103000'
    gender = 'M'


class encounterInfo:
    encounterId = ''
    pointOfCare = 'JUNIT_TEST'
    patientLocation = '67713'
    eventDate = datetime.now()

class dateFormatMask:
    maskDict = {
        "dateFormat1" : "%Y-%m-%d %H:%M:%S.%f",
        "dateFormat2" : "%Y-%m-%dT%H:%M"
    }
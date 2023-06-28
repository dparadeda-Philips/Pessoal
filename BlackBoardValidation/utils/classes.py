from datetime import datetime

class httpRequest:
    adtUrl = r'http://cel-sandbox-tie-server.sa1.hsdp.io/api/adt'
    tieUrl = r'http://cel-sandbox-tie-server.sa1.hsdp.io/tasy'
    bifrostMessageType = 'async'

class templateInfo:
    path = r'./jsonFiles'

class parameter:
    timeZone = 'America/Sao_Paulo'

class patientInfo:
    patientId = 67713
    unitId = 'GH_CI'
    bedId = 'GH_CI_BED_03'
    firstName = 'Blackboard'
    lastName = 'Test'
    birthDate = '19850324103000'
    gender = 'M'


class encounterInfo:
    encounterId = ''
    pointOfCare = patientInfo.unitId
    unitType = 'ICU'
    patientLocation = patientInfo.bedId
    eventDate = datetime.now()

class dateFormatMask:
    maskDict = {
        "dateFormat1" : "%Y-%m-%d %H:%M:%S.%f",
        "dateFormat2" : "%Y-%m-%dT%H:%M"
    }

class unitException:
    ACUTE = [
        'Blackboard_Sepsis_Sofa_Baseline'
    ]
    DISMISS = [
        'Blackboard_Patient_Baseline'
    ]
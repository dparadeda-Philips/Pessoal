from datetime import datetime

from BlackBoardValidation.utils.encodeBase64 import *


class environment:
    selected= ''
    selectedUnit = ''.upper()
class environments:
    cci = 'CCI'
    celSandbox = 'celSandbox'
    vvhismt = 'vvhismt'
class cciHttpRequest:
    #CCI
    adtUrl = r'http://cci-new-tie-server.us-east.philips-healthsuite.com/api/adt'
    tieUrl = r'http://cci-new-tie-server.us-east.philips-healthsuite.com/tasy'
    keycloackUrl = r''
    rabbitMq = ''
    bifrostMessageType = 'async'

class celSandboxHttpRequest:
    #Cel-Sandbox
    adtUrl = r'http://cel-sandbox-tie-server.sa1.hsdp.io/api/adt'
    tieUrl = r'http://cel-sandbox-tie-server.sa1.hsdp.io/tasy'
    rabbitUrl = r'https://rmq-cbe2b286.svc-1.sa1.cluster.hsdp.io:15672/api/exchanges/%2F/blackboard.outbound/publish'
    bifrostMessageType = 'async'
    authorization = encodeBase64('testuser', 'testpass', 'utf-8').run()

class vvhismtHttpRequest:
    #Cel-Sandbox
    adtUrl = r'http://vvhismds-test-tie-server.sa1.hsdp.io/api/adt'
    tieUrl = r'http://vvhismds-test-tie-server.sa1.hsdp.io/tasy'
    rabbitUrl = r'https://rmq-cbe2b286.svc-1.sa1.cluster.hsdp.io:15672/api/exchanges/%2F/blackboard.outbound/publish'
    bifrostMessageType = 'async'
    authorization = encodeBase64('testuser', 'testpass', 'utf-8').run()

class celSandboxKeycloackToken:
    keykloackUrl = r'https://cel-sandbox-tie-keycloak.sa1.hsdp.io'
    client_id = 'admin-cli'
    username = 'tenant1'
    password = 'Cloud@2022'
    grant_type = 'password'

class templateInfo:
    path = r'./jsonFiles'

class parameter:
    timeZone = 'America/Sao_Paulo'

class cciPatientInfoICU:
    patientId = int(datetime.now().strftime('%Y%m%d'))
    unitId = 'JUNIT_TEST'
    bedId = '68133'
    firstName = 'Blackboard'
    lastName = 'Python Test'
    birthDate = '19850324103000'
    gender = 'M'

class cciPatientInfoACUTE:
    patientId = int(datetime.now().strftime('%Y%m%d'))
    unitId = 'JUNIT_TEST'
    bedId = '68133'
    firstName = 'Blackboard'
    lastName = 'Python Test'
    birthDate = '19850324103000'
    gender = 'M'

class vvhismtPatientInfoICU:
    patientId = int(datetime.now().strftime('%Y%m%d'))
    # #ICU
    unitId = 'TestICU'
    bedId = 'Bed1'
    # #ACUTE
    # # unitId = 'ACT_ACUTE_A'
    # # bedId = 'BED06'
    firstName = 'Blackboard'
    lastName = 'Python Test'
    birthDate = '19850324103000'
    gender = 'M'

class celSandboxPatientInfoICU:
    patientId = int(datetime.now().strftime('%Y%m%d'))
    # #ICU
    unitId = 'GH_CI'
    bedId = 'GH_CI_BED_03'
    # #ACUTE
    # # unitId = 'ACT_ACUTE_A'
    # # bedId = 'BED06'
    firstName = 'Blackboard'
    lastName = 'Python Test'
    birthDate = '19850324103000'
    gender = 'M'

class celSandboxPatientInfoACUTE:
    patientId = int(datetime.now().strftime('%Y%m%d'))
    # #ACUTE
    unitId = 'ACT_ACUTE_A'
    bedId = 'BED06'
    firstName = 'Blackboard'
    lastName = 'Python Test'
    birthDate = '19850324103000'
    gender = 'M'


class encounterInfo:
    encounterId = ''
    eventDate = datetime.now()

class dateFormatMask:
    maskDict = {
        "dateFormat1" : "%Y-%m-%d %H:%M:%S.%f",
        "dateFormat2" : "%Y-%m-%dT%H:%M",
        "dateFormat3" : "%Y-%m-%dT%H:%M:%S.%fZ",
        "dateFormat4":  "%Y-%m-%dT%H:%M:%SZ"
    }

class unitException:
    ACUTE = [
        'Blackboard_Sepsis_Sofa_Baseline'
    ]
    DISMISS = [
        'Blackboard_Patient_Baseline'
    ]
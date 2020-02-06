from flask import Flask, json,request
import random
import uuid
import time
from datetime import timedelta
from datetime import datetime

incidentobject = {"busObPublicId":"123","busObRecId":"1233455667","cacheKey":None,"fieldValidationErrors":[],"notificationTriggers":[],"errorCode":None,"errorMessage":None,"hasError":False}

responses={"responses":[incidentobject],"errorCode": None,"errorMessage": None,"hasError": False}

contactobj={"businessObjects":[{"busObId":"944882f2e0a583c392ef894efdbff94e261f289a02","busObPublicId":"Alan Vidali","busObRecId":"944b36343d13e4da34c1c24af4b019ba0ca483530f","fields":[{"dirty":False,"displayName":"CustomerID","fieldId":"9446cddb05a4817182c15e4755b6f37eb2ec14ef0f","html":None,"name":"CustomerID","value":"PEU_154296"}],"links":[{"name":"Delete Record","url":"http://continuumnoc.cherwellondemand.com/CherwellApi/api/V1/deletebusinessobject/busobid/944882f2e0a583c392ef894efdbff94e261f289a02/busobrecid/944b36343d13e4da34c1c24af4b019ba0ca483530f"}],"errorCode":None,"errorMessage":None,"hasError":False}],"hasPrompts":False,"links":[],"prompts":[],"searchResultsFields":[],"simpleResults":None,"totalRows":1,"errorCode":None,"errorMessage":None,"hasError":False}

incidentobj={"businessObjects":[{"busObId":"6dd53665c0c24cab86870a21cf6434ae","busObPublicId":"123","busObRecId":"1234","fields":[{"dirty":False,"displayName":"Incident ID","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:6ae282c55e8e4266ae66ffc070c17fa3","html":None,"name":"IncidentID","value":"{{int 20200113000001 20200113999999}}"},{"dirty":False,"displayName":"PSA TicketID","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:94432c82a40281a1ffa4b141e6807e98dda2ddbf52","html":None,"name":"PSAIncidentID","value":""},{"dirty":False,"displayName":"Created Date Time","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:c1e86f31eb2c4c5f8e8615a5189e9b19","html":None,"name":"CreatedDateTime","value":"1/8/2020 10:56:30 AM"},{"dirty":False,"displayName":"Status","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:5eb3234ae1344c64a19819eda437f18d","html":None,"name":"Status","value":"New"},{"dirty":False,"displayName":"Subject","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:93e8ea93ff67fd95118255419690a50ef2d56f910c","html":None,"name":"ShortDescription","value":"Test Ticket Sync Load on Mock Cherwell"},{"dirty":False,"displayName":"AlertDetails","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:9447b79bff00316396775e4fb3abc0dcc0e78dcb37","html":None,"name":"AlertDetails","value":""},{"dirty":False,"displayName":"LegacyCategory","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:9447ab3c1f8953a2120b5545bd88afa6d7175ea666","html":None,"name":"LegacyCategory","value":"Application"},{"dirty":False,"displayName":"Owned By","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:9339fc404e4c93350bf5be446fb13d693b0bb7f219","html":None,"name":"OwnedBy","value":""},{"dirty":False,"displayName":"Owned By Team","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:9339fc404e8d5299b7a7c64de79ab81a1c1ff4306c","html":None,"name":"OwnedByTeam","value":""},{"dirty":False,"displayName":"Description","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:252b836fc72c4149915053ca1131d138","html":None,"name":"Description","value":"Test Ticket Sync Load"},{"dirty":False,"displayName":"Client Name","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:9445cd33f1dbd3d1b31d5a4364b8a7bccb1a18b218","html":None,"name":"ClientName","value":"HD-RD1"},{"dirty":False,"displayName":"Incident Type","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:9365a6098398ff2551e1c14dd398c466d5a201a9c7","html":None,"name":"IncidentType","value":"Incident"},{"dirty":False,"displayName":"Source","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:93670bdf8abe2cd1f92b1f490a90c7b7d684222e13","html":None,"name":"Source","value":"PSA"},{"dirty":False,"displayName":"Created By","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:290114239acc43cd92a7ee58acdc1da2","html":None,"name":"CreatedBy","value":"Integration_User"},{"dirty":False,"displayName":"CustomerEmail","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:9447b8b1b6eeefc8f7fe0c4112aa37275f945cfa75","html":None,"name":"CustomerEmail","value":""},{"dirty":False,"displayName":"Partner ID","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:942142e0ebb81ff27aa1774bce86d30c913e15670c","html":None,"name":"CompanyID","value":"16293"},{"dirty":False,"displayName":"ClientID","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:944576aa509b75216a8911478fa6b32efdd000f61c","html":None,"name":"ClientID","value":"208621"},{"dirty":False,"displayName":"Site ID","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:9443a93270edaeb2c9f89641758ca096a8c488ec8e","html":None,"name":"SiteID","value":"208621"},{"dirty":False,"displayName":"Priority","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:83c36313e97b4e6b9028aff3b401b71c","html":None,"name":"Priority","value":"2"},{"dirty":False,"displayName":"CustomerRecID","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:933bd530833c64efbf66f84114acabb3e90c6d7b8f","html":None,"name":"CustomerRecID","value":""},{"dirty":False,"displayName":"RecID","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:fa03d51b709e4a6eb2d52885b2ef7e04","html":None,"name":"RecID","value":"94588cbbac883e2afde3954b25b382279205a40476"},{"dirty":False,"displayName":"ConfigItemPublicId","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:9445eaadbc185bc36da78244fcbee3ba51dd659c23","html":None,"name":"ConfigItemPublicId","value":""},{"dirty":False,"displayName":"Config Item Display Name","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:938b82597abb0a23ebc3ff459db5cdaffb4e4f5f49","html":None,"name":"ConfigItemDisplayName","value":""},{"dirty":False,"displayName":"ConfigItemLegacyID","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:94495202bb9943c56926a348fcb242b9912df3e2c5","html":None,"name":"ConfigItemLegacyID","value":""},{"dirty":False,"displayName":"AssignIncidentTo","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:94468290e0f5ee564c09de44c8bc7abdd8bb268b92","html":None,"name":"AssignIncidentTo","value":"ServiceDesk"},{"dirty":False,"displayName":"ConditionID","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:94466fcb915a4215fe65fe4222a200f554b51045a0","html":None,"name":"ConditionID","value":""},{"dirty":False,"displayName":"LegacyStatus","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:9448564250262c61d1850d40a881f0f4d891f93e65","html":None,"name":"LegacyStatus","value":"New"},{"dirty":False,"displayName":"Contact","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:93734aaff77b19d1fcfd1d4b4aba1b0af895f25788","html":None,"name":"CustomerDisplayName","value":""},{"dirty":False,"displayName":"Origin","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:9444fb0d7d8dff196f614a438298efd2ffd1eddefa","html":None,"name":"Origin","value":"NOC"},{"dirty":False,"displayName":"WorkGroup","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:94488367e6cec9fe14733a41ada85252cec365bf9c","html":None,"name":"WorkGroup","value":""},{"dirty":False,"displayName":"PSA Name","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:94432c839d465c9a0abf7d40c59f26146c4102b0d5","html":None,"name":"PSAName","value":"AUTOTASK"},{"dirty":False,"displayName":"PSA Contact ID","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:9448a4b8563656ab8c4273457299db813f8d8cb209","html":None,"name":"PSAContactID","value":""},{"dirty":False,"displayName":"Service","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:936725cd10c735d1dd8c5b4cd4969cb0bd833655f4","html":None,"name":"Service","value":""},{"dirty": False,"displayName": "NOCVersion","fieldId": "BO:6dd53665c0c24cab86870a21cf6434ae,FI:9456a886b185c4843e12924b588feb64a99e4e696f","html": None,"name": "NOCVersion","value": "1"},{"dirty":False,"displayName":"Category","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:9e0b434034e94781ab29598150f388aa","html":None,"name":"Category","value":""},{"dirty":False,"displayName":"Subcategory","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:1163fda7e6a44f40bb94d2b47cc58f46","html":None,"name":"Subcategory","value":""},{"dirty":False,"displayName":"nocticketID","fieldId":"BO:6dd53665c0c24cab86870a21cf6434ae,FI:944682eacb7c655f9053474074bb3e8feb4fa16d20","html":None,"name":"NocticketID","value":"20000000001"}],"links":[{"name":"Delete Record","url":"http://continuumnoc.cherwellondemand.com/CherwellAPI/api/V1/deletebusinessobject/busobid/6dd53665c0c24cab86870a21cf6434ae/busobrecid/94588cbbac883e2afde3954b25b382279205a40476"}],"errorCode":None,"errorMessage":None,"hasError":False}],"hasPrompts":False,"links":[],"prompts":[],"searchResultsFields":[],"simpleResults":None,"totalRows":1,"errorCode":None,"errorMessage":None,"hasError":False}

notesobj={"businessObjects":[],"hasPrompts":False,"links":[],"prompts":[],"searchResultsFields":[],"simpleResults":None,"totalRows":0,"errorCode":None,"errorMessage":None,"hasError":False}

accessobj={"access_token": "123456","token_type": "bearer","expires_in": 86399,"refresh_token": "ad7c5a8b9fb2414589de314b7ad608dd","as:client_id": "4695f441-a353-41bb-bafd-651bb016e7d7","username": "Integration_Test2",".issued": "Tue, 21 Jan 2020 13:10:38 GMT",".expires": "Wed, 22 Jan 2020 13:10:38 GMT"}

listofincidents={}

api = Flask(__name__)

latency=0.5

PREFIX="/mbird/api/V1"

@api.route(PREFIX+'/savebusinessobject', methods=['POST'])
def post_savebusinessobject():
    incidentobject["busObPublicId"]=str(random.randrange(20200100000001, 20200199999999, 3))
    incidentobject["busObRecId"]=str(uuid.uuid1().hex)
    time.sleep(latency)
    return json.dumps(incidentobject)

@api.route(PREFIX+'/savebusinessobjectbatch', methods=['POST'])
def post_savebusinessobjectbatch():
    responses["responses"][0]["busObPublicId"]=str(random.randrange(20200100000001, 20200199999999, 3))
    responses["responses"][0]["busObRecId"]=str(uuid.uuid1().hex)
    time.sleep(latency)
    return json.dumps(responses)

@api.route(PREFIX+'/linkrelatedbusinessobject/<path:text>', methods=['GET'])
def get_linkRelatedBO(text):
	time.sleep(latency)
	return json.dumps({})


@api.route('/mbird/token', methods=['POST'])
def get_authToken():
	accessobj["access_token"]=str(uuid.uuid4())
	accessobj[".issued"]=time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())
	accessobj[".expires"]=time.strftime("%a, %d %b %Y %I:%M:%S %p GMT", (datetime.now()+timedelta(hours=18)).timetuple())
	time.sleep(latency)
	return accessobj


@api.route(PREFIX+'/getsearchresults', methods=['POST'])
def get_searchResults():
    requestjson=request.get_json()
    print request
    print requestjson["filters"][0]["fieldId"]
    print requestjson
    time.sleep(latency)
    if(requestjson["filters"][0]["fieldId"]=="944682eacb7c655f9053474074bb3e8feb4fa16d20"):
        incidentobj["businessObjects"][0]["busObPublicId"]=str(random.randrange(20200100000001, 20200199999999, 3))
        incidentobj["businessObjects"][0]["busObRecId"]=str(uuid.uuid1().hex)
	incidentobj["businessObjects"][0]["busObRecId"]=str(uuid.uuid1().hex)
	return json.dumps(incidentobj)
    elif (requestjson["filters"][0]["fieldId"]=="9446cddb05a4817182c15e4755b6f37eb2ec14ef0f"):
	return json.dumps(contactobj)
    else:
        return json.dumps(notesobj)

if __name__ == '__main__':
    api.run(host='0.0.0.0',debug=False)

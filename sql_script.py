from __future__ import print_function
import mysql.connector
import json
import urllib2
from mysql.connector import errorcode
cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='fsa')
cursor = cnx.cursor()
#Records = 0;
def listing(XXstr):
    add_business = ("INSERT INTO fsadata "
               "(FHRSID, BusinessName,RatingDate, BusinessType, RatingValue, AddressLine1, AddressLine2, AddressLine3, AddressLine4,Postcode,LocalAuthorityBusinessID,BusinessTypeID, RatingKey, LocalAuthorityCode, LocalAuthorityName, NewRatingPending ) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    FHRSID = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['FHRSID'])
    FHRSID = FHRSID.replace('"',"")
    BusinessName = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['BusinessName'])
    BusinessName = BusinessName.replace('"','')
    BusinessType = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['BusinessType'])
    BusinessType = BusinessType.replace('"','')
    RatingDate = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['RatingDate'])
    RatingDate = RatingDate.replace('"','')
    RatingValue = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['RatingValue'])
    RatingValue = RatingValue.replace('"','')
    AddressLine1 = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['AddressLine1'])
    AddressLine1 = AddressLine1.replace('"','')
    if AddressLine1 == 'null':
        AddressLine1 = ''
    AddressLine2 = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['AddressLine2'])
    AddressLine2 = AddressLine2.replace('"','')
    if AddressLine2 == 'null':
        AddressLine2 = ''
    AddressLine3 = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['AddressLine3'])
    AddressLine3 = AddressLine3.replace('"','')
    if AddressLine3 == 'null':
        AddressLine3 = ''
    AddressLine4 = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['AddressLine4'])
    AddressLine4 = AddressLine4.replace('"','')
    if AddressLine4 == 'null':
        AddressLine4 = ''
    Postcode = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['PostCode'])
    Postcode = Postcode.replace('"','')
    LocalAuthorityBusinessID = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['LocalAuthorityBusinessID'])
    LocalAuthorityBusinessID = LocalAuthorityBusinessID.replace('"','')
    BusinessTypeID = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['BusinessTypeID'])
    BusinessTypeID = BusinessTypeID.replace('"','')
    RatingKey = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['RatingKey'])
    RatingKey = RatingKey.replace('"','')
    LocalAuthorityCode = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['LocalAuthorityCode'])
    LocalAuthorityCode = Postcode.replace('"','')
    LocalAuthorityName = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['LocalAuthorityName'])
    LocalAuthorityName = LocalAuthorityName.replace('"','')
    NewRatingPending = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['NewRatingPending'])
    NewRatingPending = NewRatingPending.replace('"','')
    data_business = (FHRSID, BusinessName,RatingDate , BusinessType, RatingValue, AddressLine1, AddressLine2, AddressLine3, AddressLine4,Postcode,LocalAuthorityBusinessID,BusinessTypeID, RatingKey, LocalAuthorityCode, LocalAuthorityName, NewRatingPending)
    cursor.execute(add_business, data_business)
#try:
for x in range(0, 2):
    x += 1 # Same as a = a + 1
    astr = str(x)
    if not x % 1:
        print("the program has searched:" + str(x) + ' pages')
        url = 'http://ratings.food.gov.uk/enhanced-search/en-GB/%5E/%5E/Relevance/0/%5E/%5E/1/'+ astr +'/2500/json'
    print(url)
    req = urllib2.Request(url)
    opener =  urllib2.build_opener()
    f = opener.open(req)
    jsona = json.load(f)
    Records = str(x)
    for XX in range(0, 2500):
        XXstr = XX
        listing(XXstr)
        XX += 1 # Same as a = a + 1
        astr = str(XX)
#except:
print('The program has reached the end of the search with' + Records + 'Pages')
cnx.commit()
cursor.close()
cnx.close()

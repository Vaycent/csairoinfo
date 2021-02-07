# amway-content-center

python3 -m zeep http://10.143.173.61:7103/EB_Ebiz_Services/member/MemberInfoDbSrv_v1_0_0?wsdl

Prefixes:
     xsd: http://www.w3.org/2001/XMLSchema
     ns0: http://xmlns.oracle.com/pcbpel/adapter/db/sp/memberinfo
     ns1: http://xmlns.oracle.com/pcbpel/adapter/db/sp/retrieve_personal_services
     ns2: http://xmlns.oracle.com/pcbpel/adapter/db/sp/getXMemberInfo

Global elements:
     
     ns2:InputParameters(ARG_ADA: xsd:decimal)
     ns2:OutputParameters(ARG_ERRCODE: xsd:string, ARG_XMEMBER_INFO: ns2:AMWAY.XMEMBER_INFO)
     ns0:InputParameters(ARG_ADA: xsd:decimal)
     ns0:OutputParameters(ARG_ERRCODE: xsd:string, ARG_MEMBER_INFO: ns0:AMWAY.MEMBER_INFO)
     ns1:InputParameters(ARG_ADA: xsd:decimal)
     ns1:OutputParameters(ARG_ERRCODE: xsd:string, ARG_PERSONAL_SERVICES: ns1:AMWAY.PERSONAL_SERVICE)

Global types:
     xsd:anyType
     xsd:ENTITIES
     xsd:ENTITY
     xsd:ID
     xsd:IDREF
     xsd:IDREFS
     xsd:NCName
     xsd:NMTOKEN
     xsd:NMTOKENS
     xsd:NOTATION
     xsd:Name
     xsd:QName
     xsd:anySimpleType
     xsd:anyURI
     xsd:base64Binary
     xsd:boolean
     xsd:byte
     xsd:date
     xsd:dateTime
     xsd:decimal
     xsd:double
     xsd:duration
     xsd:float
     xsd:gDay
     xsd:gMonth
     xsd:gMonthDay
     xsd:gYear
     xsd:gYearMonth
     xsd:hexBinary
     xsd:int
     xsd:integer
     xsd:language
     xsd:long
     xsd:negativeInteger
     xsd:nonNegativeInteger
     xsd:nonPositiveInteger
     xsd:normalizedString
     xsd:positiveInteger
     xsd:short
     xsd:string
     xsd:time
     xsd:token
     xsd:unsignedByte
     xsd:unsignedInt
     xsd:unsignedLong
     xsd:unsignedShort
     ns2:AMWAY.XMEMBER_INFO(ADA: xsd:decimal, CNAME: ns2:CNAME, SPOUSE_CNAME: ns2:SPOUSE_CNAME, ID_CARD_NUM: ns2:ID_CARD_NUM, SPOUSE_ID_CARD_NUM: ns2:SPOUSE_ID_CARD_NUM, SEX: ns2:SEX, SPOUSE_SEX: ns2:SPOUSE_SEX, CTR_CDE: ns2:CTR_CDE, SHOP_NAME: ns2:SHOP_NAME, CITY_CDE: ns2:CITY_CDE, CITY_NAME: ns2:CITY_NAME, PROV_CDE: ns2:PROV_CDE, PROV_NAME: ns2:PROV_NAME, WAREHOUSE_CDE: ns2:WAREHOUSE_CDE, JOIN_DATE: ns2:JOIN_DATE, DST_TYPE_CDE: ns2:DST_TYPE_CDE, DST_TYPE: ns2:DST_TYPE, PIN_LVL_CDE: ns2:PIN_LVL_CDE, CLASS_CODE: ns2:CLASS_CODE, EXPIRY_DATE: ns2:EXPIRY_DATE, EXPIRY_DAYS: xsd:decimal)
     ns0:AMWAY.MEMBER_INFO(ADA: xsd:decimal, CNAME: ns0:CNAME, SPOUSE_CNAME: ns0:SPOUSE_CNAME, ID_CARD_NUM: ns0:ID_CARD_NUM, SPOUSE_ID_CARD_NUM: ns0:SPOUSE_ID_CARD_NUM, GENDER: ns0:GENDER, SPOUSE_GENDER: ns0:SPOUSE_GENDER, SHOP_CDE: ns0:SHOP_CDE, SHOP_NAME: ns0:SHOP_NAME, CITY_NAME: ns0:CITY_NAME, PROV_NAME: ns0:PROV_NAME, REG_CDE: ns0:REG_CDE, REG_NAME: ns0:REG_NAME, JOIN_DATE: ns0:JOIN_DATE, EXPIRY_DATE: ns0:EXPIRY_DATE, RESIGN_DATE: ns0:RESIGN_DATE, STATUS: ns0:STATUS, DST_TYPE_CDE: ns0:DST_TYPE_CDE, DST_TYPE_NAME: ns0:DST_TYPE_NAME, PIN_LVL_CDE: ns0:PIN_LVL_CDE, PIN_LVL_NAME: ns0:PIN_LVL_NAME)
     ns1:AMWAY.PERSONAL_SERVICE(SMS_PHONE1: ns1:SMS_PHONE1, SMS_PHONE2: ns1:SMS_PHONE2, MMS_PHONE1: ns1:MMS_PHONE1, MMS_PHONE2: ns1:MMS_PHONE2, EMAIL: ns1:EMAIL)

Bindings:
     Soap11Binding: {http://soa.amway.com/dbadapter/memberinfo/}memberinfo-binding

Service: memberinfo-service
     Port: memberinfo (Soap11Binding: {http://soa.amway.com/dbadapter/memberinfo/}memberinfo-binding)
         Operations:
            getMemberInfo(ARG_ADA: xsd:decimal) -> ARG_ERRCODE: xsd:string, ARG_MEMBER_INFO: ns0:AMWAY.MEMBER_INFO
            getPersonalServices(ARG_ADA: xsd:decimal) -> ARG_ERRCODE: xsd:string, ARG_PERSONAL_SERVICES: ns1:AMWAY.PERSONAL_SERVICE
            getXMemberInfo(ARG_ADA: xsd:decimal) -> ARG_ERRCODE: xsd:string, ARG_XMEMBER_INFO: ns2:AMWAY.XMEMBER_INFO

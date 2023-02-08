userCreateServer = False
SaveDataVer = False
userId = False
authKey = False
secretKey = False
region = False

# This option setConfig.
def setConfigCertificate(certificateData):
    global userCreateServer, SaveDataVer, userId, authKey, secretKey, region

    userCreateServer = certificateData["userCreateServer"][:-1]
    SaveDataVer = certificateData["SaveDataVer"]
    userId = certificateData["userId"]
    authKey = certificateData["authKey"]
    secretKey = certificateData["secretKey"]
    region = userCreateServer[-2:].upper()

    if region == "US":
        region = "NA"

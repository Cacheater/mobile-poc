import os

class Initialize():
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = "%d/%m/%Y"
    formatHour = "%H%M%S"

    #JasonData
    Json = basedir + u'/pages'
    #JsonResponseData = basedir + u'\datajson'

    #************************************************************************************
    # APPIUM MOBILE DATA
    #************************************************************************************

    DEVICE = u'Emulador'
    APP_TYPE = u'STACK'
    #DEVICES JSON
    DEVICES_JSON = basedir + u'/setup/devices.json'

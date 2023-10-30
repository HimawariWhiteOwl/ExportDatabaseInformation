import json
from Model.SettingModel import AppSetting
json_file = "config/appSetting.json"

def GetAppSetting():
    with open(json_file, encoding='utf-8') as setting:
        getSetting = json.load(setting)
    AppSettingModel = AppSetting(**getSetting)
    return AppSettingModel



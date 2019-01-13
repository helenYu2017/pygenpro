# Python Localization Sample
import os, gettext

# Support localization
_ = None
def getUserLanguage():
    return "zh-CN"

# Get loc string by language
def getLocStrings():
    currentDir = os.path.dirname(os.path.realpath(__file__))
    print(currentDir)
    return gettext.translation('resource', currentDir, [getUserLanguage(), "en-US"]).gettext

_ = getLocStrings()
print(_("Hello"))


import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from ibm_watson import ApiException

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
version = '2018-05-01'

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version=f'{version}',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')

def englishToFrench(englishText):
    if englishText is None:
        return None
    try:
        frenchText = language_translator.translate(text=englishText,
        model_id='en-fr').get_result()
        return frenchText['translations'][0]['translation']
    except ApiException as ex:
        return "Method failed with status code " + str(ex.code) + ": " + ex.message

def frenchToEnglish(frenchText):
    if frenchText is None:
        return None
    try:
        englishText = language_translator.translate(text=frenchText, 
        model_id='fr-en').get_result()
        return englishText['translations'][0]['translation']
    except ApiException as ex:
        return "Method failed with status code " + str(ex.code) + ": " + ex.message






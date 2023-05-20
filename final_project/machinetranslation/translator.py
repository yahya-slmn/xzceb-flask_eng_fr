
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator('CGcToXOZdyqDi2Vnnk0dhjkyxUHZHpF4pQ2lqGvryQc7')
translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

# Set the service URL (e.g. "https://api.us-south.language-translator.watson.cloud.ibm.com")
translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/236013d9-44fd-47c8-a74e-3658973fd794')

def englishToFrench(englishText):
    # Translate English to French
    translation = translator.translate(
        text=englishText,
        source='en',
        target='fr'
    ).get_result()

    # Extract and return the translated text
    frenchText = translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    # Translate French to English
    translation = translator.translate(
        text=frenchText,
        source='fr',
        target='en'
    ).get_result()

    # Extract and return the translated text
    englishText = translation['translations'][0]['translation']
    return englishText 
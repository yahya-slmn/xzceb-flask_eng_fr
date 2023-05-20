import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
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
URL = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/236013d9-44fd-47c8-a74e-3658973fd794'
translator.set_service_url(URL)

"""
This module provides functions for translating text between English and French.
"""
def english_to_french(english_text):
    # Translate English to French
    if not english_text:
        return ""
    translation = translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()

    # Extract and return the translated text
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    # Translate French to English
    if not french_text:
        return ""
    translation = translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()

    # Extract and return the translated text
    english_text = translation['translations'][0]['translation']
    return english_text

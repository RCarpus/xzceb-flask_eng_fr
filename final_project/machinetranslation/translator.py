"""Translator module to translate text from one language to another."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-05-26',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')

def english_to_french(text):
    """Translates text from English to French."""
    if text == '':
        return ''
    translation = language_translator.translate(
        text=text,
        model_id='en-fr'
    ).get_result()
    return translation.get('translations')[0].get('translation')

def french_to_english(text):
    """Translates text from French to English."""
    if text == '':
        return ''
    translation = language_translator.translate(
        text=text,
        model_id='fr-en'
    ).get_result()
    return translation.get('translations')[0].get('translation')

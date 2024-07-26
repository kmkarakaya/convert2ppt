import google.generativeai as genai
import os
import sys
from convert2ppt import CONFIG

import logging

# Suppress log messages
os.environ['GLOG_minloglevel'] = '2'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Redirect stderr to devnull
sys.stderr = open(os.devnull, 'w')

# Set logging level for absl
logging.getLogger('absl').setLevel(logging.ERROR)



def connect_gemini():
    gemini_api_key = get_gemini_api()
    genai.configure(api_key=gemini_api_key)

    model = genai.GenerativeModel(
        'gemini-1.5-flash',
        system_instruction=CONFIG['llm']['system_prompt'],
        generation_config={"response_mime_type": "application/json"},
      
    )
    return model

def get_gemini_api():
     gemini_api_key = os.getenv('GEMINI_API_KEY')

     return gemini_api_key


# Restore stderr
sys.stderr = sys.__stderr__
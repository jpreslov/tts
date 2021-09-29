from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1
from typing import Text
import playsound

url = 'https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/312320bb-a44c-4075-a694-8b3f6d0dfeb4'
apikey = '6ok7WJNT8DoutGRBrfJyBjHgAuRIhkQiW9366VcyMznv'

num = 0

# def inc_num():
#     global num
#     num += 1


filename = './speech' + str(num) + '.mp3'
filename2 = 'speech' + str(num) + '.mp3'
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

with open(filename, 'wb') as audio_file:
    res = tts.synthesize("Thank you so much. This is what a hard work grindset will do. No days off,. Always working. Entrepeneuere",
                         accept="audio/mp3", voice="en-US_AllisonV3Voice").get_result()
    audio_file.write(res.content)

playsound.playsound(filename2)

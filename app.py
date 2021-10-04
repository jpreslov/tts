from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1
from typing import Text
import librosa
from playsound import playsound

url = "https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/312320bb-a44c-4075-a694-8b3f6d0dfeb4"
apikey = "6ok7WJNT8DoutGRBrfJyBjHgAuRIhkQiW9366VcyMznv"


def inc_num():
    num = 0
    num += 1
    print(num)


filename = "./speech.mp3"
filename2 = "speech.mp3"
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)


with open(filename, "wb") as audio_file:
    res = tts.synthesize("Thank you soiouoiuoiuouoi much. Thoys oys whoyt a hoyrd woyrk groyndset will do. Noy doys oyff.",
                         accept="audio/mp3", voice="en-US_AllisonV3Voice").get_result()
    audio_file.write(res.content)
    # y, sr = librosa.load(filename, sr=16000)
    # y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=4)
    # audio_file.write(y_shifted)


playsound(filename2)

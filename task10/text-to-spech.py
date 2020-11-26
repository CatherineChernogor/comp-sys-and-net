import io
import requests
from pydub import AudioSegment
from soundfile import SoundFile


def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values


def get_token():
    auth_url = "https://francecentral.api.cognitive.microsoft.com/sts/v1.0/issueToken"
    key = "be5f4c47488e4d349dbb06b527492c7c"
    auth_headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Content-Length": "0",
        "Content-type": "application/x-www-form-urlencoded"
    }

    return requests.post(auth_url, headers=auth_headers).text


def get_voice_list(token):
    lang_url = "https://francecentral.tts.speech.microsoft.com/cognitiveservices/voices/list"
    lang_headers = {"Authorization": "Bearer " + token, }

    return requests.get(lang_url, headers=lang_headers).json()


def get_first_voice_id(voices):

    for voice in voices:
        locale = json_extract(voice, 'Locale')
        locale = ''.join(locale)
        if (locale.find('en') != -1):
            return voices.index(voice)


def form_xml(voice):

    lang = ''.join(json_extract(voice, 'Locale'))
    gender = ''.join(json_extract(voice, 'Gender'))
    name = ''.join(json_extract(voice, 'ShortName'))

    xml = "<speak version='1.0' xml:lang='" + lang + "'><voice xml:lang='" + lang + \
        "' xml:gender='" + gender + "' name='" + \
        name + "'>" + text + "</voice></speak>"

    return xml


def tts(text):

    token = get_token()
    print("'\n'token/bearer in use: ", token, '\n')

    voices = get_voice_list(token)

    id = get_first_voice_id(voices)
    voice = voices[id]
    print("file will be read by ", voice, '\n')

    xml = form_xml(voice)

    api_url = "https://francecentral.tts.speech.microsoft.com/cognitiveservices/v1"
    api_headers = {
        "Authorization": "Bearer " + token,
        "X-Microsoft-OutputFormat": "raw-16khz-16bit-mono-pcm",
        "Content-Type": "application/ssml+xml"
    }

    response = requests.post(api_url, headers=api_headers, data=xml).content

    out_name = file + ".wav"

    raw = io.BytesIO(response)
    frame = ''.join(json_extract(voice, 'SampleRateHertz'))
    audio = AudioSegment.from_raw(raw, sample_width=2, frame_rate=int(
        frame), channels=1).export(out_name, format='wav')
    print("Done, your file is", out_name, '\n')


def extra(out_name): 
    f = SoundFile(out_name+'.wav')
    sec = format(len(f) / f.samplerate)
    result = float(sec) / len(text)

    print("seconds/symbol: ", result, '\n')


file = input('>> ')
try:
    _in = open(file+ ".txt", "r", encoding="utf-8")
    text = _in.read()
    tts(text)
    extra(file)
except:
    print("oops, something wrong")


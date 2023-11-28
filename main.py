from os import path
from huggingsound import SpeechRecognitionModel
import streamlit as st

model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-russian")

BRAILLE_DICTIONARY_PATTERNS = {
    'а':'⠁',
    'б':'⠃',
    'в':'⠺',
    'г':'⠛',
    'д':'⠙',
    'е':'⠑',
    'ё':'⠡',
    'ж':'⠚',
    'з':'⠵',
    'и':'⠊',
    'й':'⠯',
    'к':'⠅',
    'л':'⠇',
    'м':'⠍',
    'н':'⠝',
    'о':'⠕',
    'п':'⠏',
    'р':'⠗',
    'с':'⠎',
    'т':'⠞',
    'у':'⠥',
    'ф':'⠋',
    'х':'⠓',
    'ц':'⠉',
    'ч':'⠟',
    'ш':'⠱',
    'щ':'⠭',
    'ъ':'⠷',
    'ы':'⠮',
    'ь':'⠾',
    'э':'⠪',
    'ю':'⠳',
    'я':'⠫',
    ' ': ' ',
}


def convertTextToBraille(text):
    result = ""
    for char in text:
        if (char.lower() in BRAILLE_DICTIONARY_PATTERNS):
            result += BRAILLE_DICTIONARY_PATTERNS.get(char.lower())
    return result

def getTextFromAudio(path: str):
    with open(path,"wb+") as f:
         f.write(w.getbuffer())
         f.close()
         print('output: ', output)
         transcriptions = model.transcribe([output])
         text = transcriptions[0]['transcription']
         return text


w = st.file_uploader("Upload a mp3", type="mp3")
if w:
    print(w)
    st.write(w.name)
    audio_bytes = w.getvalue()
    st.audio(audio_bytes, format='audio/ogg')
    parent_dir = path.dirname(path.abspath(__file__))
    output = path.join(parent_dir, w.name)
    print(output)
    text = getTextFromAudio(output)
    st.write(text)
    st.write(convertTextToBraille(text))

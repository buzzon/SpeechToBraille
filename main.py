from huggingsound import SpeechRecognitionModel

model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-russian")
audio_paths = ["test.mp3"]

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


def speechToText(audio_paths):
    result = []
    transcriptions = model.transcribe(audio_paths)
    for t in transcriptions:
        result.append(t['transcription'])
    return result


def convertTextToBraille(text):
    result = ""
    for char in text:
        if (char.lower() in BRAILLE_DICTIONARY_PATTERNS):
            result += BRAILLE_DICTIONARY_PATTERNS.get(char.lower())
    return result


text = speechToText(audio_paths)
for t in text:
    print(t)
    print(convertTextToBraille(t))
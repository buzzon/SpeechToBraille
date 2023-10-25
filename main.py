from huggingsound import SpeechRecognitionModel

model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-russian")
audio_paths = ["test.mp3"]

transcriptions = model.transcribe(audio_paths)
text = ' .'.join(list(t['transcription'] for t in transcriptions))
                       
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

def convert(text):
    result = ""
    for char in text:
        if (char.lower() in BRAILLE_DICTIONARY_PATTERNS):
            result += BRAILLE_DICTIONARY_PATTERNS.get(char.lower())
    return result


print(text)
print(convert(text))

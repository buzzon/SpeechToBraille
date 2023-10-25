# import torch
# import librosa
# from datasets import load_dataset
# from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

# # load_dataset("mozilla-foundation/common_voice_11_0", "ru")

# LANG_ID = "ru"
# MODEL_ID = "jonatasgrosman/wav2vec2-large-xlsr-53-russian"
# SAMPLES = 5

# test_dataset = load_dataset("common_voice", LANG_ID, split=f"test[:{SAMPLES}]")
# # test_dataset = load_dataset("mozilla-foundation/common_voice_11_0", "ru")

# processor = Wav2Vec2Processor.from_pretrained(MODEL_ID)
# model = Wav2Vec2ForCTC.from_pretrained(MODEL_ID)

# def speech_file_to_array_fn(batch):
#     speech_array, sampling_rate = librosa.load(batch["path"], sr=16_000)
#     batch["speech"] = speech_array
#     batch["sentence"] = batch["sentence"].upper()
#     return batch

# test_dataset = test_dataset.map(speech_file_to_array_fn)
# inputs = processor(test_dataset["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)

# with torch.no_grad():
#     logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

# predicted_ids = torch.argmax(logits, dim=-1)
# predicted_sentences = processor.batch_decode(predicted_ids)

# for i, predicted_sentence in enumerate(predicted_sentences):
#     print("-" * 100)
#     print("Reference:", test_dataset[i]["sentence"])
#     print("Prediction:", predicted_sentence)


from huggingsound import SpeechRecognitionModel

model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-russian")
audio_paths = ["test.mp3"]



transcriptions = model.transcribe(audio_paths)
text = ' .'.join(list(t['transcription'] for t in transcriptions))

# BRAILLE_DICTIONARY_PATTERNS = {
#     'а':'\u2801',
#     'б':'\u2803',
#     'в':'\u283A',
#     'г':'\u281B',
#     'д':'\u2819',
#     'е':'\u2811',
#     'ё':'\u2821',
#     'ж':'\u2834',
#     'з':'\u2835',
#     'и':'\u280A',
#     'й':'\u28D6',
#     'к':'\u2890',
#     'л':'\u2846',
#     'м':'\u280D',
#     'н':'\u2859',
#     'о':'\u2862',
#     'п':'\u2856',
#     'р':'\u2817',
#     'с':'\u2854',
#     'т':'\u281E',
#     'у':'\u2825',
#     'ф':'\u280B',
#     'х':'\u2826',
#     'ц':'\u2809',
#     'ч':'\u28B6',
#     'ш':'\u28A2',
#     'щ':'\u28C9',
#     'ъ':'\u28E6',
#     'ы':'\u28D4',
#     'ь':'\u28F4',
#     'э':'\u2894',
#     'ю':'\u2833',
#     'я':'\u282B',
#     ' ': '\u2800',
# }

                       
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


test = "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я"

print(test)
print(convert(test))

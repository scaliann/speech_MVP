import re
import whisper
import torch
import transformers
from data_set import data_set




def speech_recognition(model='medium', reference_words=[], test_audio=''):
    speech_model = whisper.load_model(model)
    result = speech_model.transcribe(test_audio, language='ru')
    transcribed_word = result['text']
    transcribed_word = transcribed_word.replace(' ', '')
    transcribed_word = transcribed_word.lower()
    transcribed_word = transcribed_word.replace(',', '').replace('!', '').replace('.', '').replace('?', '')
    print(transcribed_word)
    for reference_word in reference_words:
        reference_word = reference_word.lower()

        min_length = min(len(reference_word), len(transcribed_word))
        ref_word_len = len(reference_word)

        matching_characters = 0
        for i in range(min_length):
            if transcribed_word[i] == reference_word[i]:
                matching_characters += 1
        n_mathing_characters = ref_word_len - matching_characters
        percentage = (matching_characters/ref_word_len) * 100

        print(f'Входное слово: {transcribed_word}, Эталонное слово: {reference_word}, Совпавших букв: {matching_characters}')
        print(f'Слово произнесенно правильно на {percentage}%')





def main():
    print('Поехали')
    for i, word in enumerate(data_set):
        test_audio = f"{i + 1}.ogg"
        speech_recognition(model='medium', reference_words=[word], test_audio=test_audio)

if __name__ == '__main__':
    main()












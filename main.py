
import whisper
from data_set import data_set

оче
def speech_recognition(model='medium', reference_words=[], test_audio=''):
    speech_model = whisper.load_model(model)
    result = speech_model.transcribe(test_audio, language='ru')
    transcribed_word = result['text']
    transcribed_word = transcribed_word.replace(' ', '')
    transcribed_word = transcribed_word.lower()
    transcribed_word = transcribed_word.replace(',', '').replace('!', '').replace('.', '').replace('?', '')

    #транскрибируется аудиофайл, убирается вся пунктуация/пробелы, нижний регистр

    print(transcribed_word)

    for reference_word in reference_words:
        reference_word = reference_word.lower()

        min_length = min(len(reference_word), len(transcribed_word))
        ref_word_len = len(reference_word)

        #эталонное слово в нижний регистр, определяется минимальное кол-во букв и кол-во букв в эталонном слове

        matching_characters = 0
        for i in range(min_length):
            if transcribed_word[i] == reference_word[i]:
                matching_characters += 1

        #происходит сравнивание совпавших слов

        n_mathing_characters = ref_word_len - matching_characters
        percentage = (matching_characters/ref_word_len) * 100

        #перевод в процентную оценку

        print(f'Входное слово: {transcribed_word}, Эталонное слово: {reference_word}, Совпавших букв: {matching_characters}')
        print(f'Слово произнесенно правильно на {percentage}%')


def main():
    print('Поехали')
    for i, word in enumerate(data_set):
        test_audio = f"{i + 1}.ogg"
        speech_recognition(model='medium', reference_words=[word], test_audio=test_audio)

#цикл 32 раза вызывает функцию, передавая в нее параметры test_audio = аудиофайл и reference_word = эталонное слово


if __name__ == '__main__':
    main()












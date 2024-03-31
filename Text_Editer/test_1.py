from gtts import gTTS


def text_to_speech(text, lan, file_name):
    voices = gTTS(text=text, lang=lan, slow=False)
    voices.save(file_name)


if __name__ == '__main__':
    mp3 = '.mp3'
    text = input("Enter the text to speech text: ")
    language = input("Enter the language of the audio that you need to speech text: ")
    file_name = input("Enter the text to speech file name: ")
    mp3_file_name = file_name + mp3

    language_mapping = {
        'english': 'en',
        'french': 'fr',
        'german': 'de',
        'italian': 'it',
        'spanish': 'es',
        'portuguese': 'pt',
        'russian': 'ru',
        'japanese': 'ja',
        'hindi': 'hi',
        'korean': 'ko',
        'chinese': 'zh',
        'arabic': 'ar',
        'dutch': 'nl',
        'turkish': 'tr',
        'polish': 'pl',
        'swedish': 'sv',
        'danish': 'da',
        'norwegian': 'no',
        'finnish': 'fi',
        'greek': 'el',
        'czech': 'cs',
        'hungarian': 'hu',
        'romanian': 'ro',
        'catalan': 'ca',
        'vietnamese': 'vi',
        'thai': 'th',
        'indonesian': 'id',
        'slovak': 'sk',
        'croatian': 'hr',
        'bulgarian': 'bg',
        'serbian': 'sr',
        'ukrainian': 'uk',
        'malay': 'ms',
        'hebrew': 'he',
        'bengali': 'bn',
        'tamil': 'ta',
        'telugu': 'te',
        'kannada': 'kn',
        'marathi': 'mr',
        'gujarati': 'gu',
        'sinhala': 'si',
        'urdu': 'ur'
    }
    if language in language_mapping:
        language = language_mapping[language]
    else:
        print('Please enter a valid language')

    text_to_speech(text, language, mp3_file_name)
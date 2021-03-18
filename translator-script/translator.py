from translate import Translator
import sys

'''File Translator
    Cmd arguments:
    
    First argument : language to translate
    Second argument : Filepath to be translated
    
'''


def beautify(fn):
    def wrapped_fn(*args, **kwargs):
        print('*' * 20)
        print(f'Translated Text in language : {kwargs["to_lang"]}')
        res = fn(*args, **kwargs)
        print('*' * 20)
        return res

    return wrapped_fn


@beautify
def translate(to_lang, text_to_translate='Hello Sir'):
    translator = Translator(to_lang=to_lang)
    translation = translator.translate(text_to_translate)
    return translation


if __name__ == '__main__':
    default_to_lang = 'hi'
    if len(sys.argv) > 1:
        default_to_lang = sys.argv[1]
        filePath = sys.argv[2]
        print(f'File to be translated : {filePath}')
        with open(filePath) as f:
            txt = f.read()
            print(translate(to_lang=default_to_lang, text_to_translate=txt))
    else:
        print(translate(to_lang=default_to_lang))

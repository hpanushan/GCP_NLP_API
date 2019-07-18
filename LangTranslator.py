from googletrans import Translator

def langTranslator(text):
    translator = Translator()
    out = translator.translate(text)
    return out.text

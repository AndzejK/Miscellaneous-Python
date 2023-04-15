from googletrans import Translator
# google API
translator=Translator()
translation=translator.translate('Sveiki, kaip sekasi? :)',dest='en').text

print(translation)
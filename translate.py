from html.parser import HTMLParser
from unittest import result
from filee import File
import googletrans
from googletrans import Translator


LANGUAGE_DEST = 'hindi' #Here you can change language_dest


def traductor(File):

    translator = Translator()
    translated = translator.translate(File, dest = LANGUAGE_DEST, src = 'auto')

    final_index = str(translated.text)
    return final_index



class Parser(HTMLParser):

  def handle_data(self, data):
    global all_data_src
    global all_data_dest
    result = traductor(data)
    all_data_src.append(data)
    all_data_dest.append(result)



all_data_src = []
all_data_dest = []


# Creating an instance of our class.
parser = Parser()
parser.feed(File) #Here you pass the HTML file



newfile = ''
for indice, valor_a in enumerate(all_data_src):

    if valor_a.startswith('\n'):
        pass
    else:
        newfile = File.replace(valor_a ,all_data_dest[indice])
        File = newfile




#here you save the HTML-translated
f = open("index-final.txt", "a")
f.write(newfile)
f.close()



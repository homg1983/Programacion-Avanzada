from PIL import Image 
import pytesseract as tess
from googletrans  import Translator

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open('frace1.jpg')
txt = tess.image_to_string(img)
archivo = open('Texto_imagen.txt','w')
filename = 'TTexto_imagen.txt'
archivo.write(txt +"\n""\n")
archivo.close()

filename = open('Texto_imagen.txt') 
text = filename.read()

translator = Translator()

translate = translator.translate(text, dest='es')

salida = open('Resultado_traducción.txt','w')
salida.write(txt + "\n""\n" + translate.text)
salida.close()
import pyttsx3
import PyPDF2
book = open('461.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
print(pages)
page = pdfReader.pages[3]
text = page.extract_text()
speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()
print("donee")    
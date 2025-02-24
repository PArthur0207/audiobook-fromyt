import pyttsx3
import PyPDF2
book = open('461.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
page_to_read = int(input("What page would you like to listen to? (0-66) \n "))
page = pdfReader.pages[page_to_read]
text = page.extract_text()
speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()
print("donee")    
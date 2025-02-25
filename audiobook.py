import pyttsx3
import PyPDF2
book = open('harrypotter.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
print("This is the Complete Harry Potter Collection")
print("CONTENTS \n Harry Potter and the Sorcerer’s Stone (11-273)") 
print("Harry Potter and the Chamber of Secrets(281-564)")
print("Harry Potter and the Prisoner of Azkaban(572-938)")
print("Harry Potter and the Goblet of Fire(948-1559)")
print("Harry Potter and the Order of the Phoenix(1569-2405)")
print("Harry Potter and the Half-Blood Prince(2414-2963)")
print("Harry Potter and the Deathly Hallows(2973-3621)")
page_to_read_start = int(input("What page would you like to listen to? (0-3623) \n "))
page_to_read_finish = int(input("Until what page?:"))
for i in range(page_to_read_start, page_to_read_finish):
    page = pdfReader.pages[i]
    text = page.extract_text()
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()
print("Done!")    
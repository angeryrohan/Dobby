import openai
from docx import Document
from docx.shared import Inches
import pywhatkit as pw
from PyPDF2 import PdfReader
from apikey import APIKEY
openai.api_key = APIKEY

reader = PdfReader('DA1.pdf')
 
# printing number of pages in pdf file
 
# getting a specific page from the pdf file
page = reader.pages[0]
userName = input("Enter your name: ")
userRegNo = input("Enter your registration number: ")
# extracting text from page

input2GPT = "My name is "+ userName + ". My registration number is "+ userRegNo + ". Below is my homework. Put my name and registration number at the top of the assignment and solve it. \n " + page.extract_text()

output = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": 
    input2GPT}]
  )

outputGPT = output['choices'][0]['message']['content']
print("DA executed successfully. Check ")

document = Document()
p = document.add_paragraph(outputGPT)
document.add_page_break()

document.save(userName + userRegNo + '_DA' +'.docx')
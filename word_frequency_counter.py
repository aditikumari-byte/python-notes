
import string
def word_frequency(text):
   #text= input("Enter your text:")
   text = text.lower()
   for char in string.punctuation:
      text= text.replace(char,' ')
   
   words = text.split()

   word_count={}
   for word in words:
      if word in word_count:
         word_count[word]+=1
      else:
         word_count[word]=1

   for word,count in word_count.items():
      print(f"{word} : {count}")         


word_frequency("hi hi Hi! aditi aditi")      
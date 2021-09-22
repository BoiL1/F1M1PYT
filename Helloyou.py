import datetime
import random

while True:
   naam = input("Je naam: ")
   print("ik ben " + naam)

   x = datetime.datetime.now()

   print(x)

   print("typ randomize")
   inputText2 = input()
   print("input:", inputText2)
   if inputText2 == "randomize":
      print(random.randint(0,999))

   while True:
      print(naam + " Wil jij dit programma nog een keer doen? yes/no")
      inputText = input()
      print("input:", inputText)
      if inputText == ["yes", "Y", "y", "YES", "Yes"]:
         break
      elif inputText == ["no", "N", "n", "NO", "No"]:
         exit()
      else:
         continue

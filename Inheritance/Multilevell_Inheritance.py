"""2: Multilevel Inheritance:
Multilevel Inheritance takes place between 3 or more than 3 classes.

In Multilevel Inheritance 1 sub class acquires properties of another super class &
that class acquires properties of its another super class & phenomenon continuous. 
"""""

class WhatsAppV1:
   def chat(self):
       print("chat feature")

class WhatsAppV2(WhatsAppV1):
   def audioCalling(self):
       print("Audio Calling Feature")

class WhatsAppV3(WhatsAppV2):
   def videoCalling(self):
       print("Vidio Calling Feature")

v=WhatsAppV3()
v.chat()
v.audioCalling()
v.videoCalling()

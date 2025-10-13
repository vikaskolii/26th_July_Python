#A string in Python is just a piece of text.
# It can be a word, a sentence, or even a whole paragraph.
# You write it inside quotes, like this.



s1="Automation"
print(s1)               #Print string
print("====================================================================================")
print("====================================================================================")


print(len(s1))            #Find the elngth of the string
print(s1.rfind(""))       #Find the elngth of the string
print("====================================================================================")
print("====================================================================================")


print(s1.upper())       #Convert into only Upper case
print("====================================================================================")
print("====================================================================================")


print(s1.lower())       #Convert into Lower case
print("====================================================================================")
print("====================================================================================")



s1=s1.upper()           #if you want permenant change  #Re_intialization
print(s1)
print("====================================================================================")
print("====================================================================================")

a="abcd"
b="ABCD"
print(a==b)                      #Compare data & Case
print(a.__eq__(b))               #Compare data & Case
print(a.lower()==b.lower())      #Compare only data
print("====================================================================================")
print("====================================================================================")

c="VikasKoli"
print("Vik" in c)               # Chcek the  words in the string.
print(c.__contains__("Vik"))    # Alternate way
print(c.startswith("ram"))      #Check starts with letter
print(c.startswith("Vika"))
print(c.endswith("lim"))        #check ends with letter
print(c.endswith("Koli"))
print("====================================================================================")
print("====================================================================================")


d="PythonAutomation"
print(d[0])                #chatAt(Index)
print(d[1])
print(d[4])
print(d[2:5])              #find Substring
print(d[1:7])
print(d.find("q"))         #Find index
print(d.find("t"))         #Find index
print(d.find("o"))
print(d.rfind("n"))        #find last index of the letter
print(d.index("i"))        #Alternate   -> this is for string & lists>>.but it confuse sometime cause duplicate letter occuered.
print("====================================================================================")
print("====================================================================================")

a1="vikas_"
b1="koli"
c1=" mahesh is from pune  "
d1="mahesh tejinkar aurangabad tejinkar tejinkar"
print(a1+b1+c1)        # Concatination the 2 or more string
print(c1.strip())      #it will remove only starting and ending space not remove in-between sentence space.
print(c1.lstrip())     # Remove only left side space
print(c1.rstrip())     # Remove only right side space
print(b1.capitalize()) #Captilize only first letter
print(b1.upper())
print(d1.title())      #capitalize of every words 1stv letter in a senetence.
print("a is occured ::",d1.count("a"),"times")     #occcurence count
print(c1.swapcase())     #convert full into capitalize word


print("====================================================================================")
print("====================================================================================")
str1="Rutuja"
str4="122"
str5="abc123"
str6="     "
str7="my name is mahesh my name is"
print(str1.isalpha())   #Checking alphbates present or not
print(str4.isdigit())   #Checking the digit is present or not
print(str5.isalnum())   #checking the alphanumeric value or not
print(str6.isspace())   #checking the space is occuered or not blank string
print(str7.count("my name is")) # Checking the occurence in string


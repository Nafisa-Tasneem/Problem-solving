formatter = "%r %r %r %r" # 4 ta formatter rakha holo string e . ekhane amra jekono variable
# rakhte parbo

print (formatter % (1, 2, 3, 4)) # ager defined formatter e integer dewa holo
print (formatter % ("one", "two", "three", "four")) #putting string in formatter
print (formatter % (True, False, False, True)) # putting logic in formatter
print (formatter % (formatter, formatter, formatter, formatter)) # putting variable in
#formatter, which is the variable itself
print (formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)) #putting 4 string in formatter
print (formatter % ("আমার", "ভেতরে বাহিরে", " অন্তরে অন্তরে", "আছো তুমি হৃদয় জুড়ে"))
def reversestring(s, i = 0) :
   """Reverses the string s recursively """
   if i == len(s):
       return ""
   return reversestring(s, i+1) + s[i]

print(reversestring("")) # ""
print(reversestring("bonjour")) # ruojnob
print(reversestring("putain de merde")) # ressasser
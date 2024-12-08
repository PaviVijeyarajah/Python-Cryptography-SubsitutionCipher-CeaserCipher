#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Subsitution Cipher

class subCipher:
    def __init__(self):
        self.words= []#put words into a list
        self.subcip = {"a":"z","b":"y","c":"x","d":"w","e":"v","f":"u","g":"t","h":"s","i":"r","j":"q","k":"p","l":"o","m":"n","A":"Z","B":"Y","C":"X","D":"W","E":"V","F":"U","G":"T","H":"S","I":"R","J":"Q","K":"P","L":"O","M":"N"} #have alpha conversion as dict
        self.word2char=[] #convert words to list of characters
        self.char2ciph=[] #convert list of characters to ciphered list of characters
        self.ciph2char=[] #convert list of cipher characters to characters
        self.cipher=[] #holds the encrypted words
        self.word=[] #holds the decrypted words
    
    #switches words to letters using what we learned in intro
    def letter(self):
        for i in range(len(self.words)):
            characters= [character for character in self.words[i]]
            self.word2char.append(characters)
    def get_encryption(self):
        return self.cipher
    def set_words(self,words): 
        self.words.append(words)
    def get_decryption(self):
        return self.word
    #Encryption
    #uses 3 loops to k for each word,i for list of characters and j for subcipher
    def Encryption(self):
        for t in range (len(self.word2char)):
            ciphchar=[]
            for i in range(len(self.word2char[t])):
                if self.word2char[t][i]==" ":
                    ciphchar.append(" ")
                for j in range(len(self.subcip)):
                    keys=list(self.subcip.keys())[j] #represents a key in dict
                    values=list(self.subcip.values())[j] #represents a value in dict
                    if self.word2char[t][i]==keys: #checks if the work
                        ciphchar.append(values)
                    elif self.word2char[t][i]==values:
                        ciphchar.append(keys)
            self.char2ciph.append(ciphchar)
        #convert character cipher into string cipher
        for l in range(len(self.char2ciph)): 
            x=""
            for m in range (len(self.char2ciph[l])):
                x+=self.char2ciph[l][m]
            self.cipher.append(x)
    
    #Decryption
    #uses 3 loops to n for each word o for subcipher and p for list of characters
    def Decryption(self):
        for n in range(len(self.char2ciph)):
            wordchar=[]
            for o in range(len(self.char2ciph[n])):
                if self.char2ciph[n][o]==" ":
                    wordchar.append(" ")
                for p in range(len(self.subcip)):
                    key=list(self.subcip.keys())[p]
                    value=list(self.subcip.values())[p]
                    if self.char2ciph[n][o]==key:
                        wordchar.append(value)
                    elif self.char2ciph[n][o]==value:
                        wordchar.append(key)
            self.ciph2char.append(wordchar)

        for q in range(len(self.ciph2char)):
            x=""
            for r in range(len(self.ciph2char[q])):
                x+=self.ciph2char[q][r]
            self.word.append(x)
obj= subCipher()
obj.set_words("Apples in the garden")
obj.set_words("cloud")
obj.letter()
obj.Encryption()
print(obj.get_encryption())
obj.Decryption()
print(obj.get_decryption())        


# In[12]:


#Ceaser Cipher
class ceaCipher:
    
    def __init__(self):
        self.words=[]
        self.letters={0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}
        self.words2chars=[]#converts the words in list words to letters
        self.encrychars=[]#converts letters to encrypted letters
        self.wordchars=[]#converts encrypted letters to letteres
        self.encryption=[]#converts encrypted letters to words 
        self.word=[]#converts letters to words
    def letter(self):
        for i in range(len(self.words)):
            characters= [character for character in self.words[i]]
            self.words2chars.append(characters)
    def get_encryption(self):
        return self.encryption
    def set_words(self,words): 
        self.words.append(words.lower())
    def get_decryption(self):
        return self.word
    #Encrypting (lets shift letters 4 to right)
    def Encryption(self): #figure out how it will look as a fn
        for k in range(len(self.words2chars)):
            encrytemp=[]
            for m in range(len(self.words2chars[k])):
                if self.words2chars[k][m]==" ": #when there is a space make a space in the encrypted message
                    encrytemp.append(" ")
                for l in range(len(self.letters)):
                    shift=(l+4)%26 #encryption using 4 as encryption key
                    if self.words2chars[k][m]==self.letters[l]:
                        encrytemp.append(self.letters[shift])
            self.encrychars.append(encrytemp)
        #encryption letters to encryption
        for n in range(len(self.encrychars)): 
            x=""
            for o in range (len(self.encrychars[n])):
                x+=self.encrychars[n][o]
            self.encryption.append(x)
    #Decryption
    def Decryption(self):
        for p in range(len(self.encrychars)):
            wordtemp=[]
            for q in range(len(self.encrychars[p])):
                if self.encrychars[p][q]==" ": #when there is a space make a space in the encrypted message
                    wordtemp.append(" ")
                for r in range(len(self.letters)):
                    rshift=(r-4)%26
                    if self.encrychars[p][q]==self.letters[r]:
                        wordtemp.append(self.letters[rshift])
            self.wordchars.append(wordtemp)
        for s in range(len(self.wordchars)):
            x=""
            for t in range(len(self.wordchars[s])):
                x+=self.wordchars[s][t]
            self.word.append(x)        
obj= ceaCipher()
obj.set_words("Apples in the garden")
obj.set_words("sky")
obj.letter()
obj.Encryption()
print(obj.get_encryption())
obj.Decryption()
print(obj.get_decryption())


# In[ ]:





# In[ ]:





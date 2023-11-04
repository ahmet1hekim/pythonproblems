
pattern =input("pattern    ")
text = input("text  ")

prime =2003
base =256
pattern_len= len(pattern)
text_len = len(text)

patternhash =0
texthash=0
verificator=0
for x in range(pattern_len):
    patternhash = (base*patternhash+ord(pattern[x]))%prime
    texthash = (base*texthash+ord(text[x]))%prime
for x in range (text_len-pattern_len+1):
    if(texthash==patternhash):
        for i in range(len(pattern)):
            if(text[x+i]==pattern[i]):
                verificator=verificator+1
        if(int(verificator)==int(len(pattern))):
            print("match at :"+str(x))
    verificator=0
    if(x<text_len-pattern_len):
        texthash =(base*(texthash-ord(text[x])*(pow(base,pattern_len-1)%prime))+ord(text[x+pattern_len]))%prime

def word_count(str):
    counts=dict()
    words=str.slit()
for word in words:
    if word in counts:
        counts[word]+=1
    else:
         counts[word]=1
return counts
print(word_count("the sun rises in the east"))         

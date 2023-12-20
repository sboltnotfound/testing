def bro(array,n,omg,i=0,array2=[],sentences=[]):
    if (i==omg):
        yo=""
        for e in range(len(array2)):      
            yo=yo+array[array2[e]]+" "
        for e in range(len(sentences)):    #making sure same sentences doesnt get printed
            if (yo==sentences[e]):
                return sentences
        sentences.append(yo)
        global stringer
        stringer = stringer + yo + "\n"
        return sentences
    for j in range(n):
        checker = False
        for k in range(len(array2)):         #making sure each selected word is unique
            if (array2[k]==j):
                checker = True
        if checker:
            continue
        array2.append(j)
        sentences=bro(array,n,omg,i+1,array2,sentences)
        array2.pop(i)
    return sentences
a = input("Enter string: ")
x = a.split()
n = len(x)
i=1
stringer=""
while (i<=n):     #here i means the number of words required to make a sentence, i assumed 1 word is also a sentence
    stringer=stringer + "sentences with "+ str(i)+ " words" + "\n"
    bro(x,n,i)
    i=i+1
print(stringer.strip())
            
            

from pyscript import display
from pyweb import pydom
import random

def loadPyContent(event):
    d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']    

    text = "meaning"
    tl = len(text)

    # get random nums
    r = random.randrange(1*(10**999), 1*(10**1000))
    r = str(r)
    tab = []
    
    # turn random numbers into text
    for i in range(len(r)):
        if i % 2 != 0:
            num = int(r[i-1]+r[i])
            if num <= 25:
                tab.append(d[num])
    
    #print("\nThere are", len(tab), "recognizable numbers in a randomly generated pool of", len(r), ".")
    lentab = len(tab)
    lenr = len(r)
    
    # Way of getting string amount 1:
    ta = [0] * tl
    words = []
    
    for j in tab:
        for i in range(tl):
            if j == text[i]:
                w = []
                for k in text:
                    if k == j:
                        w.append(j)
                    else:
                        w.append("-")
                
                words.append(''.join(w))
                ta[i] += 1
    
    t = 0        
    for i in ta:
        t += i;
    
    #print("There are", ta, text, "'s, which is", "{:.2f}".format((t/len(r))*100), "%.")
        
    # Way of getting string amount 2:
    m = 0
    words = []
    for i in tab:
        if i == text[m % tl]:
            words.append(i)
            m += 1
    
    words = ''.join(words)
    
    #print("Alternatively, there are", "{:.2f}".format(m/tl), "amount of consecutive", text, "'s.\n", words)

    pydom["span#lentab"].html = len(tab)
    pydom["span#lenr"].html = len(r)
    pydom["span#ta"].html = ta
    pydom["span#text"].html = text
    pydom["span#percent"].html = "{:.2f}".format((t/len(r))*100)
    pydom["span#divide"].html = "{:.2f}".format(m/tl)
    pydom["span#words"].html = words
    pydom["span#thisisR"].html = r
    pydom["span#thisisTab"].html = ''.join(tab)
    

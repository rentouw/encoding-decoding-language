#Made by rentouw

lol = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
kol = ['ee-oh','oo-ee','doh','mee','ooh','doon','oh','doo','neoh','poh','tooh','moh','o-ah','seh','deh','noh','gah','lah','laan','teh','tee','gor','tor','mor','dor','geh']
end = []
a= ""

def decode():
  a = input("What is ur word ?")
  L = a.split('-')
  L.append(" ")
  end =[]
  for c in range(len(L)-1):
    x = L[c]
    k=0
    for j in kol:
      if(x=="ee" and L[c+1]=="oh"):
        c = c + 1
        end.append("a")
      elif(x=="oh" and L[c-1]=="ee"):
        c = c
      elif(x=="ee" and L[c-1]=="oo"):
        c = c + 1
        end.append("b")
      elif (x==j):
        end.append(lol[k])
      elif(x=="o" and L[c+1]=="ah"):
        c = c + 1
        end.append("m")
      k= k + 1
      
  end = "".join(end)
  print (end)
    
def encode():
  a = input("What is ur word ?")
  L = list(a)
  end =[]
  k=0
  for x in L:
    k=0
    for j in lol:
      if (x==j):
        end.append(kol[k]+"-")
      k=k+1
  end = "".join(end)
  end = list(end)
  del end[-1]
  end = "".join(end)
  print (end)
    
while (a!="stop"):
  a = input("en/de/stop")
  if(a=="en"):
    encode()
  elif(a=="de"):
    decode()

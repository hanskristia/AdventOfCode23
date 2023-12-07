kortStokk="AKQJT98765432"
def sortering(x):
    if x !=[]: 
        # print("x: ",x)
        ret = []
        for i in x[0]:
            # print(i)
            ret.append(kortStokk.index(i))
        return ret
    
with open("07/input.txt") as fil:
    typeHånd=[[],[],[],[],[],[],[]]
    rank=0
    for linje in fil:
        rank+=1

        kort,by = linje.strip().split(" ")
        # print(kort,by)
        teller={}
        for i in kort:
            if i in teller:
                teller[i]+=1
            else:
                teller[i]=1
        maks=0
        for i in teller.values():
            if i > maks:
                maks=i
        lengde=len(teller)
        if maks==5:
            ## femlike
            typeHånd[0].append((kort,int(by)))
        elif maks==4:
            typeHånd[1].append((kort,int(by)))
        elif maks==3 :
            if lengde==2:
            #Hus
                typeHånd[2].append((kort,int(by)))
            else:
               #tress
                typeHånd[3].append((kort,int(by)))
        elif maks==2:
            if lengde==3:
                #to par
                typeHånd[4].append((kort,int(by)))
            else:
                #et par:
                typeHånd[5].append((kort,int(by)))
        else:
            typeHånd[6].append((kort,int(by)))
    # Så sorteres de etter valør
    for valør in typeHånd:
        
        # print(valør)
        valør.sort(key=sortering)

    løsning=0
    for i in typeHånd:
        for j in i:
            if j:
                løsning+=j[1]*rank
                rank-=1
    print(løsning)

#Vetor
vetor =  [9, 10, -1, 3, 6, 2, 1, -3, 1, 0, -2, 15, 8, -7, 0]
#Função
def Bubble(mika):
    for i in range(len(mika),0,-1):
        for j in range(0,i-1):
            if mika[j] > mika[j+1]:
                aux = mika[j]
                mika[j] = mika[j+1]
                mika[j+1] = aux
    print(mika)
Bubble(vetor)

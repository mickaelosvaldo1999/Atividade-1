#Vetor
vetor =  [9, 10, -1, 3, 6, 2, 1, -3, 1, 0, -2, 15, 8, -7, 0]
#Função
def InsertionSort(mika):
    for j in range(1, len(mika)):
        chave = mika[j]
        i = j-1
        while i>0 and mika[i]>chave:
            mika[i + 1] = mika[i]
            i = i-1
            mika[i+1] = chave
    print(mika)
InsertionSort(vetor)
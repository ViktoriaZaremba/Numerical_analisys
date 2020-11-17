import pandas as pd
import random as rm

list_code_word=[]
list_enc_word=[]
list_error_word=[]
list_error_check=[]

for i in range(10):
    code_word=""
    enc_word=""
    error_word=""
    error_check=""

    code_word=str(input("Input a code word: "))
    list_code_word.append(code_word)
    cnt1=0
    for i in range(len(code_word)):
        if code_word[i]=="1":
            cnt1+=1

    enc_word+=code_word
    if cnt1%2==0:
        enc_word+="0"
    else:
        enc_word+="1"
    print("Encrypyted code word: " + enc_word)
    list_enc_word.append(enc_word)

    error_word+=enc_word
    index = rm.randrange(0, len(code_word))
    print(index)
    if rm.randrange(0, 10)<7:
        if code_word[index]=="1":
            error_word=error_word[:index]+"0"+error_word[index+1:]
        else:
            error_word=error_word[:index]+"1"+error_word[index+1:]
    print("Encrypyted code word with mistake: " + error_word)
    list_error_word.append(error_word)

    cnt2=0
    for i in range(len(code_word)+1):
        if error_word[i]=="1":
            cnt2+=1
    if cnt2%2==0:
        error_check+="Немає"
    else:
        error_check+="Є помилка"
    print(error_check)
    list_error_check.append(error_check)

table=pd.DataFrame({'Code word from LAB3 |': list_code_word,
                    'Encrypted code words |':list_enc_word,
                    'Encrypted code words with error |': list_error_word,
                    'Error check': list_error_check})
print(table)

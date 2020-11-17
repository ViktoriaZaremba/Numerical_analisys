import pandas as pd
import random as rm

list_code_word=[]
list_enc_word=[]
list_error_word=[]
list_error_check=[]

def correct_hemming(code_word):
    code_word = list(code_word)
    wrong_bit = 0
    ins = 0
    cnt = 0
    while 2 ** insert <= len(code_word):
        bit = 2 ** insert
        i = bit - 1
        while i < len(code_word):
            j = i
            while j < i + bit and j < len(code_word):
                if code_word[j] == '1':
                    cnt += 1
                j += 1
            i = j - 1
            i += (bit + 1)
        if cnt % 2 == 1:
            wrong_bit += bit
        ins += 1
        cnt = 0
    if wrong_bit != 0:
        if code_word[wrong_bit - 1] == '1':
            code_word[wrong_bit - 1] = '0'
        elif code_word[wrong_bit - 1] == '0':
            code_word[wrong_bit - 1] = '1'
    r = ''
    return wrong_bit

for i in range(10):
    code_word=""
    enc_word=""
    error_word=""
    error_check=""

    code_word=str(input("Input a code word: "))
    list_code_word.append(code_word)
    code_word = list(code_word)
    insert = 0
    while 2**insert <= len(code_word):
        code_word.insert(2 ** insert - 1, '0')
        insert += 1
    insert = 0
    counter = 0
    while 2 ** insert <= len(code_word):
        bit = 2 ** insert
        i = bit - 1
        while i < len(code_word):
            j = i
            while j < i + bit and j < len(code_word):
                if code_word[j] == '1':
                    counter += 1
                j += 1
            i = j - 1
            i += (bit + 1)
        if counter % 2 == 1:
            code_word[bit - 1] = '1'
        insert += 1
        counter = 0
    res = ''
    enc_word = res.join(code_word)
    print("Encrypyted code word: " + enc_word)
    list_enc_word.append(enc_word)

    error_word+=enc_word
    index = rm.randrange(0, len(error_word))
    print(index)
    if rm.randrange(0, 10)<5:
        if error_word[index]=="1":
            error_word=error_word[:index]+"0"+error_word[index+1:]
        else:
            error_word=error_word[:index]+"1"+error_word[index+1:]
    print("Encrypyted code word with mistake: " + error_word)
    list_error_word.append(error_word)

    error_check=correct_hemming(error_word)
    print(error_check)
    list_error_check.append(error_check)

table=pd.DataFrame({'Code word from LAB3 |': list_code_word,
                    'Encrypted code words |':list_enc_word,
                    'Encrypted code words with error |': list_error_word,
                    'Error check': list_error_check})
print(table)

# 3) O arquivo emails.txt possui uma lista de emails. No entanto, alguns emails não
# foram digitados corretamente e precisam ser corrigidos. Leia o arquivo email.txt e
# crie um novo arquivos emails_invalidos.txt apenas com os emails inválidos.


def verificaEmail() :
    alfaNum = 'abcdefghijklmnopqrstuvwxyz1234567890'
    emailValido = []
    emailInvalido = []
    listaEmail = dados
    for email in listaEmail :
        email = email.strip()
        formatacao = True
        for i in range(len(email)):
            if email[i] == '@' and email[i+1] == '@' or email[0] not in alfaNum or email[i] == '@' and email[i+1] not in alfaNum or '@' not in email or '.' not in email or email[i] == '.' and email[i+1] == '.':
                formatacao = False
        if formatacao == False:
            emailInvalido.append(email)
        else :
            emailValido.append(email)
        #print(emailInvalido,emailValido)
    return emailInvalido


arq = open('email.txt', 'r')
emails_invalidos = open("emails_invalidos.txt", "w")
dados = arq.readlines()
emailInvalido = verificaEmail()

for email in emailInvalido :
    emails_invalidos.writelines(f'{email}\n')
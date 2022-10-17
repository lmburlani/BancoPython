import pickle
import os
import pathlib
class Account :
    accNo = 0
    name = ''
    deposit=0
    type = ''
    
    def createAccount(self):
        self.accNo= int(input("Insira o NÚMERO da conta : "))
        self.name = input("Digite o nome do TITULAR da conta : ")
        self.type = input("Digite o tipo de conta [C/P] : ")
        self.deposit = int(input("Insira o valor inicial(>=500 para Poupança e >=1000 para Corrent"))
        print("\n\n\nConta Criada")
    
    def showAccount(self):
        print("Número da Conta : ",self.accNo)
        print("nome do Titular da Conta : ", self.name)
        print("Tipo de Conta",self.type)
        print("Balance : ",self.deposit)
    
    def modifyAccount(self):
        print("Número da Conta : ",self.accNo)
        self.name = input("Mudar nome do Titular da Conta :")
        self.type = input("Mudar Tipo de Conta :")
        self.deposit = int(input("Depósito :"))
        
    def depositAmount(self,amount):
        self.deposit += amount
    
    def withdrawAmount(self,amount):
        self.deposit -= amount
    
    def report(self):
        print(self.accNo, " ",self.name ," ",self.type," ", self.deposit)
    
    def getAccountNo(self):
        return self.accNo
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit
    

def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tSISTEMA BANCARIO")
    print("\t\t\t\t**********************")

    print("\t\t\t\tFeito por:")
    print("\t\t\t\t Luiz B.")
    input()



def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.accNo," ", item.name, " ",item.type, " ",item.deposit )
        infile.close()
    else :
        print("Não há registros a serem exibidos")
        

def displaySp(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                print("O saldo da sua conta é = ",item.deposit)
                found = True
    else :
        print("Nenhum registro para pesquisar")
    if not found :
        print("Nenhum registro existente com este número")

def depositAndWithdraw(num1,num2): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    amount = int(input("Insira o valor a depositar: "))
                    item.deposit += amount
                    print("Sua conta está atualizada")
                elif num2 == 2 :
                    amount = int(input("Insira o valor a ser sacado: "))
                    if amount <= item.deposit :
                        item.deposit -=amount
                    else :
                        print("Você não pode sacar uma quantia maior")
                
    else :
        print("Nenhum registro para pesquisar")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

    
def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
     
def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
                item.name = input("Insira o nome do Titular da Conta : ")
                item.type = input("Insira o tipo de conta : ")
                item.deposit = int(input("Insira o valor : "))
        
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
   

def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
        
# start of the program
ch=''
num=0
intro()

while ch != 8:
    #system("cls");
    print("\tMENU")
    print("\t1. NOVA CONTA")
    print("\t2. DEPOSITAR")
    print("\t3. SACAR")
    print("\t4. SALDO")
    print("\t5.LISTA DE TODOS OS TITULARES DE CONTA")
    print("\t6. FECHAR CONTA")
    print("\t7. MODIFICAR CONTA")
    print("\t8. SAIR")
    print("\tSelecione sua opção (1-8) ")
    ch = input()
    #system("cls");
    
    if ch == '1':
        writeAccount()
    elif ch =='2':
        num = int(input("\tInsira o número da conta: "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tInsira o número da conta: "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tInsira o número da conta: "))
        displaySp(num)
    elif ch == '5':
        displayAll();
    elif ch == '6':
        num =int(input("\tInsira o número da conta: "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tInsira o número da conta: "))
        modifyAccount(num)
    elif ch == '8':
        print("\tOBRIGADO POR USAR O BANCO")
        break
    else :
        print("Escolha inválida")
    
    ch = input("Digite sua escolha : ")

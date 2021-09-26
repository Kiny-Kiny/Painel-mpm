__recodadoPor__:'KinyCrimson'
cl = '\033[0m';az = '\033[1;94m';cia = '\033[1;36m';cz = '\033[1;37m'

from requests import get;from os import system, execl;from sys import argv, executable;from time import sleep

def restart(): execl(executable, executable, *argv)

def clear(): system('cls||clear')

def consulta(x):
	API={'1': ['https://ipwhois.app/json/', ('%s[%s ! %s]%s Digite o IP: '%(cia,cl,cia,cl))],'2': ['https://viacep.com.br/ws/', ('%s[%s ! %s]%s Digite o CEP: '%(cia,cl,cia,cl))],'3': ['https://www.receitaws.com.br/v1/cnpj/',('%s[%s ! %s]%s Digite o CNPJ: '%(cia,cl,cia,cl))],'4': ['https://apicarros.com/v1/consulta/',('%s[%s ! %s]%s Digite a Placa: '%(cia,cl,cia,cl))]}
	try: api=API[x][0]
	except: print('%s[%s X %s]%s OPÇÃO INVÁLIDA!'%(cia,cl,cia,cl));sleep(3);restart()
	req=input(API[x][1])
	if x in ['2','4']: req=api+req+'/json'
	else: req=api+req
	req=get(req, verify=False).json();clear()
	for item in req: print(item,' : ',req[item])
	input("%sPressione ENTER para continuar"%cia)

def main():
	while True:
		clear()
		option=str(input('''
%s Milícia Pika de Mel

%sCriado por: Swag, MrDiniz,Spyware, Intactox%s
%sGithub: Swag666baby || Spyware0 || mrdiniz88%s
Zap: 556295598220

%s[%s ! %s]%s Escolha uma opção:
    	
%s[%s1%s]%s Consulta de IP
%s[%s2%s]%s Consulta de CEP
%s[%s3%s]%s Consulta de CNPJ
%s[%s4%s]%s Consulta de Placa

>>> %s'''%(cia,'\033[4;37m', cia, '\033[4;37m', cia,cl,cia,cl,cia,cl,cia,cl,cia,cl,cia,cl,cia,cl,cia,cl,cia,cl,cia,cl,cia, cl)))
		consulta(option)

if __name__ =='__main__': main()	

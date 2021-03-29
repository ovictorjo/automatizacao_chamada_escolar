
import pandas as pd 

#rename lista_chamada_t5.txt
with open('lista_chamada_t5.txt','r') as f:
	lista_chamada = [line.strip() for line in f]

#rename lista_presenca_t5.txt
with open('lista_presenca_t5.txt','r') as f:
	lista_presenca = [line.strip() for line in f]

lista_chamada = [x.upper() for x in lista_chamada]
lista_presenca = [x.upper() for x in lista_presenca]

#lista_final = dict.fromkeys(lista_chamada,'P')

def status(chamada,presenca):
	#lista = [x for x in presenca if x in chamada]

	aluno_status = dict.fromkeys(chamada,'F')
	value = ''
	total_respostas = len(presenca)

	for i in range(total_respostas):
		if presenca[i] in chamada:
			aluno_status[presenca[i]] = 'P'

	
	return aluno_status


df = pd.DataFrame((status(lista_chamada,lista_presenca).items()))
df.columns = ['Alunos','Chamada']
df.style.set_properties(**{'text-align': 'left'})

#rename Lista_Chamada_Turma_05_27_03.csv
df.to_csv('Lista_Chamada_Turma_05_27_03.csv')

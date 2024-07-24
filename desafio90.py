# nome: str = str(input("Nome: "))
# media: float = float(input(f"Média de {nome}: "))

# if media <= 7:
#     situacao = "Reprovado"
# else: 
#     situacao = "Aprovado"


# dados = {"nome": nome, "media": media, "situacao": situacao}
# #print(dados["nome"])


# print(f"Nome é igual a {dados["nome"]}")
# print(f"Média é igual a {dados["media"]}")
# print(f"Situação é igual a {dados["situacao"]}")

## Solução

aluno = dict()
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f"Média de {aluno["nome"]}: "))

if aluno['media'] >= 7:
    aluno['situacao'] = "Aprovado"
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = "Recuperacao"
else:
    aluno['situacao'] = "Reprovado"

print('-----')

for k,v in aluno.items():
    print(f"{k} é igual a {v}")
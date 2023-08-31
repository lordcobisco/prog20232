# para criar, cada um usa uma sintaxe, mas na hora de usar, todos usam colchetes []
lista = []
tupla = () # é igual a lista, mas não pode alterar os valores
dicionario = {} # em vez de índices (o número da posição), se usam chaves, que podem ser textos 

# com os dicionários, podemos criar hierarquias 
dicionario['Professores'] = ['André', 'Denis'] 
dicionario['Alunos'] = ['Vitor', 'Luis']

# criando um dicionário já com os valores
pessoalISD = {
    'Professores': ['André', 'Denis', 'Ramon'], # Professores é a chave de acesso para a lista que contém os professores. Estrutura: chave : conteúdo
    'Alunos': {
        'Giovanna': {
            'matricula': 20231010,
            'formacao': 'Psicologia',
            'orientador': 'Ramon'
        },
        'Deyvisom': {
            'matricula': 20231011,
            'formacao': 'CeT',
            'orientador': 'Hougelle'
        }
    }                     
}
aluno = input("Digite o aluno que quer pesquisar: ")
print(pessoalISD['Alunos'][aluno]['matricula'])
# ATIVIDADE 3 
## Questão 1 - Descrição Narrativa LOKOMAT
```
Inicio

Preparação do paciente:

    Coleta de informações antropométricas
		Altura
		Peso
		Comprimento de membros inferiores
		Circunferência Tornozelo
		Circunferência Perna
		Circunferência Coxa
		Circunferência Cintura
        Colocação de Acessórios
		Transferência da cadeira de rodas para tatame
			Vestir colete
			**Se** colete não estiver disponível em tamanho adequado:
				Providenciar colete de tamanho apropriado
			**Senão**
				Ajustar tiras
			Vestir almofadas de proteção virilha
		Transferência paciente tatame cadeira de rodas
	
Configuração do Sistema Lokomat:

	Ligar Sistema
	**Se** Sistema ligado:
		Criar novo usuário
		Inserir informações antropométricas
	**Senão**
		Ligar Sistema
	Verificar funcionamento/Integridade
		Esteira
		Guincho
		Lokomat

Conexão do paciente com o Lokomat:

	Abertura de porta de acesso ao dispositivo
	Deslocamento com a cadeira de rodas até o interior do dispositivo
	Colocação e fixação de braceletes nos membros inferiores
	Fixação do guincho no colete
	Inicio da suspensão do paciente
	Ajuste colete
	Retirada cadeira 
	Suspensão total
	Fechamento do acesso ao dispositivo
		**Se** tudo realizado:
			 inicio de protocolo caminhada
		**Se não**
		 	 Conexão do paciente com Lokomat

Inicio do protocolo caminhada:

	Definir Tempo
	Iniciar movimento do lokomat
	iniciar funcionamento esteira
	Iniciar apoio parcial paciente
	apoio total
	monitoramento da caminhada
        **Se** resposta fisiológica for boa:
	        aumento de velocidade
        **Senão**
	        reduz velocidade
   	 **Enquanto** tempo atual - tempo de definido de sessão maior que zero:
		monitoramento da caminhada

Finalização do protocolo:

	Desliga esteira e lokomat
	Suspende paciente
	Abertura acesso para dispositivo
	Acopla cadeira
		Apoia paciente na cadeira
		Solta colete do guincho
		Remover colete
		Remover braceletes
	Paciente é transferido até o tatame
		Retirada do colete
	Paciente é transferido para cadeira de rodas

Fim
```

## Questão 1 - Descrição Narrativa ZeroG

```
inicio

Preparação do Paciente:

	Coleta de Informações Antropométricas do paciente
		Peso
  		Altura
    		Circunferência cintura
	Vestir colete suporte
 	Ajuste de colete para se encaixar confortavelmente em torno de seu tronco
	colete é conectado a um sistema de trilhos suspenso no teto.

Inicio de Atividades:

	**Se** o paciente estiver pronto e confortável
		Realiza atividades terapêuticas
	**Senão**
		Ajuste colete

Monitoramento de Atividades:

	Enquanto tempo atual - tempo definido for maior que zero:
		Realiza atividades terapêuticas
		Ajusta a quantidade de suporte de peso conforme necessário
	
Final da sessão:

	O terapeuta verifica o progresso:
	**Se** o progresso for satisfatório
		O terapeuta posiciona o paciente em local seguro
	**Senão**
		O terapeuta posiciona o paciente em local seguro
		Ajusta estratégia para a próxima sessão

Fim

````

## Questão 2 - Memória,Processamento,Entrada/saida LOKOMAT

|**Memoria:**|
|------------|
|Altura (variável real)|
|Peso (variável real)|
|Tempo de sessão ( variável real)|
|Comprimento membros inferiores (variável|
|Circunferência Tornozelos (variável real|
|Circunferencia Pernas (variável real)|
|Circunferencia Coxas (variável real)|
|Circunferencia Cintura (variável real)|
|EquipamentoColocado (variável booleana)|
|AlmofadasDisponiveis (variável booleana)|
|RespostaFisiologicaBoa (variável booleana)|

|**Processamento:**|
|------------------|
|Coleta de informações antropométricas|
|Providenciar colete de tamanho apropriado (condicional)|
|Ajustar tiras (condicional)|
|Providenciar almofadas de proteção (condicional)|
|Transferência paciente tatame cadeira de rodas|
|Ligar Sistema|
|Criar novo usuário|
|Inserir informações antropométricas|
|Verificar funcionamento/Integridade|
|Abertura de porta de acesso ao dispositivo|
|Deslocamento com a cadeira de rodas até o interior do dispositivo|
|Colocação e fixação de braceletes nos membros inferiores|
|Fixação do guincho no colete|
|Inicio da suspensão do paciente|
|Ajuste colete|
|Retirada cadeira|
|Supensão total|
|Fechamento do acesso ao dispositivo|
|Inicia movimento do lokomat|
|Inicia funcionamento esteira|
|Inicia apoio parcial paciente|
|Apoio total|
|Aumento de velocidade (condicional)|
|Reduz velocidade (condicional)|
|Repetir até o fim da sessão|
|Monitoramento da caminhada|
|Desliga esteira e lokomat|
|Suspende paciente|
|Abertura acesso para dispositivo|
|Acopla cadeira|
|Apoia paciente na cadeira|
|Solta colete do guincho|
|Solta-se gradualmente tiras do colete|
|Solta-se braceletes|
|Paciente é transferido até o tatame|
|Retirada do colete|
|Paciente é transferido para cadeira de rodas|

|**Entrada/saida:**|
|------------------|
|Teclado|
|Mouse|
|Monitor|
|Indicações Sonoras terapeuta|
|Indicações Sonoras Paciente|

## Questão 2 - Memória,Processamento,Entrada/Saída ZeroG

|**Memória:**|
|------------|
|Altura (variável real)|
|Peso (variável real)|
|Circunferência cintura (variável real)|
|Paciente confortável (variável booleana)|
|Paciente desconfortável (variável booleana)|
|Tempo de sessão (variável real)|
|Quantidade Suporte (variável real)|
|Progresso satisfatório (Condicional)|
|Progresso não satisfatório (Condicional)|

|**Processamento:**|
|------------------|
|Vestir colete|
|Ajustar colete|
|Conectar sistema aos trilhos| 
|Ajustar suporte|
|Relizar a terapeutica| 
|Verificar progresso|

|**Entradas/Saidas:**|
|--------------------|
|Teclado|
|Mouse|
|Monitor|
|Informações sonoras terapeuta|
|Informações sonoras Paciente|
|Informações visuais terapeuta|
|Informações visuais paciente|

## Questão 3 - Destacar o que seriam as estruturas de repetição e de decisão:

|**Lokomat**|
|-----------|
|1- Estruturas de decisão:|
|                         |
|**Se** colete não estiver disponível em tamanho adequado|
|Providenciar colete de tamanho apropriado|
|**Senão**|
|Ajustar tiras|
|             |    
|Ligar Sistema|
|**Se** Sistema ligado|
|Criar novo usuário|
|Inserir informações antropométricas|
|**Senão**|
|Ligar Sistema|
|             |
|**Se** tudo realizado|
|inicio de protocolo caminhada|
|**Se não**|
|Conexão do paciente com Lokomat|
|                               |    
| **Se** resposta fisiológica for boa|
|aumento de velocidade|
|**Senão**|
|reduz velocidade|
||
|2- Estrutura de repetição|
| **Enquanto** Tempo atual - Tempo definido maior que zero|
|monitoramento da caminhada|

|**Zero G**|
|----------|
|1- Estruturas de decisão|
||
|**Se** o paciente estiver pronto e confortável|
|Realiza atividades terapêuticas|
|**Senão**|
|Ajuste colete|
|**Se** o progresso for satisfatório|
|O terapeuta posiciona o paciente em local seguro|
|**Senão**|
|O terapeuta posiciona o paciente em local seguro|
|Ajusta estratégia para a próxima sessão|
|2- Estrutura de repetição|
||
|**Enquanto** tempo atual - tempo definido na sessão maior que zero|
|Realiza atividades terapêuticas|
|Ajusta a quantidade de suporte de peso conforme necessário|
	
## Questão 5 - Pseudocódigo
| LOKOMAT |
```
Algoritmo LOKOMAT

**Var** Altura,Peso,Comprimento de membros inferiores,Circunferência Tornozelo,Circunferência Perna,Circunferência Coxa,Circunferência Cintura,Tempodesessão: **real**,TamanhoColete:**Literal**,SistemaLigado,TudoRealizado,RespostaFisiologica:**Booleano**

**Inicio**

	**def** Coleta de informações antropométricas:

		**Leia** Altura

		**Leia** Peso

		**Leia** Comprimento de membros inferiores

		**Leia** Circunferência Tornozelo

		**Leia** Circunferência Perna

		**Leia** Circunferência Coxa

		**Leia** Circunferência Cintura

		**Leia** Tempo de sessão

	**def**Colocação de Acessórios:

		Transferência da cadeira de rodas para tatame

		Vestir colete

		**Se** colete não estiver disponível em tamanho adequado

			Providenciar colete de tamanho apropriado

		**Senão**

			Ajustar tiras

		Vestir almofadas de proteção virilha

		Transferência paciente tatame cadeira de rodas

	**def** Configuração do Sistema Lokomat:`

		Ligar Sistema

		**Se** Sistema ligado:

			Criar novo usuário

			Inserir informações antropométricas

		**Senão**

			Ligar Sistema

		Verificar funcionamento/Integridade

			Esteira

			Guincho

			Lokomat

	**def** Conexão do paciente com o Lokomat:

		Abertura de porta de acesso ao dispositivo

		Deslocamento com a cadeira de rodas até o interior do dispositivo

		Colocação e fixação de braceletes nos membros inferiores

		Fixação do guincho no colete
	
		Inicio da suspensão do paciente

		Ajuste colete

		Retirada cadeira 

		Suspensão total

		Fechamento do acesso ao dispositivo

		**Se** tudo realizado:

			inicio de protocolo caminhada

		**Senão**

			Conexão do paciente com Lokomat

	**def** Inicio do protocolo caminhada:

		**Leia** Temposessao

		Iniciar movimento do lokomat

		iniciar funcionamento esteira

		Iniciar apoio parcial paciente
	
		apoio total

		monitoramento da caminhada

		**Se** resposta fisiológica for boa:

			aumento de velocidade

		**Senão**

			reduz velocidade

		**Enquanto** tempo atual - tempo de definido de sessão maior que zero:

			monitoramento da caminhada

	**def** Finalização do protocolo:

		Desliga esteira e lokomat

		Suspende paciente

		Abertura acesso para dispositivo

		Acopla cadeira

		Apoia paciente na cadeira

		Solta colete do guincho

		Remover colete

		Remover braceletes

		Paciente é transferido até o tatame

		Retirada do colete

		Paciente é transferido para cadeira de rodas
		**fim_se**
		**Fim**
```
| Zero G |
```

Algoritmo ZeroG

**Var** Altura,Peso,Circunferência Cintura,Tempodesessão: **real**,TamanhoColete:**Literal**,Monitoramentoatividade:**Booleano**


**inicio**

**def** Preparação do Paciente:
	**Leia** Peso

  	**Leia** Altura

    	**Leia** Circunferência cintura

	Vestir colete suporte
 	
	Ajuste de colete para se encaixar confortavelmente em torno de seu tronco
	
	Conectar o colete ao sistema de trilhos suspenso no teto.

**def** Inicio de Atividades:

	**Se** o paciente estiver pronto e confortável

		Realiza atividades terapêuticas

	**Senão**

		Ajuste colete

**def** Monitoramento de Atividades:

	**Enquanto** tempo atual - tempo definido for maior que zero:
		
		Realiza atividades terapêuticas
		
		Ajusta a quantidade de suporte de peso conforme necessário
	
**def** Final da sessão:

	O terapeuta verifica o progresso:
	
	**Se** o progresso for satisfatório
		
		O terapeuta posiciona o paciente em local seguro
	
	**Senão**
		
		O terapeuta posiciona o paciente em local seguro
		
		Ajusta estratégia para a próxima sessão
**fim_se**
**Fim**

````

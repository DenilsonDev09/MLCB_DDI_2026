--- RESULTADOS DO LAB 01 ---
Mensagem: 'Quero consultar quanto dinheiro tenho' ==> Intenção Predita: [fazer_pix]
Mensagem: 'Pode me ajudar a fazer um pix?' ==> Intenção Predita: [fazer_pix]
Mensagem: 'Gostaria de cancelar meu cartão de crédito' ==> Intenção Predita: [cancelar_conta]

# 1 - Avaliem os resultados e verifiquem se os resultados foram corretos ou incorretos. Coloque a resposta no arquivo do relatório do laboratório
R: Parcial pois teve dois acertos e um erro.

# 2 - Detectado algum erro, qual seria a maneira mais correta de melhorar o resultado do algoritmo?
R: Usar o erro para ensinar o modelo, ou de como não devolver a resposta incorreta.

# 3 - Detalhe a função do LogisticRegression no algorítmo.
R: Ela calcula a probabilidade da resposta baseada na porcentagem reservada para teste.




--- RESULTADOS DO LAB 02 ---
Mensagem de Teste: 'Gostaria de devolver o produto que comprei'
Intenção Predita: troca_devolucao

--- Distribuição de Probabilidades por Classe ---
Classe [duvida_frete]: 27.99%
Classe [rastrear_pedido]: 24.54%
Classe [troca_devolucao]: 47.46%

# 1 - Avaliem os resultados e verifiquem se os resultados foram corretos ou incorretos. Coloque a resposta no arquivo do relatório do laboratório
R: Correto, ele acertou a intenção do usuario.

# 2 - Detectado algum erro, qual seria a maneira mais correta de melhorar o resultado do algoritmo?
R: Alimentar o dataset com mais informações e exemplos de situações similares ao "Erro" encontrado e ir adicionando mais rotas.

# 3 - Detalhe a função do Naive Bayes no algorítmo.
R: Calcula a probabilidade da presença de uma mesma palavra encontrada mais de uma vez.




--- RESULTADOS DO LAB 03 ---

Acurácia do Modelo: 33.33%

#========== PRODUÇÃO DO RELATÓRIO:==============
# Para a entrega completa deste LAB03 você precisa colar o código corrigido com os TODOs preenchidos, a acurácia obtida e responder:
# 1 - Qual foi a acurácia obtida pelo modelo no conjunto de teste e por que, em um dataset tão pequeno (9 exemplos), essa métrica pode ser enganosa?
R: Acurácia do Modelo: 33.33%, sim pois ele não recebe dados o suficiente para retornar um valor correto.

# 2 - Como o modelo de Árvore de Decisão (DecisionTreeClassifier) toma a decisão de separar as intenções do usuário?
R: O DecisionTreeClassifier separa as intenções criando regras de decisão sobre as características presentes nos textos.

# 3 - Qual é o risco de utilizar uma Árvore de Decisão sem limite de profundidade (max_depth) em datasets de texto maiores?
R: Quanto mais grande for o dataset de texto, maior o risco de a árvore memorizar o conjunto de treinamento em vez de aprender padrões úteis para novas mensagens.




--- RESULTADOS DO LAB 04 ---

==================================================
--- MOTOR DE NLU: AGÊNCIA DE VIAGENS ---
==================================================
Acurácia no conjunto de teste: 33.33%

--- PREDIÇÃO DE MENSAGENS INÉDITAS ---
Mensagem: 'Gostaria de saber o valor para voar até Paris'
==> Intenção Predita: [comprar_passagem]

Mensagem: 'Quero cancelar o bilhete que comprei ontem'
==> Intenção Predita: [cancelar_reserva]

Mensagem: 'Me transfira para um suporte humano, por favor'
==> Intenção Predita: [falar_atendente]

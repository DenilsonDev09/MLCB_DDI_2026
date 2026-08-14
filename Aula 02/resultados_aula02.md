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



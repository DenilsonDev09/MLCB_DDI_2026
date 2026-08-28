           precision    recall  f1-score   support

logistica_entregas       1.00      1.00      1.00         6
       reclamacoes       1.00      1.00      1.00         6
           suporte       1.00      1.00      1.00         6
 trocas_devolucoes       1.00      1.00      1.00         6
            vendas       1.00      1.00      1.00         6

          accuracy                           1.00        30
         macro avg       1.00      1.00      1.00        30
      weighted avg       1.00      1.00      1.00        30

[[6 0 0 0 0]
 [0 6 0 0 0]
 [0 0 6 0 0]
 [0 0 0 6 0]
 [0 0 0 0 6]]

=== INICIANDO BATERIA DE TESTES (10 INPUTS OBRIGATÓRIOS) ===

[Teste 1/10]
Digite a frase do cliente: A solução apresentada não resolveu o meu problema

Bot [Intenção: LOGISTICA_ENTREGAS | Confiança: 100.0%]: Simulador de crédito aberto. Qual o valor do bem que deseja financiar?

[Teste 2/10]
Digite a frase do cliente: 9789789

Bot: [FALLBACK - Confiança baixa: 33.3%]
Desculpe, não consegui entender sua solicitação. Por favor, aguarde um momento enquanto encaminho você para um atendente humano...

[Teste 3/10]
Digite a frase do cliente: eu

Bot: [FALLBACK - Confiança baixa: 33.3%]
Desculpe, não consegui entender sua solicitação. Por favor, aguarde um momento enquanto encaminho você para um atendente humano...

[Teste 4/10]
Digite a frase do cliente: eu nao sei

Bot [Intenção: RECLAMACOES | Confiança: 66.7%]: Simulador de crédito aberto. Qual o valor do bem que deseja financiar?

[Teste 5/10]
Digite a frase do cliente: não resolveu o meu problema

Bot [Intenção: LOGISTICA_ENTREGAS | Confiança: 100.0%]: Simulador de crédito aberto. Qual o valor do bem que deseja financiar?

[Teste 6/10]
Digite a frase do cliente: problema

Bot: [FALLBACK - Confiança baixa: 33.3%]
Desculpe, não consegui entender sua solicitação. Por favor, aguarde um momento enquanto encaminho você para um atendente humano...

[Teste 7/10]
Digite a frase do cliente: resolveu

Bot: [FALLBACK - Confiança baixa: 33.3%]
Desculpe, não consegui entender sua solicitação. Por favor, aguarde um momento enquanto encaminho você para um atendente humano...

[Teste 8/10]
Digite a frase do cliente: nao resolveu

Bot [Intenção: RECLAMACOES | Confiança: 66.7%]: Simulador de crédito aberto. Qual o valor do bem que deseja financiar?

[Teste 9/10]
Digite a frase do cliente: terrivel resolveu

Bot: [FALLBACK - Confiança baixa: 33.3%]
Desculpe, não consegui entender sua solicitação. Por favor, aguarde um momento enquanto encaminho você para um atendente humano...

[Teste 10/10]
Digite a frase do cliente: a solução apresentada

Bot: [FALLBACK - Confiança baixa: 33.3%]
Desculpe, não consegui entender sua solicitação. Por favor, aguarde um momento enquanto encaminho você para um atendente humano...

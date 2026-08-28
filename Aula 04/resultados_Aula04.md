--- RESULTADOS DO LAB 01 (AULA 04) --- 
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

--- RESULTADOS DO LAB 02 (AULA 04) --- 

=== CLASSIFICATION REPORT ===
                    precision    recall  f1-score   support

logistica_entregas       0.80      0.67      0.73         6
       reclamacoes       1.00      0.33      0.50         6
           suporte       1.00      1.00      1.00         6
 trocas_devolucoes       0.62      0.83      0.71         6
            vendas       0.67      1.00      0.80         6

          accuracy                           0.77        30
         macro avg       0.82      0.77      0.75        30
      weighted avg       0.82      0.77      0.75        30


=== CONFUSION MATRIX ===
[[4 0 0 0 2]
 [1 2 0 3 0]
 [0 0 6 0 0]
 [0 0 0 5 1]
 [0 0 0 0 6]]

=== INICIANDO BATERIA DE TESTES (8 INPUTS) ===

[Teste 1/8]
Digite a frase do cliente: quero debolver

Bot [Intenção: VENDAS | Confiança: 100.0%]: Temos uma promoção.

[Teste 2/8]
Digite a frase do cliente: manifesto comunista

Bot [Intenção: TROCAS_DEVOLUCOES | Confiança: 100.0%]: Me passe o código do pedido.

[Teste 3/8]
Digite a frase do cliente: onde esta minha entrega

Bot [Intenção: TROCAS_DEVOLUCOES | Confiança: 100.0%]: Me passe o código do pedido.

[Teste 4/8]
Digite a frase do cliente: emprendedorismo 

Bot [Intenção: TROCAS_DEVOLUCOES | Confiança: 100.0%]: Me passe o código do pedido.

[Teste 5/8]
Digite a frase do cliente: tenho uma reclamação

Bot [Intenção: RECLAMACOES | Confiança: 100.0%]: Desculpe pelo transtorno. Iremos encaminhar sua reclamação para o Denilson do TI.

[Teste 6/8]
Digite a frase do cliente: tenho uma troca pra fazer

Bot [Intenção: RECLAMACOES | Confiança: 100.0%]: Desculpe pelo transtorno. Iremos encaminhar sua reclamação para o Denilson do TI.

[Teste 7/8]
Digite a frase do cliente: problema

Bot [Intenção: TROCAS_DEVOLUCOES | Confiança: 100.0%]: Me passe o código do pedido.

[Teste 8/8]
Digite a frase do cliente: facil

Bot [Intenção: TROCAS_DEVOLUCOES | Confiança: 100.0%]: Me passe o código do pedido.


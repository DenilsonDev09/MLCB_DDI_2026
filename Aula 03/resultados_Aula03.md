--- RESULTADOS DO LAB 01 (AULA 03) ---
Mensagem: 'Preciso urgente da segunda via da fatura'
Intenção Predita: [segunda_via]
Vocabulário Filtrado (sem stopwords): ['2a', '2a via', 'aberto', 'acordo', 'acordo pagar', 'alterar', 
'alterar endereço', 'app', 'atrasada', 'atualizo', 'atualizo dados', 'boleto', 'cadastramento', 'dados', 
'dados residenciais', 'débito', 'débito aberto', 'dívida', 'emitir', 'emitir segunda', 'endereço', 'endereço cadastramento', 
'fatura', 'fatura atrasada', 'fazer', 'fazer um', 'gostaria', 'gostaria alterar', 'negociar', 'negociar pagamento', 
'no', 'no app', 'onde', 'onde atualizo', 'pagamento', 'pagamento dívida', 'pagar', 'pagar débito', 'posso', 
'posso emitir', 'residenciais', 'residenciais no', 'segunda', 'segunda via', 'um', 'um acordo', 'via', 'via boleto', 'via fatura']

#========== PRODUÇÃO DO RELATÓRIO:==============
# 1 - Qual o impacto da remoção de stopwords no tamanho do vocabulário do modelo?
R: Ele sofrerá impacto na precisão e perde tempo na execuçâo. 

# 2 - O que significa a configuração ngram_range=(1, 2) no TfidfVectorizer?
R: Ele faz a junção das palavras para um melhor contexto.

# 3 - Como a remoção de palavras genéricas ajuda a evitar classificações incorretas?
R: Evita de fazer confusão baseado nessas palavras genéricas, que não importam para o contexto
# Todos os resultados devem ser inseridos no arquivo resultados_aula03.md



--- RESULTADOS DO LAB 02 (AULA 03) ---

--- Relatório de Classificação ---
                     precision    recall  f1-score   support

horario_atendimento       0.50      1.00      0.67         1
        localizacao       0.00      0.00      0.00         1
    troca_devolucao       0.00      0.00      0.00         1

           accuracy                           0.33         3
          macro avg       0.17      0.33      0.22         3
       weighted avg       0.17      0.33      0.22         3

--- Matriz de Confusão ---
[[1 0 0]
 [1 0 0]
 [0 1 0]]

 #========== PRODUÇÃO DO RELATÓRIO:==============
# 1 - O que representam as métricas Precision, Recall e F1-Score no relatório?
R:Precision - Quantidade de acerto do eixo Y
Recall - A porcertagem de acertos do contexto com a intenção 
F1-Score - média de precisão e recall

# 2 - Como interpretar a diagonal principal da Matriz de Confusão?
R: total de acertos

# 3 - Por que a acurácia isolada pode ser enganosa quando temos classes desbalanceadas?
R: pois podemos ter 100% de acerto com uma classe, porem nenhum acerto em outra, pois não foi testado ✌

# Todos os resultados devem ser inseridos no arquivo resultados_aula03.md
#========== FIM ==============



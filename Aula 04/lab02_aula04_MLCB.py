import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# 1. Carregar dataset do CSV
# ============================================================

df = pd.read_csv('dataset_moveis_100.csv')


# ============================================================
# 2. Divisão Treino e Teste
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    df['texto'],
    df['intencao'],
    test_size=0.30,
    random_state=42,
    stratify=df['intencao']
)


# ============================================================
# 3. Montar Pipeline
# ============================================================

pipeline_nlu = Pipeline([
    ('vectorizer', TfidfVectorizer(
        ngram_range=(1, 2)
    )),
    ('classifier', DecisionTreeClassifier(
        random_state=42
    ))
])


# ============================================================
# 4. Treinar Pipeline
# ============================================================

pipeline_nlu.fit(X_train, y_train)


# ============================================================
# 5. Avaliação do modelo
# ============================================================

y_pred = pipeline_nlu.predict(X_test)

print("\n=== CLASSIFICATION REPORT ===")
print(classification_report(y_test, y_pred))

print("\n=== CONFUSION MATRIX ===")
print(confusion_matrix(y_test, y_pred))


# ============================================================
# 6. Configuração dos limiares
# ============================================================

LIMIAR_CONFIANCA = 0.70
LIMIAR_SIMILARIDADE = 0.20


# ============================================================
# 7. Preparar TF-IDF dos dados de treinamento
# ============================================================

vectorizer = pipeline_nlu.named_steps['vectorizer']

X_train_tfidf = vectorizer.transform(X_train)


# ============================================================
# 8. Bateria de testes
# ============================================================

print("\n=== INICIANDO BATERIA DE TESTES (8 INPUTS) ===")


for i in range(1, 9):

    print(f"\n[Teste {i}/8]")

    # ========================================================
    # Entrada do usuário
    # ========================================================

    frase = input("Digite a frase do cliente: ").strip()


    # ========================================================
    # Probabilidade
    # ========================================================

    probs = pipeline_nlu.predict_proba([frase])[0]

    maior_prob = np.max(probs)


    # ========================================================
    # Intenção prevista
    # ========================================================

    intencao = pipeline_nlu.predict([frase])[0]


    # ========================================================
    # Similaridade
    # ========================================================

    frase_tfidf = vectorizer.transform([frase])

    similaridades = cosine_similarity(
        frase_tfidf,
        X_train_tfidf
    )[0]

    maior_similaridade = np.max(similaridades)


    # ========================================================
    # Regra de decisão
    # ========================================================

    if (
        maior_prob >= LIMIAR_CONFIANCA
        and maior_similaridade >= LIMIAR_SIMILARIDADE
    ):

        confianca = maior_prob * 100

        if intencao == "vendas":

            resposta = "Temos uma promoção."

        elif intencao == "suporte":

            resposta = (
                "Comente qual é a sua dúvida que o suporte "
                "já vai te atender."
            )

        elif intencao == "trocas_devolucoes":

            resposta = "Me passe o código do pedido."

        elif intencao == "reclamacoes":

            resposta = (
                "Desculpe pelo transtorno. Iremos encaminhar "
                "sua reclamação para o Denilson do TI."
            )

        elif intencao == "logistica_entregas":

            resposta = "Iremos colocar prioridade na entrega."

        else:

            resposta = (
                "Desculpe, não consegui entender sua solicitação."
            )


        # ====================================================
        # Mostrar somente resposta + confiança
        # ====================================================

        print(
            f"Bot: {resposta}"
        )

        print(
            f"Confiabilidade: {confianca:.1f}%"
        )


    # ========================================================
    # FALLBACK
    # ========================================================

    else:

        print(
            "Bot: Desculpe, não consegui entender sua solicitação. "
            "Por favor, aguarde um momento enquanto encaminho "
            "você para um atendente humano..."
        )

        print(
            f"Confiabilidade: {maior_prob * 100:.1f}%"
        )
]

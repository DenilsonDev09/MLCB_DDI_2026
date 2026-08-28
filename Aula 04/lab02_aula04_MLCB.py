import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split


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
# TODO 1: Montar a Pipeline utilizando
# TfidfVectorizer e DecisionTreeClassifier
# ============================================================

pipeline_nlu = Pipeline([
    ('vectorizer', TfidfVectorizer(ngram_range=(1, 2))),
    ('classifier', DecisionTreeClassifier(
        random_state=42
    ))
])


# ============================================================
# TODO 2: Treinar a pipeline com os dados de treino
# ============================================================

pipeline_nlu.fit(X_train, y_train)


# ============================================================
# TODO 3: Gerar as predições nos dados de teste
# e exibir classification_report e confusion_matrix
# ============================================================

y_pred = pipeline_nlu.predict(X_test)

print("\n=== CLASSIFICATION REPORT ===")
print(classification_report(y_test, y_pred))

print("\n=== CONFUSION MATRIX ===")
print(confusion_matrix(y_test, y_pred))


# ============================================================
# Configuração do limiar de confiança
# ============================================================

LIMIAR_CONFIANCA = 0.50


# ============================================================
# Bateria de testes
# ============================================================

print("\n=== INICIANDO BATERIA DE TESTES (8 INPUTS) ===")


for i in range(1, 9):

    print(f"\n[Teste {i}/8]")

    # ========================================================
    # TODO 4: Solicitar a frase do usuário via teclado
    # ========================================================

    frase = input("Digite a frase do cliente: ").strip()


    # ========================================================
    # TODO 5: Extrair probabilidades e classe prevista
    # ========================================================

    probs = pipeline_nlu.predict_proba([frase])[0]

    maior_prob = np.max(probs)

    intencao = pipeline_nlu.predict([frase])[0]


    # ========================================================
    # TODO 6: Regra de decisão
    # ========================================================

    if maior_prob >= LIMIAR_CONFIANCA:

        print(
            f"\nBot [Intenção: {intencao.upper()} | "
            f"Confiança: {maior_prob * 100:.1f}%]: ",
            end=""
        )

        if intencao == "vendas":

            print("Temos uma promoção.")

        elif intencao == "suporte":

            print(
                "Comente qual é a sua dúvida que o suporte "
                "já vai te atender."
            )

        elif intencao == "trocas_devolucoes":

            print("Me passe o código do pedido.")

        elif intencao == "reclamacoes":

            print(
                "Desculpe pelo transtorno. Iremos encaminhar "
                "sua reclamação para o Denilson do TI."
            )

        elif intencao == "logistica_entregas":

            print("Iremos colocar prioridade na entrega.")



    # ========================================================
    # Fallback
    # ========================================================

    else:

        print(
            f"\nBot: [FALLBACK - Confiança baixa: "
            f"{maior_prob * 100:.1f}%]"
        )

        print(
            "Desculpe, não consegui entender sua solicitação. "
            "Por favor, aguarde um momento enquanto encaminho "
            "você para um atendente humano..."
        )

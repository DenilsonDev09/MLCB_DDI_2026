--------4 FRASES DE TESTE ---------
FRASE 1: Qual é a graça ? 
Intenção: suporte_manutencao
Confiança: 53.7%
Status da Decisão: IDENTIFICADO (suporte_manutencao)

FRASE 2: Quero negociar meu apartamento
Intenção: 2via_boleto_contrato
Confiança: 58.9%
Status da Decisão: IDENTIFICADO (2via_boleto_contrato)

FRASE 3: quanto esta um apartamento na zona sul ?
Intenção: comprar_imovel
Confiança: 70.8%
Status da Decisão:  IDENTIFICADO (comprar_imovel)

FRASE 4: estou com problema de vazamento de dados no meu apartamento 
Intenção: suporte_manutencao
Confiança: 66.5%
Status da Decisão:  IDENTIFICADO (suporte_manutencao)

-------- LAB 01 ---------
FRASE 1: Gostaria do boleto!
Intenção: 2via_boleto_contrato
Confiança: 40.0%
Status da Decisão: UNCERTAIN (Fallback Acionado)

FRASE 2: Preciso de suporte técnico para consertar vazamento.
Intenção: comprar_imovel
Confiança: 100.0%
Status da Decisão: IDENTIFICADO (comprar_imovel)

---------LAB 02----------

FRASE 1: qual a disponibilidade do apartamento
Intenção: 2via_boleto_contrato
Confiança: 40.0%
Status da Decisão: UNCERTAIN (Fallback Acionado)

FRASE 2: Preciso do boleto pra ontem
Intenção: suporte_manutencao
Confiança: 100.0%
Status da Decisão: IDENTIFICADO (suporte_manutencao)

--------LAB 03----------

FRASE 1: Preciso de suporte técnico para consertar vazamento.
Intenção: suporte_manutencao
Confiança: 100.0%
Status da Decisão: IDENTIFICADO (suporte_manutencao) (Corte mínimo: 65%)

FRASE 2: Onde consigo arrrumar um apartamento pra ontem
Intenção: suporte_manutencao
Confiança: 100.0%
Status da Decisão: IDENTIFICADO (suporte_manutencao) (Corte mínimo: 65%)

-------LAB 04--------

FRASE 1: quero cancelar meu contrato e nunca mais assinar
Intenção: cancelar_contrato
Confiança: 100.0%
Status da Decisão:  IDENTIFICADO (cancelar_contrato) (Corte mínimo: 65%)

FRASE 2: como faço para cancelar essa budega
Intenção: 2via_boleto_contrato
Confiança: 40.0%
Status da Decisão:  UNCERTAIN (Fallback Acionado) (Corte mínimo: 65%)

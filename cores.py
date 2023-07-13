"""Método ANSI - escape sequence"""

"""Estrutura para utilizar:

"\033[cod do estilo;cod do texto;cod cor background+m]
cod do estilo: negrito, itálico, sublinhado, etc.
cod do texto: fonte texto
cod background: cor do fundo
m: sempre precisa ser colocada após e junta ao ultimo código

ex.: \033[0;33;44m
cod estilo:
0 - sem estilo
1 - negrito
4 - sublinhado
7 - negative (inverte cor da fonte com cor do fundo)
cod texto:
30 - branco
31 - vermelho
32 - verde
33 - amarelo
34 - azul
35 - magenta
36 - turquesa
37 - cinza (cor padrão do terminal)
cores background:
40 a 47, mesmas cores respectivamente aos de texto

esses códigos são opcionais e suas ordens podem ser trocadas"""

\033[0;30;41m]
\033[4;33;44m]
\033[1;35;43m]
\033[30;42m] #sem estilo, considera o estilo do terminal
\033[m] #desfaz todas as configurações de cores e volta para padrão do terminal
\033[7;30] #usei inversor para tornar trocar cor da letra com o fundo
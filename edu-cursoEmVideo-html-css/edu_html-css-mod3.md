 # Apendizados adquiridos do curso de HTML e CSS do professor Guanabara - Curso em vídeo.
- Por que aprender?
sinto que preciso relembrar e exercitar meus aprendizados passados revendo esse curso. como esses conceitos são a base da programação, acho interessante reforçar a minha base nelas.

 ## Notas
 - número na frente de um lorem (ex.: lorem20) determina quantas palavras o lorem vai ter

 ## HTML
- <abbr tittle=""> -> apresenta o significado de abreviações do texto
- <table> -> cria uma tabela

 #### Hierarquia de tabelas pequenas
 TABLE = TABELA
    TABLE ROW = LINHA DE TABELA
        TABLE HEADER = CABEÇALHO DE TABELA
        TABLE DATA = DADO DE TABELA

#### Hierarquia de tabelas grandes
TABLE = TABELA
    CAPTION = LEGENDA DA TABELA
    THEAD = CABEÇALHO DA TABELA
        TR, TD, TH
    TBODY = CORPO DA TABELA
        TR, TD, TH
    TFOOT = RODAPÉ DA TABELA
        TR, TD, TH

 ## CSS
 #### Links
- :visited -> link já visitado
- :active -> quando clicado

 #### Background
- background-attachment: scroll -> quando há uma imagem de fundo do site, quando o conteúdo rolar, a imagem acompanha.
- background-attachment: fixed -> mesmo quando o conteúdo rola, a imagem fica fixa.

- transform: aplica qualquer tranformação (inclui rotação) em uma caixa.

 ### Tabelas
- "tr" -> table row.
- "td" -> table data.
- border-collapse: collapse -> tira o espaçamento entre bordas.

**alinhamento vertical**
- vertical align: top // middle // bottom.

#### Mesclagem de células
- colspan="" => expansão de coluna de uma tabela.
- rowspan="" => expansão de linha deuma tabela.

#### Escopos de grupo
- scope: col // colgroup // row // rowgroup => indica o agrupamento de itens em uma tabela .

#### Colgroup, a tag
- criando um "col" para cada uma das minhas COLUNAS, adicionando um class em cada uma delas e a partir disso, terei uma configuração flexivel de colunas que podem ser estilizadas no CSS.
- adicionando "span=""" ao col, podemos fazer uma expansão do número de colunas selecionadas (numeros) sem precisar declara-las uma por uma.

#### Responsividade de tabelas
- overflow-x: auto => conteúdo que transborda

 ### Shorthand
- font: style, weight, size, family.
- background: color, image, position, repeat, size, attachment.
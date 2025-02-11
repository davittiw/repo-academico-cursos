# Aprendizados adquiridos no curso de HTML e CSS do Curso em Vídeo - professor Guanabara (módulo 4)

## HTML

## CSS

### Formulários
- **autocomplete="off"** => desativa o auxiliar 
- **action=""** => ação que será disparada quando o botão submit for clicado
- label **for="#"** => cria uma ligação entre o título do dado a ser inserido e o input
- **required** => obrigatório
- **minlength / maxlength** => máximo e mínimo de resposta permitido
- quando input do tipo **number**, há possibilidade de adicionar "step" que é de quanto em quanto um numero pode aumentar, exemplo: se  step = 0.5, então podemos escrever 5.5 ao invés de pular diretamente para 6 ou simplesmente 5.
- **pattern** => pode ser adicionado e configurado quando input é do tipo tel. exemplo: "/(/d{2}/)[0-9]/d{4,5}-[0-9]/d{4}$"
**/d{} => quantos dígitos serão aceitos
**[0-9] => quais digitos serão aceitos
- **fieldset** => agrupamento de campos (precisa envelopar os itens do formulário)
- **legend** => legenda desse agrupamento
- input do tipo **radio** só pode selecionar uma única opção, por esse motivo, name tem que ser iguais em todas as opções
- input do tipo **range** => cria um "gráfico" de seleção
- **value** => valor pré-definido, introdutório
- input do tipo **file** => deixa que o usuário envie um arquivo/fato (quando utilizado, não pode ser feito pelo método GET, apenas POST)

**estudar sobre regras de expressões regulares de formulários**

#### Métodos POST e GET
- GET: método por padrão, quando os dados não forem sensíveis (até 3 mil bytes, não utulizar para envios de foto)
- POST: dados sensíveis (ideal HTTPS), se dados tiverem mais de 3 mil bytes e se for para enviar arquivos

### Posicionamento
- quando adicionamos no container um position relative e no conteudo um position absolute, podemos configurar top, left, bottom e right e isso ajuda na responsividade do site, pois independente do tamanho da tela, o conteudo sempre vai se manter no meio
- utilizando transform: translate, conseguimos movimentar o bloco para o centro (quando positivo: right e bottom, quando negativo: top e left)
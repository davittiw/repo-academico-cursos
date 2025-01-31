# Terceiro semestre: Tecnologia da Informação.
## Agenda 1: Blocos de linguagem de consulta estruturada.

=> Ao desenvolver módulos que sejam executados diretamente no servidor diminui-se o tráfego de informações na rede, esconde-se boa parte das estruturas das tabelas e agiliza-se o processamento e retorno das mensagens.
=> O MySql suporta variáveis específicas com a sintaxe ´@nomevariavel´. Um nome de variável pode conter letras, números e os caracteres especiais como underline, cifrão e ponto.
A sintaxe básica para configurar uma variável é:

set @variavel= { expressao inteira / espressao real / expressao string } [@variavel= ...].

Também há possibilidade de atribuir um valor a uma variável em outras instruções além de set. No entanto, o operador de atribuição é := (pois = é reservado para comparações em instruções diferentes de set.)
Dependendo da rotina a ser executada, isso pode requer várias consultas e atualizações na base, o que acarreta um maior consumo de recursos pela aplicação.

### Como executar várias ações no banco de dados a partir de uma única instrução?
=> Os procedimentos armazenados (stored procedures) são rotinas definidas no banco de dados, identificadas por um nome pelo qual podem ser chamadas.

**Pontos positivos do uso**
- Simplificação da execução de instruções SQL;
- Transferência de parte da responsabilidade de processamento para o servidor;
- Facilidade na manutenção, reduzindo a quantidade de alterações na aplicação.

**Pontos negativos do uso**
- Necessidade de maior conhecimento da sintaxe do banco de dados para escrita de 
rotinas em SQL;
- As rotinas ficam mais facilmente acessíveis. Alguém que tenha acesso ao banco 
poderá visualizar e alterar o código.

Sintaxe de criação Stored Procedures:
delimiter $$
    create procedure nome_procedimento ([parâmetros])
    begin
    /*corpo do procedimento*/
    end $$
delimiter ;

*nome_procedimento: nome que identificará o procedimento armazenado.
*parâmetros: são opcionais e, caso não sejam necessários, devem permanecer apenas os parênteses vázios na declaração.

Sintaxe na declaração de parâmetros:
(modo nome tipo, modo nome tipo, modo nome tipo)
*nome: nome do parâmetro.
*tipo: o tipo de dado do parâmetro (int, varchar, decimal, etc).
*modo: forma como o parâmetro será tratado no procedimento, se será apenas um dado 
de entrada, apenas de saída ou se terá ambas as funções

**Os valores possível para modo:**
in: indica que o parâmetro é apenas para entrada/recebimento de dados, não podendo ser 
usado para retorno; </br>
out: usado para parâmetros de saída. Para esse tipo não pode ser informado um valor direto 
(como ‘teste’, 1 ou 2.3), deve ser passada uma variável “por referência”; </br>
inout: como é possível imaginar, este tipo de parâmetro pode ser usado para os dois fins 
(entrada e saída de dados). Nesse caso também deve ser informada uma variável e não um valor 
direto.

=> Por padrão o MySQL utiliza o sinal de ponto e vírgula como delimitador de comandos, separando as instruções a serem executadas. No entanto, dentro do corpo do Stored Procedure será necessário separar algumas instruções internamente utilizando esse mesmo sinal, por isso é preciso inicialmente alterar o 
delimitador padrão do MySQL (neste caso, para $$) e ao fim da criação do procedimento, restaurar 
seu valor padrão.

## Agenda 2: Funções
=> Procedures e Funções são até um pouco similares, mas possuem aplicações diferentes. São invocadas de formas diferentes e uma função é usada para gerar um valor que pode ser usado em uma expressão. Esse valor geralmente é baseado em um ou mais parâmetros fornecidos à função.

```php
    delimiter $$
    create function nome_funcao ([parâmetros])
    returns tipo_dados
    begin
        /* corpo da função*/
    return <expressão ou valor ou conteúdo da variável de retorno>;
    end $$
    delimiter;
``
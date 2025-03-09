<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <title>8 Ano A</title>
</head>
<body>
    <div class="w3-third w3-margin w3-responsive w3-container w3-center">
        <h2 class="w3-blue w3-container">8 Ano A</h2>
        <?php
            $alunos = array(
                array('nome'=> 'Alessandro', '1SEM'=> '10', '2SEM'=> '9.5'),
                array('nome'=> 'Rosa', '1SEM'=> '8', '2SEM'=> '5'),
                array('nome'=> 'Andre', '1SEM'=> '5', '2SEM'=> '6.5'),
                array('nome'=> 'Maria', '1SEM'=> '9', '2SEM'=> '9'),
                array('nome'=> 'Túlio', '1SEM'=> '10', '2SEM'=> '10'),
                array('nome'=> 'Cristiane', '1SEM'=> '8', '2SEM'=> '6'),
                array('nome'=> 'Julia', '1SEM'=> '6', '2SEM'=> '8'),
                array('nome'=> 'Jefferson', '1SEM'=> '7', '2SEM'=> '5'),
                array('nome'=> 'João', '1SEM'=> '8', '2SEM'=> '7'),
                array('nome'=> 'Carla', '1SEM'=> '10', '2SEM'=> '6')
            );
            echo '<table class="w3-table-all w3-hoverable w3-text-black">';
            echo '<tr class="w3-blue">';
            echo '<th class="w3-center"> Nome </th>';
            echo '<th class="w3-center"> 1º Semestre </th>';
            echo '<th class="w3-center"> 2º Semestre </th>';
            echo '</tr>';

            foreach($alunos as $aluno) 
            {
                echo '<tr>';
                echo '<td class="w3-center">'.$aluno['nome'].'</td>';
                echo '<td class="w3-center">'.$aluno['1SEM'].'</td>';
                echo '<td class="w3-center">'.$aluno['2SEM'].'</td>';
                echo '</tr>';
            }

            echo '</table>';
        ?>
    </div>
</body>
</html>
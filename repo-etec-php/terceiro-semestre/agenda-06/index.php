<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <title>Projeto - Alunos Concluintes</title>
</head>
<body>
    <div class="w3-padding w3-content w3-text-grey w3-third w3-display-middle">
        <?php
            $host = 'localhost';
            $username = 'root';
            $password = '';
            $database = 'pwii';
            $conexao = new mysqli($host, $username, $password, $database);
            if ($conexao->connect_error) {
                die('Erro na conexão' . $conexao->connect_error);
            }
                echo '
            <div class="w3-padding w3-display-top w3-margin">
                <h1 class="w3-center w3-blue w3-round-large w3-margin">Listagem de Alunos</h1>
                <table class="w3-table-all w3-centered">
                <thead>
                    <tr class="w3-center w3-blue">
                        <th>ID</th>
                        <th>Nome</th>
                        <th>Nota 1</th>
                        <th>Nota 2</th>
                        <th>Nota 3</th>
                        <th>Nota 4</th>
                        <th>Média</th>
                    </tr>
                </thead>
            ';
            $sql = "SELECT * FROM alunoconcluinte ORDER BY idalunoconcluinte";
            $resultado = $conexao->query($sql);
            if($resultado != null)
            foreach($resultado as $linha) {
                echo '<tr>';
                echo '<td>'.$linha['idalunoconcluinte'].'</td>';
                echo '<td>'.$linha['nome'].'</td>';
                echo '<td>'.$linha['nota1'].'</td>';
                echo '<td>'.$linha['nota2'].'</td>';
                echo '<td>'.$linha['nota3'].'</td>';
                echo '<td>'.$linha['nota4'].'</td>';
                echo '<td>'.$linha['media'].'</td>';
                echo '</tr>';
            }
            echo '<table> <br>';
            $sql = "SELECT idalunoconcluinte, nome, media FROM alunoconcluinte WHERE media < 6";
            $result = $conexao->query($sql);
            if($result != null){
                while ($row = $result->fetch_assoc()) {
                    $idaluno = $row['idalunoconcluinte'];
                    $media = $row["media"];
                    $situacao = ($media < 5) ? "Reprovado" : "Aprovado";
                    echo "ID: ".$idaluno." - Situação: ".$situacao;
                }
            }
            $conexao->close();
            ?>
    </div>
</body>
</html>
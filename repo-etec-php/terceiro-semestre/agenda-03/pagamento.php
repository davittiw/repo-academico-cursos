<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <title>Desconto</title>
</head>
<body>
    <div class="w3-container w3-teal">
        <h1>
        <?php
            $pagamento = $_POST['cmbPag'];
            $desconto;
            $valorFinal;
            $valorCompra = $_POST['txtValorCompra'];
            echo "Olá, ".$_POST['txtNome']."! <br> ";
            echo "O Valor da compra: R$".$valorCompra."<br>";
        ?>
        <?php
                if($pagamento == "deposito")
                {
                    echo "Forma de pagamento: ".$pagamento."<br>";
                    echo "Desconto: 10%"."<br>";
                } elseif($pagamento == "boleto")
                {
                    echo "Forma de pagamento: ".$pagamento."<br>";
                    echo "Desconto: 8%"."<br>";
                } else {
                    echo "Forma de pagamento: Cartão de Crédito"."<br>";
                }
            ?>
            <?php
                if($pagamento == "deposito")
                {
                    $desconto = (($valorCompra * 10) / 100);
                    $valorFinal = ($valorCompra - $desconto);
                    echo "Economizou: R$".$desconto."<br>";
                    echo "Valor à pagar: R$".$valorFinal;
                } elseif($pagamento == "boleto")
                {
                    $desconto = (($valorCompra * 8) / 100);
                    $valorFinal = ($valorCompra - $desconto);
                    echo "Economizou: R$".$desconto."<br>";
                    echo "Valor à pagar: R$".$valorFinal;
                } else{
                    echo "Economizou: R$0";
                }
            ?>
        </h1>
    </div>
</body>
</html>
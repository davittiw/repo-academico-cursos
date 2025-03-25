class Main:
    pass

print("Testando o projeto")

# importando cliente de cliente ?
from Client import Client
from Acc import Acc

#construindo um novo objeto da classe cliente (c/ atributos cliente, fone e n)
c1 = Client("João", "13408978459")

#pegando o nome do titular no obj c1 (de cliente) e adicionando diretamente num e saldo
conta = Acc(c1.get_nome(), 1222)

conta.deposito(200)
conta.saque(50)
conta.extrato()

## public: exemplo_
## protected: _exemplo
## private: exemplo__ (modificador mais restrito)
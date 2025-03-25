class Client:
    # init chamado quando criar um objeto
    # self nesse caso exporta as caract do objeto
    def __init__(self, n, fone):
        self._nome = n #modificador: protegido
        self._telefone = fone #modificador: protegiso

    def get_nome(self):
        return self._nome #retornar valor de nome?

    def set_nome(self, nome):
        self._nome = nome

        # get le os valores e retorna
        # set recebe argumentos e atribui a obj internos
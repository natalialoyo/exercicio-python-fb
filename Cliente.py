# class declara a classe
class Cliente:

# def declara o método

# para definir o construtor adicionamos: __init__
# o init() é um método especial que será chamado sempre que criarmos um objeto da classe

# incluímos o parâmetro obrigatório self, que está presente em todos os métodos e exporta as características do objeto
# self representa o objeto em si, portanto, devemos usá-lo sempre que quisermos especificar atributos de objetos
    def __init__(self, n, fone):

# para adicionar atributos a uma classe, basta definir o nome do atributo acompanhado da palavra reservada self, no método especial denominado __init__ do método construtor
        self.nome = n
        self.telefone = fone

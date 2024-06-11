class Main:

# como a classe Main não possui atributos, utilizamos apenas a palavra reservada pass
    pass

print("Testando o projeto")

from Cliente import Cliente

# após criarmos a referência da classe, adicionamos o novo objeto, passando por parâmetro os valores para inicialização dos atributos
# [TESTE] c1 = Cliente("João", "98765-4321")
# [TESTE] print(c1)
# [TESTE] print(c1.nome, "e", c1.telefone)

from Conta import Conta

c1 = Cliente("João", "98765-4321")
conta  = Conta(c1.nome, 6565, 0)

print(f'Nome: {conta.titular}, Número: {conta.numero} e Saldo: {conta.saldo}.')

class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Valor inválido para depósito.')

    def saque(self, valor):
        if self.saldo >= valor and valor <= 500 and len(self.saques) < 3:
            self.saldo -= valor
            self.saques.append(valor)
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        elif self.saldo < valor:
            print('Saldo insuficiente para o saque.')
        elif len(self.saques) >= 3:
            print('Limite máximo de saques diários atingido.')
        else:
            print('Valor inválido para saque.')

    def extrato(self):
        if len(self.depositos) == 0 and len(self.saques) == 0:
            print('Não foram realizadas movimentações.')
        else:
            print('----- Extrato -----')
            for deposito in self.depositos:
                print(f'Depósito: R$ {deposito:.2f}')
            for saque in self.saques:
                print(f'Saque: R$ {saque:.2f}')
            print(f'Saldo atual: R$ {self.saldo:.2f}')


# Exemplo de uso do sistema bancário
sistema = SistemaBancario()
sistema.deposito(1000)
sistema.saque(300)
sistema.saque(200)
sistema.saque(600)
sistema.deposito(500)
sistema.extrato()

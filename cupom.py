import datetime  # Importa o módulo datetime para lidar com datas e horas

class CupomFiscal:
    def __init__(self, itens, numero_pedido, nome_cliente, cartao_credito, numero_mesa, operador, atendente, tempo_permanencia):
        # Inicializa os atributos da instância com os valores fornecidos
        self.itens = itens
        self.numero_pedido = numero_pedido
        self.nome_cliente = nome_cliente
        self.cartao_credito = cartao_credito
        self.numero_mesa = numero_mesa
        self.operador = operador
        self.atendente = atendente
        self.tempo_permanencia = tempo_permanencia
        # Calcula o total do pedido ao inicializar o objeto
        self.total_pedido = self.calcular_total_pedido()

    def calcular_total_pedido(self):
        # Calcula o total do pedido somando os valores de cada item
        total = sum(item['valor'] for item in self.itens)
        return total

    def emitir_cupom(self):
        # Imprime cabeçalho do cupom fiscal
        print("Restaurante do Interior - Cupom Fiscal")
        print("===================================")
        # Imprime informações do pedido
        print(f"Número do Pedido: {self.numero_pedido}")
        print(f"Número da Mesa: {self.numero_mesa}")
        # Obtém a data e hora atual e a imprime formatada
        print(f"Data e Hora: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Nome do Cliente: {self.nome_cliente}")
        print(f"Atendente: {self.atendente}")
        print(f"Operador: {self.operador}")
        print("-------- Itens do Pedido --------")
        # Imprime cada item do pedido com sua quantidade, preço unitário e valor total
        for item in self.itens:
            print(f"{item['nome']:20} x{item['quantidade']:2}  R${item['preco']:6.2f}  R${item['valor']:6.2f}")
        print("---------------------------------")
        # Calcula subtotal, taxa de serviço e total a pagar
        subtotal = self.total_pedido / 1.10  # Subtotal antes da taxa de serviço (10%)
        taxa_servico = self.total_pedido - subtotal
        print(f"Subtotal: R${subtotal: .2f}")
        print(f"Taxa de Serviço (10%): R${taxa_servico: .2f}")
        print(f"Total a Pagar: R${self.total_pedido: .2f}")
        # Imprime informações adicionais como pagamento e tempo de permanência
        print(f"Pagamento com Cartão de Crédito: {self.cartao_credito}")
        print(f"Tempo de Permanência: {self.tempo_permanencia}")
        print("===================================")

# Exemplo de uso:
pedido = [
    {'nome': 'Hamburguer', 'quantidade': 2, 'preco': 15.0, 'valor': 0.0},
    {'nome': 'Batata Frita', 'quantidade': 1, 'preco': 10.0, 'valor': 0.0},
    {'nome': 'Refrigerante', 'quantidade': 3, 'preco': 5.0, 'valor': 0.0}
]

# Calcula o valor de cada item no pedido
for item in pedido:
    item['valor'] = item['quantidade'] * item['preco']

# Define outras informações do pedido
numero_pedido = 12345
nome_cliente = "Karol Wojtyla"
cartao_credito = "**** **** **** 1234"  # Número fictício do cartão
numero_mesa = 5
operador = "João"
atendente = "Maria"
tempo_permanencia = "1 hora e 30 minutos"  # Tempo fictício de permanência

# Cria uma instância de CupomFiscal com os detalhes do pedido e emite o cupom fiscal
cupom = CupomFiscal(pedido, numero_pedido, nome_cliente, cartao_credito, numero_mesa, operador, atendente, tempo_permanencia)
cupom.emitir_cupom()

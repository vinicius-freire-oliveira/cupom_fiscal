import datetime

def calcular_total_pedido(itens):
    total = sum(item['valor'] for item in itens)
    return total

def emitir_cupom_fiscal(itens, total_pedido, numero_pedido, nome_cliente, cartao_credito, numero_mesa, operador, atendente, tempo_permanencia):
    # Imprime cabeçalho do cupom fiscal
    print("Restaurante do Interior - Cupom Fiscal")
    print("===================================")
    # Imprime informações do pedido
    print(f"Número do Pedido: {numero_pedido}")
    print(f"Número da Mesa: {numero_mesa}")
    print(f"Data e Hora: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Nome do Cliente: {nome_cliente}")
    print(f"Atendente: {atendente}")
    print(f"Operador: {operador}")
    print("-------- Itens do Pedido --------")
    # Imprime cada item do pedido com sua quantidade, preço unitário e valor total
    for item in itens:
        print(f"{item['nome']:20} x{item['quantidade']:2}  R${item['preco']:6.2f}  R${item['valor']:6.2f}")
    print("---------------------------------")
    # Calcula subtotal, taxa de serviço e total a pagar
    subtotal = total_pedido / 1.10  # Subtotal antes da taxa de serviço (10%)
    taxa_servico = total_pedido - subtotal
    print(f"Subtotal: R${subtotal: .2f}")
    print(f"Taxa de Serviço (10%): R${taxa_servico: .2f}")
    print(f"Total a Pagar: R${total_pedido: .2f}")
    # Imprime informações adicionais como pagamento e tempo de permanência
    print(f"Pagamento com Cartão de Crédito: {cartao_credito}")
    print(f"Tempo de Permanência: {tempo_permanencia}")
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

# Calcula o total do pedido
total_pedido = calcular_total_pedido(pedido)

# Definição de outras informações do pedido
numero_pedido = 12345
nome_cliente = "Karol Wojtyla"
cartao_credito = "**** **** **** 1234"  # Número fictício do cartão
numero_mesa = 5
operador = "João"
atendente = "Maria"
tempo_permanencia = "1 hora e 30 minutos"  # Tempo fictício de permanência

# Emite o cupom fiscal
emitir_cupom_fiscal(pedido, total_pedido, numero_pedido, nome_cliente, cartao_credito, numero_mesa, operador, atendente, tempo_permanencia)

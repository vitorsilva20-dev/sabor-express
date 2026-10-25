print('bem vindo ao menu\n')

clientes = []
reservas = []
mesas = [
    {'numero': 1, 'lugares': 2, 'ocupada': False},
    {'numero': 2, 'lugares': 2, 'ocupada': False},
    {'numero': 3, 'lugares': 4, 'ocupada': False},
    {'numero': 4, 'lugares': 4, 'ocupada': False},
    {'numero': 5, 'lugares': 6, 'ocupada': False}
]


def menu():
    print('Menu de opcoes: ')
    print('1. Cadastrar cliente')
    print('2. Listar clientes')
    print('3. Cadastrar reserva')
    print('4. Ver mesas disponiveis')
    print('5. Pagamentos de reserva')
    print('6. Lista de reservas')
    print('7. Sair')


def main():
    while True:
        menu()
        opcao = input('Escolha uma opcao: ')

        if opcao == '1':
            print('Cadastrar cliente')
            cliente = {
                'nome': input('Digite seu nome: '),
                'cpf': input('Digite o seu CPF: '),
                'email': input('Digite o seu email: '),
                'cidade': input('Informe a sua cidade: ')
            }
            clientes.append(cliente)
            print('Cliente cadastrado com sucesso!')

        elif opcao == '2':
            print('\nLista de clientes')
            if not clientes:
                print('Nenhum cliente cadastrado.')
            else:
                for cliente in clientes:
                    print(cliente)

        elif opcao == '3':
            print('Cadastrar reserva')
            cpf = input('Digite o CPF do cliente: ').strip()
            cliente = next(
                (cliente for cliente in clientes if cliente['cpf'].strip() == cpf),
                None
            )

            if cliente is None:
                print('Cliente nao encontrado. Cadastre o cliente primeiro.')
                continue

            data = input('Data da reserva: ')
            horario = input('Horario da reserva: ')

            try:
                pessoas = int(input('Quantidade de pessoas: '))
            except ValueError:
                print('Quantidade de pessoas deve ser um numero inteiro.')
                continue

            if pessoas < 1:
                print('A reserva deve ter pelo menos uma pessoa.')
                continue

            mesas_disponiveis = [
                mesa for mesa in mesas
                if not mesa['ocupada'] and mesa['lugares'] >= pessoas
            ]
            if not mesas_disponiveis:
                print('Nao ha mesa disponivel para essa quantidade de pessoas.')
                continue

            mesa = min(mesas_disponiveis, key=lambda item: item['lugares'])
            mesa['ocupada'] = True
            reserva = {
                'cpf': cpf,
                'data': data,
                'horario': horario,
                'pessoas': pessoas,
                'mesa': mesa['numero']
            }
            reservas.append(reserva)
            print(f"Reserva cadastrada com sucesso! Mesa {mesa['numero']}.")

        elif opcao == '4':
            print('\nMesas disponiveis')
            mesas_disponiveis = [mesa for mesa in mesas if not mesa['ocupada']]
            if not mesas_disponiveis:
                print('Nenhuma mesa disponivel.')
            else:
                for mesa in mesas_disponiveis:
                    print(f"Mesa {mesa['numero']} - {mesa['lugares']} lugares")

        elif opcao == '5':
            print('Pagamento da reserva')
            print('Funcionalidade ainda nao implementada.')

        elif opcao == '6':
            print('\nLista de reservas')
            if not reservas:
                print('Nenhuma reserva cadastrada.')
            else:
                for reserva in reservas:
                    print(reserva)

        elif opcao == '7':
            print('Saindo do sistema.')
            break

        else:
            print('Opcao invalida! Tente novamente.')


if __name__ == '__main__':
    main()

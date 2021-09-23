import pandas as pd

class Main:
    def __init__(self):
        pass

    def analise_1(self, a, b):
        c = pd.DataFrame()
        c['A'] = a.Usabilidade
        c['B'] = b.Usabilidade
        print(c)


if __name__ == '__main__':
    newMain = Main()
    print(f"Controle do Processo de Produção dos Sensores")
    print(f"1 - Preparação dos Módulos de Hardware")
    print(f"2 - Programação do Firmware")
    print(f"3 - Preparação da Caixa do Sensor")
    print(f"4 - Fixação do Sensor na Caixa")
    print(f"5 - Fechamento e Acabamento do Sensor na Xaixa")
    print(f"6 - Envio para o Cliente")

    choice = int(input('Sua escolha: '))

    if choice == 1:
        x = pd.read_csv('Tabelas/preparacao_modulos_hardware.csv')
        print(x.head(10))
    elif choice == 2:
        x = pd.read_csv('Tabelas/programação_firmware.csv')
        print(x.head(10))
    elif choice == 3:
        x = pd.read_csv('Tabelas/preparação_caixa.csv')
        print(x.head(10))
    elif choice == 4:
        x = pd.read_csv('Tabelas/fixação_sensor.csv')
        print(x.head(10))
    elif choice == 5:
        x = pd.read_csv('Tabelas/fechamento_acabamento_sensor.csv')
        print(x.head(10))
    elif choice == 6:
        x = pd.read_csv('Tabelas/envio_cliente.csv')
        print(x.head(10))

    a = pd.read_csv('Tabelas/preparacao_modulos_hardware.csv')
    b = x = pd.read_csv('Tabelas/envio_cliente.csv')

    newMain.analise_1(a, b)
    
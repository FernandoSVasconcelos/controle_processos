import pandas as pd
from random import randint

class preencheTabelas:
    def __init__(self, nome) -> None:
        self._preenchimento = []
        self._dict_preenchimento = {}
        self._nome = nome

        for i in range(100):
            self._preenchimento.append(f'{i}')

        self._dict_preenchimento['Código_Sensor'] = self._preenchimento
        self._planilha = pd.DataFrame.from_dict(self._dict_preenchimento, orient = 'index').T

    @property
    def planilha(self):
        return self._planilha

    @planilha.setter
    def planilha(self, planilha):
        self._planilha = planilha

    def numero_chip(self):
        for i in range(100):
            x = randint(10000, 99999)
            self._preenchimento[i] = x
        self._planilha['Número_Chip'] = self._preenchimento

    def código_modulo(self):
        for i in range(100):
            x = randint(100000, 999999)
            self._preenchimento[i] = x
        self._planilha['Código_Módulo'] = self._preenchimento

    def controle_qualidade(self):
        for i in range(100):
            x = randint(0, 2)
            if x == 0:
                self._preenchimento[i] = 'Ruim'
            elif x == 1:
                self._preenchimento[i] = 'Regular'
            elif x == 2:
                self._preenchimento[i] = 'Bom'

        self._planilha['Controle_Qualidade'] = self._preenchimento

    def status_sensor(self):
        for i in range(100):
            x = randint(0, 1)
            if x == 0:
                self._preenchimento[i] = 'Não Funcional'
            elif x == 1:
                self._preenchimento[i] = 'Funcional'

        self._planilha['Status_Sensor'] = self._preenchimento

    def mudança_status(self):
        for i in range(100):
            x = randint(0, 1)
            if x == 0:
                self._preenchimento[i] = 'Não Funcional'
            elif x == 1:
                self._preenchimento[i] = 'Funcional'

        self._planilha['Mudança_Status'] = self._preenchimento

    def solução_incremental(self):
        for i in range(100):
            x = randint(0, 1)
            if x == 0:
                self._preenchimento[i] = 'Não'
            elif x == 1:
                self._preenchimento[i] = 'Sim'

        self._planilha['Solução_Incremental'] = self._preenchimento

    def usabilidade_solução(self):
        for i in range(100):
            x = randint(0, 1)
            if x == 0:
                self._preenchimento[i] = 'Não usável'
            elif x == 1:
                self._preenchimento[i] = 'Usável'

        self._planilha['Usabilidade'] = self._preenchimento

    def __str__(self):
        return f"{self._planilha}"

if __name__ == '__main__':
    new_preencheTabelas = preencheTabelas('preparacao_modulos_hardware.csv')
    new_preencheTabelas.numero_chip()
    new_preencheTabelas.código_modulo()
    new_preencheTabelas.controle_qualidade()
    new_preencheTabelas.status_sensor()
    new_preencheTabelas.mudança_status()
    new_preencheTabelas.solução_incremental()
    new_preencheTabelas.usabilidade_solução()
    new_preencheTabelas.planilha.to_csv('Tabelas/preparacao_modulos_hardware.csv', index = False)

    new_preencheTabelas = preencheTabelas('programação_firmware.csv')
    new_preencheTabelas.numero_chip()
    new_preencheTabelas.código_modulo()
    new_preencheTabelas.controle_qualidade()
    new_preencheTabelas.status_sensor()
    new_preencheTabelas.mudança_status()
    new_preencheTabelas.solução_incremental()
    new_preencheTabelas.usabilidade_solução()
    new_preencheTabelas.planilha.to_csv('Tabelas/programação_firmware.csv', index = False)

    new_preencheTabelas = preencheTabelas('preparação_caixa.csv')
    new_preencheTabelas.numero_chip()
    new_preencheTabelas.código_modulo()
    new_preencheTabelas.controle_qualidade()
    new_preencheTabelas.status_sensor()
    new_preencheTabelas.mudança_status()
    new_preencheTabelas.solução_incremental()
    new_preencheTabelas.usabilidade_solução()
    new_preencheTabelas.planilha.to_csv('Tabelas/preparação_caixa.csv', index = False)

    new_preencheTabelas = preencheTabelas('fixação_sensor.csv')
    new_preencheTabelas.numero_chip()
    new_preencheTabelas.código_modulo()
    new_preencheTabelas.controle_qualidade()
    new_preencheTabelas.status_sensor()
    new_preencheTabelas.mudança_status()
    new_preencheTabelas.solução_incremental()
    new_preencheTabelas.usabilidade_solução()
    new_preencheTabelas.planilha.to_csv('Tabelas/fixação_sensor.csv', index = False)

    new_preencheTabelas = preencheTabelas('fechamento_acabamento_sensor.csv')
    new_preencheTabelas.numero_chip()
    new_preencheTabelas.código_modulo()
    new_preencheTabelas.controle_qualidade()
    new_preencheTabelas.status_sensor()
    new_preencheTabelas.mudança_status()
    new_preencheTabelas.solução_incremental()
    new_preencheTabelas.usabilidade_solução()
    new_preencheTabelas.planilha.to_csv('Tabelas/fechamento_acabamento_sensor.csv', index = False)

    new_preencheTabelas = preencheTabelas('envio_cliente.csv')
    new_preencheTabelas.numero_chip()
    new_preencheTabelas.código_modulo()
    new_preencheTabelas.controle_qualidade()
    new_preencheTabelas.status_sensor()
    new_preencheTabelas.mudança_status()
    new_preencheTabelas.solução_incremental()
    new_preencheTabelas.usabilidade_solução()
    new_preencheTabelas.planilha.to_csv('Tabelas/envio_cliente.csv', index = False)
import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 0
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        #Layout
        desenho = [
            [sg.Text('Seu Chute', size=(20,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Chutar')],
            [sg.Output(size=(30,10))]
        ]
        #Janela
        self.janela = sg.Window('Chute o Número',layout=desenho)
        self.GerarNumeroAleatorio()
        try:
            while True:
                #recebe valor
                self.evento, self.valores = self.janela.Read()
                    #fazer algo com os valores
                if self.evento == 'Chutar':                     
                    self.valor_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo '+ self.valor_chute)
                            break
                        elif int(self.valor_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto '+ self.valor_chute)
                            break
                        if int(self.valor_chute) == self.valor_aleatorio:
                            print('Parabéns você acertou '+ self.valor_chute)
                            self.tentar_novamente = False
                            break
                            
        except:
                print('Por favor somente números')        
                self.Iniciar()
                        
    def GerarNumeroAleatorio(self):
           self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()
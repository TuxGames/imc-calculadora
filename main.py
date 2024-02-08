from PySimpleGUI import PySimpleGUI as sg

imc = 0
pesonivel = 'indefinido'

sg.theme('Reddit')

layout = [
    [sg.Text('Sua altura em metros:'), sg.Input(key='altura')],
    [sg.Text('Seu peso em Kg:'), sg.Input(key='peso')],
    [sg.Text('*Coloque . caso seja um valor não inteiro, como a altura.')],
    [sg.Text('*Resultados imprecisos')],
    [sg.Button('Calcular')]
]

app = sg.Window('Calculadora IMC V1', layout)

while True:
    events, valores = app.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == 'Calcular':
        try:
            imc = float(valores['peso']) / (float(valores['altura']) * float(valores['altura']))
            if imc < 18.5:
                pesonivel='abaixo do peso'
            elif imc >= 18.5 and imc < 25:
                pesonivel='saudável'
            elif imc >= 25:
                pesonivel='sobrepeso'
            sg.popup_ok(f'IMC = {imc}, você está {pesonivel}')
        except ValueError:
            sg.popup_error('Algo deu errado... Verifique suas respostas e tente novamente.')
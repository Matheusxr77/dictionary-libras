# Importando a classe Flask e a função render_template do módulo flask
from flask import Flask, render_template
import json

# Importando a classe Sinal do módulo models.sinal
from models.Sinal import Sinal

# Criando a aplicação Flask
webApp = Flask(__name__)

# Definindo a chave secreta para a sessão da aplicação
webApp.secret_key = 'UFAPE'

# Função para carregar sinais do arquivo JSON
def carregar_sinais():
    with open('./data/sinais.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        return [Sinal(**sinal) for sinal in dados]
    
# Carregando a lista de sinais
listaSinais = carregar_sinais()

# Rota para a página inicial
@webApp.route('/')
def inicio():
    return render_template('index.html', titulo='Lista de Disciplinas', listaSinais=listaSinais)

# Iniciando a aplicação Flask em modo de depuração
if __name__ == '__main__':
    webApp.run(debug=True)
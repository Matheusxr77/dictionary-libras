# Importando a classe Flask e a função render_template do módulo flask
from flask import Flask, render_template
import json

# Importando a classe Sinal do módulo models.sinal
from models.Sinal import Sinal

# Criando a aplicação Flask
webApp = Flask(__name__)

# Definindo a chave secreta para a sessão da aplicação
webApp.secret_key = 'UFAPE'

# Iniciando a aplicação Flask em modo de depuração
if __name__ == '__main__':
    webApp.run(debug=True)
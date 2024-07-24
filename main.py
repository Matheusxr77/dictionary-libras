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
    with open('./static/data/sinais.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        return [Sinal(**sinal) for sinal in dados]
    
# Carregando a lista de sinais
listaSinais = carregar_sinais()

# Rota para a página inicial
@webApp.route('/')
def inicio():
    return render_template('index.html', titulo='Lista de Disciplinas', listaSinais=listaSinais)

# Rota para a página de Introdução à Programação
@webApp.route('/introducao-a-programacao')
def introducaoProgramacao():
    sinais_ip = [sinal for sinal in listaSinais if sinal.disciplina == "Introdução à Programação"]
    return render_template('ip.html', titulo="Disciplina de Introdução à Programação", listaSinais=sinais_ip)

# Rota para a página de Introdução à Computação
@webApp.route('/introducao-a-computacao')
def introducaoComputacao():
    sinais_ic = [sinal for sinal in listaSinais if sinal.disciplina == "Introdução à Computação"]
    return render_template('ic.html', titulo="Disciplina de Introdução à Computação", listaSinais=sinais_ic)

# Rota para a página de Programação Orientada a Objetos
@webApp.route('/programacao-orientada-a-objetos')
def programacaoOrientada():
    sinais_poo = [sinal for sinal in listaSinais if sinal.disciplina == "Programação Orientada a Objetos"]
    return render_template('poo.html', titulo="Disciplina de Programação Orientada a Objetos", listaSinais=sinais_poo)

# Iniciando a aplicação Flask em modo de depuração
if __name__ == '__main__':
    webApp.run(debug=True)
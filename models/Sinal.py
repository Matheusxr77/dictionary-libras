# Definindo a classe sinal
class Sinal:
    # Função que inicializa os atributos da função
    def __init__(self, nome, descricao, video, disciplina) -> None:
        # Inicialização dos atributos do sinal
        self.nome = nome
        self.descricao = descricao
        self.video = video
        self.disciplina = disciplina
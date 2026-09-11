from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

print(__name__)

@app.route('/')
def pagina_inicial():
    return '<h1>Olá, Mundo</h1>'

@app.route('/sobre')
def sobre():
    return '''
        <h1 style='color:red'> Meu nome é: </h1>
        <p> Juliamel Maria <b> Domingos <p>
        <!--  Tudo  que eu pensar em html pode ir aqui -->
        '''

@app.route('/curso')
def curso():
    return '''
        <h1 style='color:purple'> Meu curso é: </h1>
        <p> Gestão da Tecnolgia da Informação na <b> Fatec Jahu <p>
        '''

@app.route('/var')
def variavel():
    palavra = 'Juliamel'
    return f'<h1> Adicionado texto de var: {palavra} </h1>'
        # 'f' uso para troca do [palavra]

@app.route ('/idade/<int:ano>') # 'int' usado para número (se nao usar da erro) '<>' sig que é variavel
def idade(ano):
    calculoidade = 2026 - ano
    return f'você tem {calculoidade} anos!'

@app.route ('/salvar/<nome>/produtos')
def salvar(nome):
    return f'Você salvou produto [ {nome} ] com sucesso!'

@app.route('/html')
def pagina_html():
    return render_template('index.html')

@app.route('/lugar')
def lugar():
    return f'Bem-Vindo a FATEC'

@app.route('/calcular/<nome>/<int:ano>')
def calcular(nome, ano):
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade > 18: 
        status = 'Maior de Idade'

# coloque o codigo "= 18 tem que aparecer"(fazer cai na prova!!!)

    else:
        status = 'Menor de Idade - ACESSO NEGADO!'

    return render_template('variaveis.html', nome_usuario = nome,
                           ano_atual = ano_atual, nascimento = ano,
                           idade = idade, status = status)
                           # esquerda html = direita app.py(python)

@app.route('/dicio')
def dicionario():
    dados = {
        'chave' : 'valor',
        'curso' : 'GTI',
        'local' : 'Fatec Jahu',
        'semestre' : 4,
    }
    return render_template('dicio.html', **dados)

@app.route('/condicao/<int:numero>')
def condicao(numero):
    return render_template('condicao.html', numero = numero)

@app.route('/perfil/<nome>')
def perfil(nome):
    # Simulando um banco de dados com um dicionário de usuários
    # Na Aula 05 isso virá do MySQL de verdade
    usuarios = {
        'admin': {
            'nome': 'Administrador',
            'email': 'admin@fatec.br',
            'nivel': 'administrador',
            'ativo': True,
            'posts': 47
        },
        'joao': {
            'nome': 'João Silva',
            'email': 'joao@email.com',
            'nivel': 'usuario',
            'ativo': True,
            'posts': 12
        },
        'maria': {
            'nome': 'Maria Souza',
            'email': 'maria@email.com',
            'nivel': 'moderador',
            'ativo': False,
            'posts': 31
        }
    }

    # Busca o usuário pelo nome na URL — .get() retorna None se não existir
    usuario = usuarios.get(nome)

    # Passa o usuário (ou None) para o template
    return render_template('perfil.html', usuario=usuario, nome_buscado=nome)

# Ultima coisa do codigo
if __name__ == '__main__' :
    app.run(debug=True)
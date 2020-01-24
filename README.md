# Exercício do Curso Flask Intro

Descrição:
----------

Aqui na Space Devs estamos precisando salvar a lista dos usuários que assiste nossos cursos.

Porém não queremos salvar esses dados no bloco de notas do Windows 10. Estamo precisando de uma aplicação para salvar esses contatos.

## Requerido:

- Queremos salvar Nome, Telefone e e-mail dos usuários.

## Formas de fazer:

Cria apenas um arquivo app.py e modela esse arquivo para servir apenas uma rota, faz a conexão com o banco de dados, pode ser via SQLITE para ser mais rápido.

Os dados podem ser salvos através do FLASK SHELL como mostrado na aula, mas caso isso aconteça o aluno deverá enviar para o github o arquivo **.db**

** Atenção: Você pode usar esse repositório como base para construir sua aplicação.

Dúvidas poderam ser retiradas aqui:
[Comunidade](https://t.me/spacedevs)


# Como rodar o Projeto

```
git clone https://github.com/Hp2501/Desafio_SpaceDevs.git
cd Desafio_SpaceDevs
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask db upgrade
export FLASK_ENV=development
flask run
```
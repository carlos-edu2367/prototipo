from private.credenciais import conectar_banco
from organizacional import criar_tabelas_organizacional
from rh import criar_tabelas_rh

# Criando as tabelas dos models
def criar_tabelas():
    criar_tabelas_rh()
    criar_tabelas_organizacional()
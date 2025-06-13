from private.credenciais import conectar_banco
from organizacional import criar_tabelas_organizacional
from rh import criar_tabelas_rh
from financeiro import criar_tabelas_financeiro
from models.administração_neectify import criar_tabelas_adm

# Criando as tabelas dos models
def criar_tabelas():
    criar_tabelas_rh()
    criar_tabelas_organizacional()
    criar_tabelas_adm()
    criar_tabelas_financeiro()


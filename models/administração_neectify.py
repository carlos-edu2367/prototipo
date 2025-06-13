from private.credenciais import conectar_banco
from utils.data_e_hora import data_atual

def criar_tabelas_adm():
    conn = conectar_banco()
    cursor = conn.cursor()

    # Tabela que só será administrada pela equipe responsável pelo sistema (Neectify)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empresas(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            nome_empresa TEXT NOT NULL,
            cnpj_cpf TEXT NOT NULL,
            plano_contratado INTEGER NOT NULL DEFAULT 0,
            contrato_plano DATE NOT NULL,
            expiração_plano DATE NOT NULL,
            qtd_usuarios INTEGER NOT NULL DEFAULT 1
        )
    """)

    # Tabela que moldará os planos (crud somente na neectify)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS planos_base(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            nome_plano TEXT NOT NULL,
            descrição TEXT NOT NULL,
            preço DECIMAL NOT NULL,
            creditos INTEGER NOT NULL,
            detalhes_internos TEXT
        )
    """)
    
    # Tabela de cadastro das funcionalidades (crud neectify)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS funcionalidades(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            titulo_funcionalidade TEXT NOT NULL,
            descrição TEXT NOT NULL,
            creditos_usados TEXT NOT NULL
        )
    """)


    conn.commit()
    conn.close()
    cursor.close()


def verificar_plano_ativo(empresa_id:int):
    """
        Função que verifica se o plano da empresa referente ao colaborador ainda está ativo, se retornar verdadeiro está.


        ARGS: int empresa_id

        RETURNS: Boolean 

    """
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT expiração_plano FROM empresas WHERE id = ?
    """, (empresa_id,))

    dados = cursor.fetchone()
    data_exp = dados

    data_atual = data_atual()
    if data_atual >= data_exp:
        return True
    elif data_atual < data_exp:
        return False
    else:
        print(f"ERRO ao realizar verificação de plano. {data_atual}")
        return False


def verificar_plano_contratado(empresa_id:int):
    """
        Função que retorna o id do plano contratado com base no id da empresa.

        ARGS: int empresa_id

        RETURNS: int id_plano

                   Erros
                ERRO ao realizar verificação de plano: cursor.fetchone não conseguiu pegar o plano desta empresa
    """

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT plano_contratado FROM empresas WHERE id = ?
    """, (empresa_id, ))
    plano = cursor.fetchone()

    if plano:
        return plano
    else:
        print("ERRO ao realizar verificação de plano")
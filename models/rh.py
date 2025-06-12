from private.credenciais import conectar_banco

def criar_tabelas_rh():
    conn = conectar_banco()
    cursor = conn.cursor()

    #                           INICIANDO TABELAS RH/ADMINISTRAÇÃO


# Tabela que só será administrada pela equipe responsável pelo sistema (Neectify)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empresas(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            nome_empresa TEXT NOT NULL,
            cnpj_cpf UNIQUE TEXT NOT NULL,
            plano_contratado INTEGER NOT NULL DEFAULT 0,
            contrato_plano DATE NOT NULL,
            expiração_plano DATE NOT NULL,
            qtd_usuarios INTEGER NOT NULL DEFAULT 1
        )
    """)


# Tabela com informações do usuário (Relacionar com as outras tabelas no CRUD)
# (Estudar a necessidade de mais informações ou de não obrigatoriedade de algumas)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            empresa_id INTEGER NOT NULL,
            nome TEXT NOT NULL,
            sobrenome TEXT NOT NULL,
            endereco TEXT NOT NULL,
            cep TEXT NOT NULL,
            tel1 TEXT NOT NULL,
            tel2 TEXT,
            email TEXT,
            empresa_nome TEXT NOT NULL,
            cpf UNIQUE TEXT NOT NULL,
            senha TEXT NOT NULL,
            data_nascimento DATE NOT NULL,
            cargo INTEGER NOT NULL DEFAULT 0,
            salário DECIMAL NOT NULL,
            carga_horária INTEGER NOT NULL,
            tipo_contrato TEXT NOT NULL,
            data_contratado DATE NOT NULL,
            data_ultima_ferias DATE NOT NULL,
            extras TEXT
        )
    """)


# Cadastro de cargos (elaborar mais, incompleto)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cargos(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            nome TEXT NOT NULL,
            nivel_de_acesso TEXT NOT NULL DEFAULT 'comum'
        )
    """)


# Tabela separada para facilitar crud de cargas horárias, cadastro separado para facilitar casos e casos de forma 
# # padronizada
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS carga_horaria(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            escala TEXT NOT NULL,
            horario_entrada TIME NOT NULL,
            horario_saida TIME NOT NULL,
            horas_semanais INTEGER NOT NULL,
            horas_mensais INTEGER NOT NULL,
            horas_intervalo DECIMAL NOT NULL
        )
    """)


# Adicionando tabela responsável pelo controle de ponto (Atenção a lógica de tipo ENTRADA e SAÍDA do colaborador
# caso necessário solicitar manualmente pelo próprio)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ponto(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            data DATE NOT NULL,
            hora TIME NOT NULL,
            tipo TEXT NOT NULL,
            id_colaborador INTEGER NOT NULL
        )
    """)



# Tabela contendo informações sobre os benefícios de forma escalável (CRUD facilitado)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS beneficios(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            titulo TEXT NOT NULL,
            valor_pago DECIMAL NOT NULL,
            valor_colaborador DECIMAL NOT NULL DEFAULT 0,
            extra TEXT
        )
    """)

# Tabela responsável por relacionar cada colaborador com os benefícios escolhidos pelo próprio
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS relacao_beneficios(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            id_beneficio INTEGER NOT NULL,
            id_colaborador INTEGER NOT NULL
            
        )
    """)


    conn.commit()
    conn.close()
    cursor.close()
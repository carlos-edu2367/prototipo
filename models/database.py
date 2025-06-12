from private.credenciais import conectar_banco


def criar_tabelas():
    conn = conectar_banco()
    cursor = conn.cursor()

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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            empresa_id INTEGER NOT NULL,
            nome TEXT NOT NULL,
            sobrenome TEXT NOT NULL,
            empresa_nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cargos(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            nome TEXT NOT NULL
        )
    """)

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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ponto(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            data DATE NOT NULL,
            hora TIME NOT NULL,
            id_colaborador INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS relacao_ponto(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            id_ponto INTEGER NOT NULL,
            id_colaborador INTEGER NOT NULL,
            tipo TEXT NOT NULL
        )
    """)


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS beneficios(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            titulo TEXT NOT NULL,
            valor_pago DECIMAL NOT NULL,
            valor_colaborador DECIMAL NOT NULL DEFAULT 0,
            extra TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS relacao_beneficios(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            id_beneficio INTEGER NOT NULL,
            id_colaborador INTEGER NOT NULL
            
        )
    """)

#Entrando na area organizacional

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cards(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            id_categoria INTEGER NOT NULL,
            titulo TEXT NOT NULL,
            descricao TEXT,
            data_criada DATE NOT NULL,
            hora_criada TIME NOT NULL,
            data_prazo DATE,
            hora_prazo TIME
        )
    """)
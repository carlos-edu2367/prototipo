from private.credenciais import conectar_banco


def criar_tabelas():
    conn = conectar_banco()
    cursor = conn.cursor()

    #                           INICIANDO TABELAS RH/ADMINISTRAÇÃO


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


# Cadastro de cargos (elaborar mais, incompleto)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cargos(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            nome TEXT NOT NULL
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

                                                #Entrando na area organizacional#

# Criando a base dos cartões (tipo os cartões do trello, uma organização baseada no modelo kanban)
# Atualizações em massa relacionadas a cartões específicos vão ter sua própria tabela para melhor organização e desempenho
# Lembrar de adicionar a data e hora atual nas funções de criar cartão (datetime.now())
# Estudar a possibilidade de mais informações (manter as obrigatórias como estão)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cards(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            id_categoria INTEGER NOT NULL,
            id_lista INTEGER NOT NULL,
            titulo TEXT NOT NULL,
            descricao TEXT,
            id_criador INTEGER NOT NULL,
            data_criada DATE NOT NULL,
            hora_criada TIME NOT NULL,
            data_prazo DATE,
            hora_prazo TIME
        )
    """)

# Criando a tabela de checklists, (Relacionada com cada cartão)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS checklists(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            titulo TEXT NOT NULL,
            realizada? BOOLEAN NOT NULL DEFAULT FALSE
        )
    """)

# Criando a tabela de anexos onde serão salvos as informações do anexo feito via google cloud storage
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS anexos(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            card_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            titulo TEXT NOT NULL,
            url TEXT NOT NULL,
            tipo_arquivo TEXT NOT NULL,
            tamanho_arquivo BIGINT,
            data_upload DATE NOT NULL,
            hora_upload TIME NOT NULL
            
        )
    """)
    


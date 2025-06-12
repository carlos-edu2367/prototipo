from private.credenciais import conectar_banco

def criar_tabelas_organizacional():
    conn = conectar_banco()
    cursor = conn.cursor()

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
    

# Criando a tabela de comentários onde serão feitos os comentários relacionados a cada cartão
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comentarios(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            usuario_id INTEGER NOT NULL,
            texto TEXT NOT NULL,
            anexo_id INTEGER,
            data_post DATE NOT NULL,
            hora_post TIME NOT NULL
        )
    """)

# Criando as listas que agruparão os cartões (normalmente usadas para dividir etapas, inicio, meio e fim)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS listas(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            id_categoria INTEGER NOT NULL,
            lista_nome TEXT NOT NULL,
            lista_cor TEXT NOT NULL DEFAULT 'CINZA'
        )
    """)

# Criando categorias para dividir o estilo de trabalho, cada categoria pode ter um fluxo completamente diferente
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            nome TEXT NOT NULL,
            cor_categoria TEXT NOT NULL DEFAULT 'CINZA',
            nivel_de_acesso TEXT NOT NULL DEFAULT 'comum'
        )
    """)


    
    conn.commit()
    conn.close()
    cursor.close()
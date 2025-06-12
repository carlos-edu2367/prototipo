from private.credenciais import conectar_banco

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
    


    conn.commit()
    conn.close()
    cursor.close()
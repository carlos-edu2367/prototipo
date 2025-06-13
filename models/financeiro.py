from private.credenciais import conectar_banco

def criar_tabelas_financeiro():
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contratos(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            titulo_contrato TEXT NOT NULL,
            orcamento_id INTEGER,
            link_ref_anexo TEXT NOT NULL,
            valor_contrato DECIMAL NOT NULL
            )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orçamentos(
                id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                titulo_orçamento TEXT NOT NULL,
                link_ref_orçamento TEXT NOT NULL,
                valor_orçamento DECIMAL NOT NULL
            )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contas_a_pagar(
                id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                empresa_id INTEGER NOT NULL,
                responsavel_id INTEGER NOT NULL,
                titulo_conta TEXT NOT NULL,
                descrição TEXT NOT NULL,
                fornecedor TEXT NOT NULL,
                valor DECIMAL NOT NULL,
                data_vencimento DATE NOT NULL,
                data_pagamento DATE,
                comprovante_ref TEXT,
                nota_fiscal_ref TEXT
            )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contas_a_receber(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            empresa_id INTEGER NOT NULL,
            responsavel_id INTEGER NOT NULL,
            titulo_conta TEXT NOT NULL,
            descrição TEXT NOT NULL,
            valor DECIMAL NOT NULL,
            data_vencimento DATE NOT NULL,
            data_pagamento DATE,
            comprovante_ref TEXT,
            nota_fiscal_ref TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contas_recorrentes(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            empresa_id INTEGER NOT NULL,
            titulo TEXT NOT NULL,
            descrição TEXT NOT NULL,
            dia_vencimento TEXT NOT NULL,
            valor DECIMAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS relação_contas_recorrentes(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            id_conta INTEGER NOT NULL,
            empresa_id INTEGER NOT NULL,
            titulo TEXT NOT NULL,
            descrição TEXT NOT NULL,
            valor DECIMAL NOT NULL,
            data_vencimento DATE NOT NULL,
            data_pagamento DATE,
            comprovante_ref TEXT,
            nota_fiscal_ref TEXT
        )
    """)

    
    conn.commit()
    conn.close()
    cursor.close()
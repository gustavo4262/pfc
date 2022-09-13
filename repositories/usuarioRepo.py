from conexao import criaConexao

def criaUsuarioRepo(nome, senha, isMedico):
    conn, cur = criaConexao()

    if isMedico:
        query = f"""
                insert into "Medico" ("Nome", "Senha")
                values ('{nome}', '{senha}')
                """
    else:
        query = f"""
                insert into "Paciente" ("Nome", "Senha")
                values ('{nome}', '{senha}')
                """
    cur.execute(query)
    conn.commit()

    cur.close()
    conn.close()


def adicionaPacienteAMedicoRepo(paciente, medico):
    conn, cur = criaConexao()

    query1 = f"""
            select "ID" from "Medico" 
            where "Nome" = '{medico}'
            """
    query2 = f"""
            select "ID" from "Paciente" 
            where "Nome" = '{paciente}'
            """

    cur.execute(query2)
    pacienteRes = cur.fetchone()
    if pacienteRes is None:
        raise Exception("Not Found")
    pacienteID = pacienteRes[0]
    
    cur.execute(query1)
    medicoRes = cur.fetchone()
    if medicoRes is None:
        raise Exception("Not Found")
    medicoID = medicoRes[0]

    query3 = f"""
            insert into "PacienteMedico" ("PacienteID", "MedicoID")
            values ({pacienteID}, {medicoID})
            """
    
    print(query3)
    cur.execute(query3)
    conn.commit()

    cur.close()
    conn.close()
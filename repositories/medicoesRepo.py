from conexao import criaConexao


def postaMedicaoRepo(paciente, tipoDados, valor, horario):
    conn, cur = criaConexao()

    query1 = f"""
            select * from "TipoDados"
            where "TipoDados" = '{tipoDados}'
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
    tipoDadosRes = cur.fetchone()
    if tipoDadosRes is None:
        raise Exception("Not Found")
    tipoDadosID = tipoDadosRes[0]


    query3 = f"""
            insert into "Medicoes" ("TipoDadosID", "PacienteID", "DataTime", "Valor")
            values ({tipoDadosID}, {pacienteID}, '{horario}', {valor})
            """
    
    cur.execute(query3)
    conn.commit()

    cur.close()
    conn.close()


def pegaMedicaoRepo(paciente, tipoDados):
    conn, cur = criaConexao()

    query1 = f"""
            select * from "TipoDados"
            where "TipoDados" = '{tipoDados}'
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
    tipoDadosRes = cur.fetchone()
    if tipoDadosRes is None:        
        raise Exception("Not Found")
    tipoDadosID = tipoDadosRes[0]


    query3 = f"""
            select * from "Medicoes"
            where "PacienteID" = {pacienteID}
            and "TipoDadosID" = {tipoDadosID}
            """
    
    cur.execute(query3)
    res = cur.fetchall()

    cur.close()
    conn.close()

    return res


def pegaListaPacientesMedicoRepo(medico):
    conn, cur = criaConexao()
    
    query = f"""
                select pac."Nome" from  "PacienteMedico"
                inner join  "Paciente" as pac
                on "PacienteMedico"."PacienteID" = pac."ID"
                inner join "Medico" as med
                on med."ID" = "PacienteMedico"."MedicoID"
                where med."Nome" = '{medico}'
            """
    cur.execute(query)
    res = cur.fetchall()
    if res is None:
        raise Exception("Not Found")

    cur.close()
    conn.close()

    return res
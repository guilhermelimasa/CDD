import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user='root',
    password='cdd2023',
    database='ESCOLATURMAC'
)
print(banco)

meucursor = banco.cursor()
#pesquisa = 'select * from funcionarios;'
#meucursor.execute(pesquisa)
#resultado = meucursor.fetchall()
#for x in resultado:
#    print(x)


nome1 = "Alberto lima"
telefone1 = "81951535984"
turma1 = "C"
media1 = 8.95
sql = "insert into alunos (NOME, TELEFONE, TURMA, MEDIA) values (%s,%s,%s,%s)"
data = (nome1, telefone1, turma1, media1)
meucursor.execute(sql, data)
banco.commit()
userid = meucursor.lastrowid
print(userid)
meucursor.close()
banco.close()

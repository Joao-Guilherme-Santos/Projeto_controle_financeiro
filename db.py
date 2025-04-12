import sqlite3

conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS gastos(nome ,valor)
''')

conexao.commit()

def addBill(bill,value):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()
    cursor.execute(f"INSERT INTO gastos VALUES('{bill}', {value})")
    conexao.commit()

addBill('agua', 1950)

cursor.execute("SELECT * FROM gastos")
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)

cursor.execute("SELECT nome, valor FROM gastos")
resultado = cursor.fetchone()
print(resultado[1])
print(resultado)
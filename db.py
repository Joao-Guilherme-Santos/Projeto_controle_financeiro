import sqlite3

conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()

def creatTab(tabName,values):
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {tabName}(id integer primary key auto increment,{values})
    ''')
    
    conexao.commit()


def addBill(tab,bill,value):
    cursor.execute(f"INSERT INTO {tab} VALUES('{bill}', {value})")
    conexao.commit()


def selectFromTab(tabName):
    cursor.execute(f"SELECT * FROM {tabName}")
    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)


def findFromTab(tabName, values):
    cursor.execute(f"SELECT {values} FROM {tabName}")
    resultado = cursor.fetchone()
    print(resultado)

print("executei")
if __name__ == "__main__":
    creatTab("gastos",("conta,valor"))
    addBill("gastos","agua",150)
    selectFromTab("gastos")
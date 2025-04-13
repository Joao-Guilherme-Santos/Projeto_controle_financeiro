import db

db.creatTab("gastos",("conta,valor"))
db.addBill("gastos","agua",150.675)
db.selectFromTab("gastos")
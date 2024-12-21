import pymongo

def conectar_mongo():
    try:
        cliente = pymongo.MongoClient('mongodb://localhost:27017/')
        db = cliente['estoque_db']
        print('Conectado ao MongoDB')
        return db
    except Exception as e:
        print(f'Erro ao conectar ao MongoDB: {e}')
        return None
    
print(conectar_mongo())
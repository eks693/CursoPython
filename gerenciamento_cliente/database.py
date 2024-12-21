import pymongo

def conectar_mongo():
    """
    Função para conectar ao MongoDB e retornar a referência ao banco de dados 'clientes_db'.
    """
    try:
        cliente = pymongo.MongoClient('mongodb://localhost:27017/')
        db = cliente['clientes_db']  # Nome do banco de dados para cadastro de clientes
        print('Conectado ao MongoDB')
        return db
    except Exception as e:
        print(f'Erro ao conectar ao MongoDB: {e}')
        return None

# Testando a conexão ao MongoDB
if __name__ == '__main__':
    db = conectar_mongo()
    if db:
        print('Conexão estabelecida com sucesso.')
    else:
        print('Falha na conexão.')

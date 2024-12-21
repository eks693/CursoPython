class CadastroClientes:
    def __init__(self, db):
        self.db = db
        self.collection = db['clientes']

    def adicionar_cliente(self, nome, email, telefone):
        cliente_existente = self.collection.find_one({'nome': nome})
        if cliente_existente:
            print(f"Cliente '{nome}' já cadastrado.")
        else:
            self.collection.insert_one({
                'nome': nome,
                'email': email,
                'telefone': telefone
            })
            print(f"Cliente '{nome}' cadastrado com sucesso!")

    def remover_cliente(self, nome):
        cliente = self.collection.find_one({'nome': nome})
        if cliente:
            self.collection.delete_one({'nome': nome})
            print(f"Cliente '{nome}' removido com sucesso!")
        else:
            print(f"Cliente '{nome}' não encontrado.")

    def listar_clientes(self):
        # Corrigido: retorna todos os clientes cadastrados
        return list(self.collection.find())

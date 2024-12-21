class Estoque:
    def __init__(self, db):
        self.db = db
        self.collection = db['estoque']

    def adicionar_produto(self, nome, quantidade):
        # Comando com o MongoDB que encontra  items pelo nome
        item = self.collection.find_one({'nome': nome})
        if item:
           nova_quantidade = item['quantidade'] + quantidade
           # Update com o comando MongoDB
           self.collection.update_one({'nome': nome}, {'$set': {'quantidade': nova_quantidade}})
        # Caso o item não exista, insere um novo item
        else:
            self.collection.insert_one({
                'nome': nome,
                'quantidade': quantidade
           })
        
    def remover_produto(self, nome, quantidade):
        item = self.collection.find_one({'nome': nome})
        if item:
            nova_quantidade = item['quantidade'] - quantidade
            #Comando de deletar mongodb
            if nova_quantidade <= 0:
                self.collection.delete_one({'nome': nome})
            else:
                #Comando de update mongodb
                self.collection.update_one({
                    'nome': nome},
                    {'$set': {'quantidade': nova_quantidade}})
        else:
            print(f'Item {nome} não encontrado')

    def listar_itens(self):
        for item in self.collection.find():
            return list(self.collection.find())
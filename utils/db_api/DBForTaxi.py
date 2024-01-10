from utils.db_api.mongoDb import collectionAll, collectionCs, collectionDr, products


async def get_Drivers():
    productsAdd = []

    documents = collectionDr3.find({})
    for document in await documents.to_list(length=100):
        productsAdd.append(document)
    return productsAdd

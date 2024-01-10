from utils.db_api.mongoDb import collectionAll, collectionCs, collectionDr, products


# Products

async def get_categories():
    productsAdd = []
    documents = products.find()
    for document in await documents.to_list(length=100):
        productsAdd.append(document)
    return productsAdd


async def get_subcategories(category_code):
    productsAdd = []

    documents = products.find({"category_code": category_code})

    for document in await documents.to_list(length=100):
        productsAdd.append(document)
    return productsAdd


async def count_products(category_code, subcategory_code=None):
    if subcategory_code:
        count = await products.count_documents({"category_code": category_code, "subcategory_code": subcategory_code})
        return count
    else:
        count = await products.count_documents({"category_code": category_code})
        return count


async def get_products(category_code, subcategory_code):
    productsAdd = []

    documents = products.find({"category_code": category_code})
    for document in await documents.to_list(length=100):
        productsAdd.append(document)
    return productsAdd


async def get_product(item_id):

    document = await products.find_one({"id": item_id})
    return document


async def add_product(
        id,
        category_code,
        category_name,
        subcategory_code,
        subcategory_name,
        productname,
        photo=None,
        price=None,
        description=""):
    await products.insert_one({
        "id": id,
        "category_code": category_code,
        "category_name": category_name,
        "subcategory_code": subcategory_code,
        "subcategory_name": subcategory_name,
        "productname": productname,
        "photo": photo,
        "price": price,
        "description": description
    })


async def delete_product(category_code):
    await products.delete_one({'category_code': category_code})

    # All Users


async def delete_products():
    await products.delete_many({})

    # All Users


async def drop_products():
    await products.drop()


async def add_new_all_user(tg_id, username, firstname, lastname):

    await collectionAll.insert_one({"tg_id": tg_id,
                                    "username": username,
                                    "firstname": firstname,
                                    "lastname": lastname
                                    })
# cursor = collectionAll.find()
# for document in await cursor.to_list(length=100):
#     print(document)


async def update_new_all_user(get_id, tg_id, username, firstname, lastname):
    await collectionAll.update_one({'tg_id': get_id}, {'$set': {"tg_id": tg_id,
                                                                "username": username,
                                                                "firstname": firstname,
                                                                "lastname": lastname
                                                                }})


async def delete_new_all_user(tg_id):
    await collectionAll.delete_one({'tg_id': tg_id})


async def show_all_user(tg_id):
    document = await collectionAll.find_one({"tg_id": tg_id})
    print(document)


async def show_all_users():
    user = []
    cursor = collectionAll.find()
    for document in await cursor.to_list(length=100):
        user.append(document)
    return user


async def count_all_user(tg_id):
    count = await collectionAll.count_documents({"tg_id": tg_id})
    return count


async def count_all_users():
    count = await collectionAll.count_documents({})
    return count

# /////////////  Driver Haqida


async def add_new_driver(tg_id, username, firstname, lastname, driverMashina, driverQayerTaxi, kishiSoni, manzil, manzilTuman, name, nameCustomer, phone, yolNarxi):

    await collectionDr.insert_one({"tg_id": tg_id,
                                   "username": username,
                                   "firstname": firstname,
                                   "lastname": lastname,
                                   "driverMashina": driverMashina,
                                   "driverQayerTaxi": driverQayerTaxi,
                                   "kishiSoni": kishiSoni,
                                   "manzil": manzil,
                                   "manzilTuman": manzilTuman,
                                   "name": name,
                                   "nameCustomer": nameCustomer,
                                   "phone": phone,
                                   "yolNarxi": yolNarxi
                                   })


async def add_driver(tg_id, tsh_vd, username, firstname, lastname):

    await collectionDr.insert_one({"tg_id": tg_id,
                                   "tsh_vd": tsh_vd,
                                   "username": username,
                                   "firstname": firstname,
                                   "lastname": lastname
                                   })


async def update_driver(get_id, tg_id, tsh_vd, username, firstname, lastname):
    await collectionDr.update_one({'tg_id': get_id}, {'$set': {"tg_id": tg_id,
                                                               "tsh_vd": tsh_vd,
                                                               "username": username,
                                                               "firstname": firstname,
                                                               "lastname": lastname
                                                               }})


async def update_new_driver(get_id, tg_id, username, firstname, lastname, driverMashina, driverQayerTaxi, kishiSoni, manzil, manzilTuman, name, nameCustomer, phone, yolNarxi):
    await collectionDr.update_one({'tg_id': get_id}, {'$set': {"tg_id": tg_id,
                                                               "username": username,
                                                               "firstname": firstname,
                                                               "lastname": lastname,
                                                               "driverMashina": driverMashina,
                                                               "driverQayerTaxi": driverQayerTaxi,
                                                               "kishiSoni": kishiSoni,
                                                               "manzil": manzil,
                                                               "manzilTuman": manzilTuman,
                                                               "name": name,
                                                               "nameCustomer": nameCustomer,
                                                               "phone": phone,
                                                               "yolNarxi": yolNarxi
                                                               }})


async def delete_driver(tg_id):
    await collectionDr.delete_one({'tg_id': tg_id})


async def show_driver(tg_id):
    document = await collectionDr.find_one({"tg_id": tg_id})
    print(document)


async def show_all_drivers():
    users = []
    cursor = collectionDr.find()
    for document in await cursor.to_list(length=100):
        users.append(document)
    return users


async def count_driver(tg_id):
    count = await collectionDr.count_documents({"tg_id": tg_id})
    return count


async def count_drivers():
    count = await collectionDr.count_documents({})
    return count


async def find_driver(tg_id):
    find_user = await collectionDr.find_one({"tg_id": tg_id})
    return find_user


async def find_all_drivers(manzil):
    users = []
    find_user = collectionDr.find({"driverQayerTaxi": manzil})
    for document in await find_user.to_list(length=100):
        users.append(document)
    return users

# /////////////  User Haqida


async def add_new_user(tg_id, username, firstname, lastname, kishiSoni, manzil, manzilTuman, name, nameCustomer, phone, yolNarxi):

    await collectionCs.insert_one({"tg_id": tg_id,
                                   "username": username,
                                   "firstname": firstname,
                                   "lastname": lastname,
                                   "kishiSoni": kishiSoni,
                                   "manzil": manzil,
                                   "manzilTuman": manzilTuman,
                                   "name": name,
                                   "nameCustomer": nameCustomer,
                                   "phone": phone,
                                   "yolNarxi": yolNarxi
                                   })


async def add_user(tg_id, tsh_vd, username, firstname, lastname):

    await collectionCs.insert_one({"tg_id": tg_id,
                                   "tsh_vd": tsh_vd,
                                   "username": username,
                                   "firstname": firstname,
                                   "lastname": lastname
                                   })


async def update_new_user(get_id, tg_id, username, firstname, lastname, kishiSoni, manzil, manzilTuman, name, nameCustomer, phone, yolNarxi):
    await collectionCs.update_one({'tg_id': get_id}, {'$set': {"tg_id": tg_id,
                                                               "username": username,
                                                               "firstname": firstname,
                                                               "lastname": lastname,
                                                               "kishiSoni": kishiSoni,
                                                               "manzil": manzil,
                                                               "manzilTuman": manzilTuman,
                                                               "name": name,
                                                               "nameCustomer": nameCustomer,
                                                               "phone": phone,
                                                               "yolNarxi": yolNarxi
                                                               }})


async def update_user(get_id, tg_id, tsh_vd, username, firstname, lastname):
    await collectionCs.update_one({'tg_id': get_id}, {'$set': {"tg_id": tg_id,
                                                               "tsh_vd": tsh_vd,
                                                               "username": username,
                                                               "firstname": firstname,
                                                               "lastname": lastname
                                                               }})


async def delete_user(tg_id):
    await collectionCs.delete_one({'tg_id': tg_id})


async def show_user(tg_id):
    document = await collectionCs.find_one({"tg_id": tg_id})
    print(document)


async def show_all_users():
    users = []
    cursor = collectionCs.find()
    for document in await cursor.to_list(length=100):
        users.append(document)
    return users


async def count_user(tg_id):
    count = await collectionCs.count_documents({"tg_id": tg_id})
    return count


async def count_users():
    count = await collectionCs.count_documents({})
    return count


async def find_user(tg_id):
    find_user = await collectionCs.find_one({"tg_id": tg_id})
    return find_user


async def find_all_user(manzil):
    users = []
    find_user = collectionCs.find({"manzil": manzil})
    for document in await find_user.to_list(length=100):
        users.append(document)
    return users

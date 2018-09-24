import pymongo

mongo_url = 'mongodb+srv://user:password@example.org/database'
mongodb_client = pymongo.MongoClient(mongo_url)
mongodb = mongodb_client.my_database


def main(params):
    product_id = params['product_id']
    stock_change = int(params['stock_change'])

    result = mongodb.inventory.find_one_and_update(
        {'product_id': product_id},
        {'$inc': {'count': stock_change}},
        upsert=True,
        return_document=pymongo.collection.ReturnDocument.AFTER
    )

    return {
        'product_id': result['product_id'],
        'count': result['count']
    }


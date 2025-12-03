from pymongo import MongoClient

# Подключение
client = MongoClient("mongodb://localhost:27017/")
db = client["testdb"]
users = db["users"]

# Очистим коллекцию (чтобы не дублировать при повторном запуске)
users.delete_many({})

# Вставка документов
users.insert_many([
    {"id": 1, "name": "Анатолий", "age": 28, "gender": "m"},
    {"id": 2, "name": "Светлана", "age": 25, "gender": "f"},
    {"id": 3, "name": "Никита", "age": 33, "gender": "m"},
    {"id": 4, "name": "Ольга", "age": 22, "gender": "f"},
])

# 1. Все женщины
print("Женщины:", list(users.find({"gender": "f"})))

# 2. Женщины и старше 30
print("Женщины >30:", list(users.find({"gender": "f", "age": {"$gt": 30}})))

# 3. Имя в списке
print("Имя в списке:",
      list(users.find({"name": {"$in": ["Анатолий", "Дмитрий", "Ольга", "Семен"]}})))

# 4. id = 3
print("id=3:", list(users.find({"id": 3})))

# 5. Возраст от 30 до 40
print("Возраст 30–40:", list(users.find({"age": {"$gte": 30, "$lte": 40}})))



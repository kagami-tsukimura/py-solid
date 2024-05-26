from item_service import ItemService
from user_service import UserService

if __name__ == "__main__":
    item_service = ItemService()
    user_service = UserService()

    item_service.test()
    user_service.test()
